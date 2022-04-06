import hashlib
import os
from functools import partial

from config import config
from config.setting import Setting
from server.sql_server import SqlServer
from task.qt_task import TaskBase, QtTaskBase
from tools.book import BookMgr, BookEps, Picture
from tools.log import Log
from tools.status import Status
from tools.str import Str


class QtDownloadTask(object):
    Waiting = Str.Waiting
    Reading = Str.Reading
    ReadingEps = Str.ReadingEps
    ReadingPicture = Str.ReadingPicture
    Downloading = Str.Downloading
    Success = Str.Success
    Error = Str.Error
    Cache = Str.Cache

    def __init__(self, downloadId=0):
        self.downloadId = downloadId
        self.downloadCallBack = None       # addData, laveSize
        self.downloadCompleteBack = None   # data, status
        self.statusBack = None
        self.fileSize = 0
        self.url = ""
        self.path = ""
        self.originalName = ""
        self.backParam = None
        self.cleanFlag = ""
        self.lastLaveSize = 0
        self.isInit = False

        self.loadPath = ""    # 只加载
        self.cachePath = ""   # 缓存路径
        self.savePath = ""    # 下载保存路径

        self.bookId = ""      # 下载的bookId
        self.epsId = 0        # 下载的章节
        self.index = 0        # 下载的索引
        self.resetCnt = 0     # 重试次数
        self.isLocal = True
        self.status = self.Waiting


