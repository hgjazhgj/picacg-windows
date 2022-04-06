from PySide6.QtCore import QObject, QCoreApplication


class QtStrObj(QObject):
    def __init__(self):
        QObject.__init__(self)


class Str:
    IconList = "😄😆😊😃😏😍😘😚😳😌😆😁😉😜😝😀😗😙😛😴😟😦😧😮😬😕😯😑😒😅😓😥😩😔😞😖😨😰😣😢😭😂😲😱😫😠😡😤😪😋😷😎😵👿😈😐😶😇👽💛💙💜💚💔💆💇💅👦👧👩👨👶👵👴👱👲👳👷👮👼👸😺😸😻😽😼🙀😿😹😾👹👺🙈🙉🙊💂💀🐾👄💋💧👂👀👃👅💌👤👥💬💭"

    obj = None
    strDict = dict()

    # Enum

    Ok = 1001              # "成功"
    Load = 1002            # "加载"
    Error = 1003           # "错误"
    WaitLoad = 1004        # "等待"
    NetError = 1005        # "网络错误，请检查代理设置"
    UserError = 1006       # "用户名密码错误"
    RegisterError = 1007   # "注册失败"
    UnKnowError = 1008     # "未知错误，"
    NotFoundBook = 1009    # "未找到书籍"
    ParseError = 1010      # "解析出错了"
    NeedGoogle = 1011      # "需要谷歌验证"
    SetHeadError = 1012    # "头像设置出错了, 请尽量选择500kb以下的图片，"
    UnderReviewBook = 1013  # "本子审核中"
    NotLogin = 1014         # "未登录"
    SaveError = 1015         # "保存出错"
    Cache = 1016         # "缓存"
    AddError = 1017         # "Add错误"
    PathError = 1018         # "路径错误"
    FileError = 1019         # "未发现源文件"
    FileFormatError = 1020   # "文件损坏"

    Success = 2001         # "下载完成"
    Reading = 2002         # "获取信息"
    ReadingEps = 2003      # "获取分页"
    ReadingPicture = 2004  # "获取下载地址"
    DownloadCover = 2005   # "正在下载封面"
    Downloading = 2006     # "正在下载"
    Waiting = 2007         # "等待中"
    Pause = 2008           # "暂停"
    DownError = 2009       # "出错了"
    NotFound = 2010        # "原始文件不存在"
    Converting = 2011      # "转换中"
    ConvertSuccess = 2012  # "转换成功"

    DownloadSuc = 3001     # "下载完成"
    DownloadError = 3002   # "下载错误"
    DownloadReset = 3003   # "重新下载"
    WaifuWait = 3004       # "等待中"
    WaifuStateStart = 3005     # "转换开始"
    WaifuStateCancle = 3006    # "不转换"
    WaifuStateEnd = 3007       # "转换完成"
    WaifuStateFail = 3008      # "转换失败"
    OverResolution = 3009      # "超过设置分辨率"

    LoadingPicture = 1     # "图片加载中..."
    LoadingFail = 2        # "图片加载失败"
    LoginCookie = 3        # "使用Cookie登录"
    LoginUser = 4          # "使用账号登录"
    NotSpace = 5           # "不能为空"
    LoginFail = 6          # "登录失败"

    Menu = 10              # 菜单
    FullSwitch = 11        # 全屏切换
    ReadMode = 12          # 阅读模式

    UpDownScroll = 13      # 上下滚动
    Default = 14           # 默认
    LeftRightDouble = 15   # 左右双页
    RightLeftDouble = 16   # 右左双页
    LeftRightScroll = 17   # 左右滚动
    RightLeftScroll = 18   # 右左滚动
    Scale = 19             # 缩放
    SwitchPage = 20        # 切页
    LastChapter = 21       # 上一章
    NextChapter = 22       # 下一章
    Exit = 23              # 退出
    AutoScroll = 24        # 自动滚动/翻页
    ExitFullScreen = 25    # 退出全屏
    FullScreen = 26        # 全屏
    ContinueRead = 27      # 继续阅读
    Page = 28              # 页
    AlreadyLastPage = 29   # 已经是第一页
    AlreadyNextPage = 30   # 已经最后一页
    AutoSkipLast = 31      # 自动跳转到上一章
    AutoSkipNext = 32      # 自动跳转到下一章
    Position = 33          # 位置
    Resolution = 34        # 分辨率
    Size = 35              # 大小
    State = 36             # 状态
    DownloadNot = 37       # 下载未完成
    NotRecommendWaifu2x = 38  # Waifu2x当前为CPU模式，看图模式下不推荐开启
    StopAutoScroll = 39    # 自动滚动/翻页已停止
    LastPage = 40          # 上一页
    NextPage = 41          # 下一页
    LastScroll = 42        # 上滑
    NextScroll = 43        # 下滑
    NoProxy = 44           # 无代理
    SaveSuc = 45           # 保存成功
    Login = 46             # 登录
    Register = 47          # 注册
    SpeedTest = 48         # 测速
    PasswordShort = 49     # 密码太短
    RegisterSuc = 50       # 注册成功
    ComicFinished = 51     # 完结
    SelectFold = 52        # 选择文件夹
    Save = 53              # 保存
    CommentLoadFail = 54   # 评论加载失败
    Top = 55               # 置顶
    The = 56               # 第
    Floor = 57             # 楼
    DayAgo = 58            # 天前
    HourAgo = 59           # 小时前
    MinuteAgo = 60         # 分钟前
    SecondAgo = 61         # 秒前
    FavoriteNum = 62       # 收藏数
    FavoriteLoading = 63   # 正在加载收藏分页
    Updated = 64           # 更新完成
    Picture = 65           # 图片
    Sending = 66           # "正在发送"
    OnlineNum = 67         # "在线人数"
    AlreadyLastChapter = 68  # 已经是第一章
    AlreadyNextChapter = 69  # 已经最后一章
    ChapterLoadFail = 70     # 章节加载失败
    AddFavoriteSuc = 71      # 添加收藏成功
    Convert = 72             # 转换
    CopySuc = 73             # 复制成功
    HeadUpload = 74          # "头像上传中......"
    Update = 75              # 更新
    AlreadySign = 76         # 已打卡
    Sign = 77                # 打卡
    Hidden = 78              # 屏蔽
    NotHidden = 79           # 取消屏蔽
    OpenDir = 80             # 打开目录
    DeleteRecord = 81        # 删除记录
    DeleteRecordFile = 82    # 删除记录和文件
    SelectEps = 83           # 选择下载章节
    Start = 84               # 开始
    StartConvert = 85        # 开始转换
    PauseConvert = 86        # 暂停转换

    Open = 87                # 打开
    LookCover = 88           # 查看封面
    ReDownloadCover = 89     # 重下封面
    Waifu2xConvert = 90      # Waifu2x转换
    CopyTitle = 91           # 复制标题
    Download = 92            # 下载
    Delete = 93              # 删除
    CurVersion = 94          # 当前版本
    CheckUpdateAndUp = 95    # 检查到更新，是否前往更新
    CopyAndroid = 96         # 复制Android下载地址
    CopyIos = 97             # 复制IOS下载地址
    SetDir = 98              # 请设置目录
    AddDownload = 99         # 添加下载成功
    LookFirst = 100          # 观看第1章
    LastLook = 101           # 上次看到第
    Chapter = 102            # 章
    Looked = 103             # 看过
    PressEnter = 104         # 按Enter发送消息
    PressCtrlEnter = 105     # 按Ctrl+Enter发送消息
    DelWaifu2xConvert = 106     # 取消Waifu2x转换
    NeedResetSave = 107      # 需要重启保存
    CheckUp = 108            # 检查更新
    DailyUpdated = 109            # 今日已更新
    HaveUpdate = 110            # 有更新
    AlreadyUpdate = 111            # 已是最新
    AgoUpdate = 112                # 最近更新
    LeaveMsg = 113                # 留言板
    Rank = 114                # 排行榜
    RandomBook = 115                # 随机本子
    DeleteSuc = 116                 # 删除成功
    All = 117                       # 所有
    Favorite = 118                  # 收藏
    Classify = 119                  # 分类
    Comment = 120                  # 评论
    Change = 121                   # 更改
    SwitchSite = 122               # 表里切换
    DelFavoriteSuc = 123           # 删除收藏成功
    AllComment = 124               # 所有评论
    Move = 125               # 移动
    Add = 126                # 新增
    SelectAll = 127                # 全选
    NotSelectAll = 128             # 反选
    MyComment = 129          # 我的评论
    LoginOut = 130                # 登出
    Sock5Error = 131              # Sock5设置出错

    @classmethod
    def Reload(cls):
        cls.obj = QtStrObj()
        cls.obj.setObjectName(u"ObjTr")
        cls.strDict[cls.Ok] = QCoreApplication.translate("cls.obj", "成功", None)
        cls.strDict[cls.Load] = QCoreApplication.translate("cls.obj",  "加载", None)
        cls.strDict[cls.Error] = QCoreApplication.translate("cls.obj",  "错误", None)
        cls.strDict[cls.WaitLoad] = QCoreApplication.translate("cls.obj",  "等待", None)
        cls.strDict[cls.NetError] = QCoreApplication.translate("cls.obj",  "网络错误，请检查代理设置", None)
        cls.strDict[cls.UserError] = QCoreApplication.translate("cls.obj",  "用户名密码错误", None)
        cls.strDict[cls.RegisterError] = QCoreApplication.translate("cls.obj",  "注册失败", None)
        cls.strDict[cls.UnKnowError] = QCoreApplication.translate("cls.obj",  "未知错误", None)
        cls.strDict[cls.NotFoundBook] = QCoreApplication.translate("cls.obj",  "未找到书籍", None)
        cls.strDict[cls.ParseError] = QCoreApplication.translate("cls.obj",  "解析出错了", None)
        cls.strDict[cls.NeedGoogle] = QCoreApplication.translate("cls.obj",  "需要谷歌验证", None)
        cls.strDict[cls.SetHeadError] = QCoreApplication.translate("cls.obj",  "头像设置出错了, 请尽量选择500kb以下的图片", None)
        cls.strDict[cls.UnderReviewBook] = QCoreApplication.translate("cls.obj",  "本子审核中", None)
        cls.strDict[cls.NotLogin] = QCoreApplication.translate("cls.obj",  "未登录", None)
        cls.strDict[cls.SaveError] = QCoreApplication.translate("cls.obj",  "保存出错", None)
        cls.strDict[cls.Cache] = QCoreApplication.translate("cls.obj",  "缓存", None)
        cls.strDict[cls.AddError] = QCoreApplication.translate("cls.obj",  "Add错误", None)
        cls.strDict[cls.PathError] = QCoreApplication.translate("cls.obj",  "路径错误", None)
        cls.strDict[cls.FileError] = QCoreApplication.translate("cls.obj",  "未发现源文件", None)
        cls.strDict[cls.FileFormatError] = QCoreApplication.translate("cls.obj",  "文件损坏", None)

        cls.strDict[cls.LoadingPicture] = QCoreApplication.translate("cls.obj",  "图片加载中...", None)
        cls.strDict[cls.LoadingFail] = QCoreApplication.translate("cls.obj",  "图片加载失败", None)
        cls.strDict[cls.LoginCookie] = QCoreApplication.translate("cls.obj",  "使用Cookie登录", None)
        cls.strDict[cls.LoginUser] = QCoreApplication.translate("cls.obj",  "使用账号登录", None)
        cls.strDict[cls.NotSpace] = QCoreApplication.translate("cls.obj",  "不能为空", None)
        cls.strDict[cls.LoginFail] = QCoreApplication.translate("cls.obj",  "登录失败", None)
        cls.strDict[cls.Success] = QCoreApplication.translate("cls.obj",  "下载完成", None)
        cls.strDict[cls.Reading] = QCoreApplication.translate("cls.obj",  "获取信息", None)
        cls.strDict[cls.ReadingEps] = QCoreApplication.translate("cls.obj",  "获取分页", None)
        cls.strDict[cls.ReadingPicture] = QCoreApplication.translate("cls.obj",  "获取下载地址", None)
        cls.strDict[cls.DownloadCover] = QCoreApplication.translate("cls.obj",  "正在下载封面", None)
        cls.strDict[cls.Downloading] = QCoreApplication.translate("cls.obj",  "正在下载", None)
        cls.strDict[cls.Waiting] = QCoreApplication.translate("cls.obj",  "等待中", None)
        cls.strDict[cls.Pause] = QCoreApplication.translate("cls.obj",  "暂停", None)
        cls.strDict[cls.DownError] = QCoreApplication.translate("cls.obj",  "出错了", None)
        cls.strDict[cls.NotFound] = QCoreApplication.translate("cls.obj",  "原始文件不存在", None)
        cls.strDict[cls.Converting] = QCoreApplication.translate("cls.obj",  "转换中", None)
        cls.strDict[cls.ConvertSuccess] = QCoreApplication.translate("cls.obj",  "转换成功", None)
        cls.strDict[cls.DownloadSuc] = QCoreApplication.translate("cls.obj",  "下载完成", None)
        cls.strDict[cls.DownloadError] = QCoreApplication.translate("cls.obj",  "下载错误", None)
        cls.strDict[cls.DownloadReset] = QCoreApplication.translate("cls.obj",  "重新下载", None)
        cls.strDict[cls.WaifuWait] = QCoreApplication.translate("cls.obj",  "等待中", None)
        cls.strDict[cls.WaifuStateStart] = QCoreApplication.translate("cls.obj",  "转换开始", None)
        cls.strDict[cls.WaifuStateCancle] = QCoreApplication.translate("cls.obj",  "不转换", None)
        cls.strDict[cls.WaifuStateEnd] = QCoreApplication.translate("cls.obj",  "转换完成", None)
        cls.strDict[cls.WaifuStateFail] = QCoreApplication.translate("cls.obj",  "转换失败", None)
        cls.strDict[cls.OverResolution] = QCoreApplication.translate("cls.obj",  "超过设置分辨率", None)

        cls.strDict[cls.Menu] = QCoreApplication.translate("cls.obj",  "菜单", None)
        cls.strDict[cls.FullSwitch] = QCoreApplication.translate("cls.obj",  "全屏切换", None)
        cls.strDict[cls.ReadMode] = QCoreApplication.translate("cls.obj",  "阅读模式", None)
        cls.strDict[cls.UpDownScroll] = QCoreApplication.translate("cls.obj",  "上下滚动", None)
        cls.strDict[cls.Default] = QCoreApplication.translate("cls.obj",  "默认", None)
        cls.strDict[cls.LeftRightDouble] = QCoreApplication.translate("cls.obj",  "左右双页", None)
        cls.strDict[cls.RightLeftDouble] = QCoreApplication.translate("cls.obj",  "右左双页", None)
        cls.strDict[cls.LeftRightScroll] = QCoreApplication.translate("cls.obj",  "左右滚动", None)
        cls.strDict[cls.RightLeftScroll] = QCoreApplication.translate("cls.obj",  "右左滚动", None)
        cls.strDict[cls.Scale] = QCoreApplication.translate("cls.obj",  "缩放", None)
        cls.strDict[cls.SwitchPage] = QCoreApplication.translate("cls.obj",  "切页", None)
        cls.strDict[cls.LastChapter ]= QCoreApplication.translate("cls.obj",  "上一章", None)
        cls.strDict[cls.NextChapter] = QCoreApplication.translate("cls.obj",  "下一章", None)
        cls.strDict[cls.Exit] = QCoreApplication.translate("cls.obj",  "退出", None)
        cls.strDict[cls.AutoScroll] = QCoreApplication.translate("cls.obj",  "自动滚动/翻页", None)
        cls.strDict[cls.ExitFullScreen] = QCoreApplication.translate("cls.obj",  "退出全屏", None)
        cls.strDict[cls.FullScreen] = QCoreApplication.translate("cls.obj",  "全屏", None)
        cls.strDict[cls.ContinueRead] = QCoreApplication.translate("cls.obj",  "继续阅读", None)
        cls.strDict[cls.Page] = QCoreApplication.translate("cls.obj",  "页", None)
        cls.strDict[cls.AlreadyLastPage] = QCoreApplication.translate("cls.obj",  "已经是第一页", None)
        cls.strDict[cls.AlreadyNextPage] = QCoreApplication.translate("cls.obj",  "已经最后一页", None)
        cls.strDict[cls.AutoSkipLast] = QCoreApplication.translate("cls.obj",  "自动跳转到上一章", None)
        cls.strDict[cls.AutoSkipNext] = QCoreApplication.translate("cls.obj",  "自动跳转到下一章", None)
        cls.strDict[cls.Position] = QCoreApplication.translate("cls.obj",  "位置", None)
        cls.strDict[cls.Resolution] = QCoreApplication.translate("cls.obj",  "分辨率", None)
        cls.strDict[cls.Size] = QCoreApplication.translate("cls.obj",  "大小", None)
        cls.strDict[cls.State] = QCoreApplication.translate("cls.obj",  "状态", None)
        cls.strDict[cls.DownloadNot] = QCoreApplication.translate("cls.obj",  "下载未完成", None)
        cls.strDict[cls.NotRecommendWaifu2x] = QCoreApplication.translate("cls.obj",  "Waifu2x当前为CPU模式，看图模式下不推荐开启", None)
        cls.strDict[cls.StopAutoScroll] = QCoreApplication.translate("cls.obj",  "自动滚动/翻页已停止", None)
        cls.strDict[cls.LastPage] = QCoreApplication.translate("cls.obj",  "上一页", None)
        cls.strDict[cls.NextPage] = QCoreApplication.translate("cls.obj",  "下一页", None)
        cls.strDict[cls.LastScroll] = QCoreApplication.translate("cls.obj",  "上滑", None)
        cls.strDict[cls.NextScroll] = QCoreApplication.translate("cls.obj",  "下滑", None)

        cls.strDict[cls.NoProxy] = QCoreApplication.translate("cls.obj",  "无代理", None)
        cls.strDict[cls.SaveSuc] = QCoreApplication.translate("cls.obj",  "保存成功", None)
        cls.strDict[cls.Login] = QCoreApplication.translate("cls.obj",  "登录", None)
        cls.strDict[cls.Register] = QCoreApplication.translate("cls.obj",  "注册", None)
        cls.strDict[cls.SpeedTest] = QCoreApplication.translate("cls.obj",  "测速", None)
        cls.strDict[cls.PasswordShort] = QCoreApplication.translate("cls.obj",  "密码太短", None)
        cls.strDict[cls.RegisterSuc] = QCoreApplication.translate("cls.obj",  "注册成功", None)
        cls.strDict[cls.ComicFinished] = QCoreApplication.translate("cls.obj",  "完结", None)
        cls.strDict[cls.SelectFold] = QCoreApplication.translate("cls.obj",  "选择文件夹", None)
        cls.strDict[cls.Save] = QCoreApplication.translate("cls.obj",  "保存", None)
        cls.strDict[cls.CommentLoadFail] = QCoreApplication.translate("cls.obj",  "评论加载失败", None)
        cls.strDict[cls.Top] = QCoreApplication.translate("cls.obj",  "置顶", None)
        cls.strDict[cls.The] = QCoreApplication.translate("cls.obj",  "第", None)
        cls.strDict[cls.Floor] = QCoreApplication.translate("cls.obj",  "楼", None)
        cls.strDict[cls.DayAgo] = QCoreApplication.translate("cls.obj",  "天前", None)
        cls.strDict[cls.HourAgo] = QCoreApplication.translate("cls.obj",  "小时前", None)
        cls.strDict[cls.MinuteAgo] = QCoreApplication.translate("cls.obj",  "分钟前", None)
        cls.strDict[cls.SecondAgo] = QCoreApplication.translate("cls.obj",  "秒前", None)
        cls.strDict[cls.FavoriteNum] = QCoreApplication.translate("cls.obj",  "收藏数", None)
        cls.strDict[cls.FavoriteLoading] = QCoreApplication.translate("cls.obj",  "正在加载收藏分页", None)
        cls.strDict[cls.Updated] = QCoreApplication.translate("cls.obj",  "更新完成", None)
        cls.strDict[cls.Picture] = QCoreApplication.translate("cls.obj",  "图片", None)
        cls.strDict[cls.Sending] = QCoreApplication.translate("cls.obj",  "正在发送", None)
        cls.strDict[cls.OnlineNum] = QCoreApplication.translate("cls.obj",  "在线人数", None)
        cls.strDict[cls.AlreadyLastChapter] = QCoreApplication.translate("cls.obj",  "已经是第一章", None)
        cls.strDict[cls.AlreadyNextChapter] = QCoreApplication.translate("cls.obj",  "已经最后一章", None)
        cls.strDict[cls.ChapterLoadFail] = QCoreApplication.translate("cls.obj",  "章节加载失败", None)
        cls.strDict[cls.AddFavoriteSuc] = QCoreApplication.translate("cls.obj",  "添加收藏成功", None)
        cls.strDict[cls.Convert] = QCoreApplication.translate("cls.obj",  "转换", None)
        cls.strDict[cls.CopySuc] = QCoreApplication.translate("cls.obj",  "复制成功", None)
        cls.strDict[cls.HeadUpload] = QCoreApplication.translate("cls.obj",  "头像上传中......", None)
        cls.strDict[cls.Update] = QCoreApplication.translate("cls.obj",  "更新", None)
        cls.strDict[cls.AlreadySign] = QCoreApplication.translate("cls.obj",  "已打卡", None)
        cls.strDict[cls.Sign] = QCoreApplication.translate("cls.obj",  "打卡", None)
        cls.strDict[cls.Hidden] = QCoreApplication.translate("cls.obj",  "屏蔽", None)
        cls.strDict[cls.NotHidden] = QCoreApplication.translate("cls.obj",  "取消屏蔽", None)
        cls.strDict[cls.OpenDir] = QCoreApplication.translate("cls.obj",  "打开目录", None)
        cls.strDict[cls.DeleteRecord] = QCoreApplication.translate("cls.obj",  "删除记录", None)
        cls.strDict[cls.DeleteRecordFile] = QCoreApplication.translate("cls.obj",  "删除记录和文件 ", None)
        cls.strDict[cls.SelectEps] = QCoreApplication.translate("cls.obj",  "选择下载章节", None)
        cls.strDict[cls.Start] = QCoreApplication.translate("cls.obj",  "开始", None)
        cls.strDict[cls.StartConvert] = QCoreApplication.translate("cls.obj",  "开始转换", None)
        cls.strDict[cls.PauseConvert] = QCoreApplication.translate("cls.obj",  "暂停转换", None)
        cls.strDict[cls.Open] = QCoreApplication.translate("cls.obj",  "打开", None)
        cls.strDict[cls.LookCover] = QCoreApplication.translate("cls.obj",  "查看封面", None)
        cls.strDict[cls.ReDownloadCover] = QCoreApplication.translate("cls.obj",  "重下封面", None)
        cls.strDict[cls.Waifu2xConvert] = QCoreApplication.translate("cls.obj",  "Waifu2x转换", None)
        cls.strDict[cls.CopyTitle] = QCoreApplication.translate("cls.obj",  "复制标题", None)
        cls.strDict[cls.Download] = QCoreApplication.translate("cls.obj",  "下载", None)
        cls.strDict[cls.Delete] = QCoreApplication.translate("cls.obj",  "删除", None)
        cls.strDict[cls.CurVersion] = QCoreApplication.translate("cls.obj",  "当前版本", None)
        cls.strDict[cls.CheckUpdateAndUp] = QCoreApplication.translate("cls.obj",  "检查到更新，是否前往更新", None)
        cls.strDict[cls.CopyAndroid] = QCoreApplication.translate("cls.obj",  "复制Android下载地址", None)
        cls.strDict[cls.CopyIos] = QCoreApplication.translate("cls.obj",  "复制IOS下载地址", None)
        cls.strDict[cls.SetDir] = QCoreApplication.translate("cls.obj",  "请设置目录", None)
        cls.strDict[cls.AddDownload] = QCoreApplication.translate("cls.obj",  "添加下载成功", None)
        cls.strDict[cls.LookFirst] = QCoreApplication.translate("cls.obj",  "观看第1章", None)
        cls.strDict[cls.LastLook] = QCoreApplication.translate("cls.obj",  "上次看到第", None)
        cls.strDict[cls.Chapter] = QCoreApplication.translate("cls.obj",  "章", None)
        cls.strDict[cls.Looked] = QCoreApplication.translate("cls.obj",  "看过", None)
        cls.strDict[cls.PressEnter] = QCoreApplication.translate("cls.obj",  "按Enter发送消息", None)
        cls.strDict[cls.PressCtrlEnter] = QCoreApplication.translate("cls.obj",  "按Ctrl+Enter发送消息", None)
        cls.strDict[cls.DelWaifu2xConvert] = QCoreApplication.translate("cls.obj",  "取消Waifu2x转换", None)
        cls.strDict[cls.NeedResetSave] = QCoreApplication.translate("cls.obj",  "需要重启保存", None)
        cls.strDict[cls.CheckUp] = QCoreApplication.translate("cls.obj",  "检查更新", None)
        cls.strDict[cls.DailyUpdated] = QCoreApplication.translate("cls.obj",  "今日已更新", None)
        cls.strDict[cls.HaveUpdate] = QCoreApplication.translate("cls.obj",  "有更新", None)
        cls.strDict[cls.AlreadyUpdate] = QCoreApplication.translate("cls.obj",  "已是最新", None)
        cls.strDict[cls.AgoUpdate] = QCoreApplication.translate("cls.obj",  "最近更新", None)
        cls.strDict[cls.LeaveMsg] = QCoreApplication.translate("cls.obj",  "留言板", None)
        cls.strDict[cls.Rank] = QCoreApplication.translate("cls.obj",  "排行版", None)
        cls.strDict[cls.RandomBook] = QCoreApplication.translate("cls.obj",  "随机本子", None)
        cls.strDict[cls.DeleteSuc] = QCoreApplication.translate("cls.obj",  "删除成功", None)
        cls.strDict[cls.All] = QCoreApplication.translate("cls.obj",  "所有", None)
        cls.strDict[cls.Favorite] = QCoreApplication.translate("cls.obj",  "收藏", None)
        cls.strDict[cls.Classify] = QCoreApplication.translate("cls.obj",  "分类", None)
        cls.strDict[cls.Comment] = QCoreApplication.translate("cls.obj",  "评论", None)
        cls.strDict[cls.Change] = QCoreApplication.translate("cls.obj",  "更改", None)
        cls.strDict[cls.SwitchSite] = QCoreApplication.translate("cls.obj",  "表里切换", None)
        cls.strDict[cls.DelFavoriteSuc] = QCoreApplication.translate("cls.obj",  "删除收藏成功", None)
        cls.strDict[cls.AllComment] = QCoreApplication.translate("cls.obj",  "所有评论", None)
        cls.strDict[cls.Move] = QCoreApplication.translate("cls.obj",  "移动", None)
        cls.strDict[cls.Add] = QCoreApplication.translate("cls.obj",  "新增", None)
        cls.strDict[cls.SelectAll] = QCoreApplication.translate("cls.obj",  "全选", None)
        cls.strDict[cls.NotSelectAll] = QCoreApplication.translate("cls.obj",  "反选", None)
        cls.strDict[cls.MyComment] = QCoreApplication.translate("cls.obj",  "我的评论", None)
        cls.strDict[cls.LoginOut] = QCoreApplication.translate("cls.obj",  "登出", None)
        cls.strDict[cls.Sock5Error] = QCoreApplication.translate("cls.obj",  "Sock5设置出错", None)

    @classmethod
    def GetStr(cls, enumType):
        return cls.strDict.get(enumType, "")

    @classmethod
    def CheckStr(cls):
        allEnum = set()
        for name in dir(cls):
            value = getattr(cls, name)
            if not isinstance(value, int):
                continue
            if value in allEnum:
                raise Exception("Already exists str: " + name)
            allEnum.add(value)
            if value not in cls.strDict:
                raise Exception("Not Found str: " + name)


if __name__ == "__main__":
    Str.Reload()
    Str.CheckStr()