class TaskDownload(TaskBase, QtTaskBase):

    def __init__(self):
        TaskBase.__init__(self)
        QtTaskBase.__init__(self)
        self.taskObj.downloadBack.connect(self.HandlerTask)
        self.taskObj.downloadStBack.connect(self.HandlerTaskSt)
        self.thread.start()

    def Run(self):
        while True:
            v = self._inQueue.get(True)
            self._inQueue.task_done()
            if v == "":
                break
            self.HandlerDownload({"st": Status.Ok}, (v, QtDownloadTask.Waiting))

    def DownloadTask(self, url, path, downloadCallBack=None, completeCallBack=None, downloadStCallBack=None, backParam=None, loadPath="", cachePath="", savePath="", cleanFlag="", isReload=False):
        self.taskId += 1
        data = QtDownloadTask(self.taskId)
        data.downloadCallBack = downloadCallBack
        data.downloadCompleteBack = completeCallBack
        data.backParam = backParam
        data.statusBack = downloadStCallBack
        data.isReload = isReload
        data.url = url
        data.path = path
        data.loadPath = loadPath
        data.cachePath = cachePath
        data.savePath = savePath
        self.tasks[self.taskId] = data
        if cleanFlag:
            data.cleanFlag = cleanFlag
            taskIds = self.flagToIds.setdefault(cleanFlag, set())
            taskIds.add(self.taskId)

        Log.Debug("add download info, cachePath:{}, loadPath:{}, savePath:{}".format(data.cachePath, data.loadPath, data.savePath))
        from server.server import Server
        from server import req
        Server().Download(req.DownloadBookReq(url, data.loadPath, data.cachePath, data.savePath, data.isReload), backParams=self.taskId)
        return self.taskId

    def HandlerTask(self, downloadId, laveFileSize, data, isCallBack=True):
        info = self.tasks.get(downloadId)
        if not info:
            return
        assert isinstance(info, QtDownloadTask)

        # 表示保存失败了
        if laveFileSize == -2:
            v = {"st": Status.SaveError}
            self.CallBookBack(v, info)
            return

        if laveFileSize < 0 and data == b"":
            try:
                if info.downloadCompleteBack:
                    if info.backParam is not None:
                        info.downloadCompleteBack(b"", Str.Error, info.backParam)
                    else:
                        info.downloadCompleteBack(b"", Str.Error)
            except Exception as es:
                Log.Error(es)
            self.ClearDownloadTask(downloadId)
            return

        if info.lastLaveSize <= 0:
            info.lastLaveSize = laveFileSize

        if info.downloadCallBack:
            try:
                if info.backParam is not None:
                    info.downloadCallBack(info.lastLaveSize-laveFileSize, laveFileSize, info.backParam)
                else:
                    info.downloadCallBack(info.lastLaveSize-laveFileSize, laveFileSize)
            except Exception as es:
                Log.Error(es)
            info.lastLaveSize = laveFileSize

        if laveFileSize == 0 and data != b"":
            if info.downloadCompleteBack:
                try:
                    if info.cleanFlag:
                        taskIds = self.flagToIds.get(info.cleanFlag, set())
                        taskIds.discard(info.downloadId)
                    if info.backParam is not None:
                        info.downloadCompleteBack(data, Status.Ok, info.backParam)
                    else:
                        info.downloadCompleteBack(data, Status.Ok)
                except Exception as es:
                    Log.Error(es)
            self.ClearDownloadTask(downloadId)

    def DownloadBook(self, bookId, epsId, index, statusBack=None, downloadCallBack=None, completeCallBack=None,
                    backParam=None, loadPath="", cachePath="", savePath="", cleanFlag=None, isInit=False):
        self.taskId += 1
        data = QtDownloadTask(self.taskId)
        data.downloadCallBack = downloadCallBack
        data.downloadCompleteBack = completeCallBack
        data.isInit = isInit
        data.statusBack = statusBack
        data.backParam = backParam
        data.bookId = bookId
        data.epsId = epsId
        data.index = index
        data.loadPath = loadPath
        data.cachePath = cachePath
        data.savePath = savePath
        self.tasks[self.taskId] = data
        if cleanFlag:
            data.cleanFlag = cleanFlag
            taskIds = self.flagToIds.setdefault(cleanFlag, set())
            taskIds.add(self.taskId)
        Log.Debug("add download info, savePath:{}, loadPath:{}".format(data.savePath, data.loadPath))
        self._inQueue.put(self.taskId)
        return self.taskId

    def HandlerDownload(self, data, v):
        (taskId, newStatus) = v
        task = self.tasks.get(taskId)
        if not task:
            return
        backData = {}
        from server import req, ToolUtil
        try:
            assert isinstance(task, QtDownloadTask)
            isReset = False
            if data["st"] != Status.Ok:
                task.resetCnt += 1

                # 失败了
                if task.resetCnt >= 5:
                    self.SetTaskStatus(taskId, backData, task.Error)
                    return

                isReset = True
            else:
                task.status = newStatus
            info = BookMgr().GetBook(task.bookId)
            if task.status == task.Waiting:
                isReset or self.SetTaskStatus(taskId, backData, task.Reading)
                if not info:
                    if task.isLocal:
                        task.isLocal = False
                        self.AddSqlTask("book", task.bookId, SqlServer.TaskTypeCacheBook, self.HandlerDownload, (taskId, task.Waiting))
                    else:
                        self.AddHttpTask(req.GetComicsBookReq(task.bookId), self.HandlerDownload, (taskId, task.Reading), task.cleanFlag)
                    return

                task.status = task.Reading
            if task.status == task.Reading:
                isReset or self.SetTaskStatus(taskId, backData, task.ReadingEps)
                if not info.eps:
                    self.AddHttpTask(req.GetComicsBookEpsReq(task.bookId), self.HandlerDownload, (taskId, task.ReadingEps), task.cleanFlag)
                    return

                task.status = task.ReadingEps
            if task.status == task.ReadingEps:
                isReset or self.SetTaskStatus(taskId, backData, task.ReadingPicture)
                if task.epsId >= len(info.eps):
                    self.SetTaskStatus(taskId, backData, task.Error)
                    return
                epsInfo = info.eps[task.epsId]
                assert isinstance(epsInfo, BookEps)
                if not epsInfo.pics:
                    self.AddHttpTask(req.GetComicsBookOrderReq(task.bookId, task.epsId+1), self.HandlerDownload, (taskId, task.ReadingPicture), task.cleanFlag)
                    return
                task.status = task.ReadingPicture
            if task.status == task.ReadingPicture:
                epsInfo = info.eps[task.epsId]
                assert isinstance(epsInfo, BookEps)
                backData["maxPic"] = len(epsInfo.pics)
                backData["title"] = epsInfo.title
                backData["maxEps"] = len(info.eps)
                backData["bookName"] = info.title
                isReset or self.SetTaskStatus(taskId, backData, task.Downloading)

                if task.isInit:
                    self.SetTaskStatus(taskId, backData, task.Success)
                    return

                if task.savePath:
                    if ToolUtil.IsHaveFile(task.savePath):
                        self.SetTaskStatus(taskId, backData, task.Cache)
                        return
                else:
                    path = ToolUtil.GetRealPath(task.index+1, "book/{}/{}".format(task.bookId, task.epsId+1))
                    cachePath2 = os.path.join(os.path.join(Setting.SavePath.value, config.CachePathDir), path)
                    checkPaths = [task.loadPath]

                    if Setting.SavePath.value:
                        checkPaths.append(cachePath2)
                        task.cachePath = cachePath2

                    for cachePath in checkPaths:
                        if cachePath:
                            imgData = ToolUtil.LoadCachePicture(cachePath)
                            if imgData:
                                TaskBase.taskObj.downloadBack.emit(taskId, len(imgData), b"")
                                TaskBase.taskObj.downloadBack.emit(taskId, 0, imgData)
                                return

                if task.index >= len(epsInfo.pics):
                    self.SetTaskStatus(taskId, backData, task.Error)
                    return

                picInfo = epsInfo.pics[task.index]
                assert isinstance(picInfo, Picture)
                from server.server import Server
                url = ToolUtil.GetRealUrl(picInfo.fileServer, picInfo.path)

                self.AddDownloadTask(
                    url, "", task.downloadCallBack, task.downloadCompleteBack, task.statusBack,
                    task.backParam, task.loadPath, task.cachePath, task.savePath, task.cleanFlag)
        except Exception as es:
            Log.Error(es)
        return

    def SetTaskStatus(self, taskId, backData, status):
        backData["st"] = status
        self.taskObj.downloadStBack.emit(taskId, dict(backData))
        return

    def CallBookBack(self, data, task):
        try:
            if not task.statusBack:
                return
            if task.backParam is not None:
                task.statusBack(data, task.backParam)
            else:
                task.statusBack(data)
        except Exception as es:
            Log.Error(es)

    def HandlerTaskSt(self, downloadId, data):
        task = self.tasks.get(downloadId)
        if not task:
            return
        assert isinstance(task, QtDownloadTask)
        try:
            self.CallBookBack(data, task)
            status = task.status
            if status == task.Downloading or status == task.Error or status == task.Cache:
                self.ClearDownloadTask(downloadId)
        except Exception as es:
            Log.Error(es)

    def ClearDownloadTask(self, downloadId):
        info = self.tasks.get(downloadId)
        if not info:
            return
        del self.tasks[downloadId]
