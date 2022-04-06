import os
import sys

from PySide6.QtCore import Qt

from config.setting import Setting
from tools.log import Log

MainType = 1

Main = None

if sys.platform == "win32" and not Setting.IsNotUseTitleBar.value:
    try:
        from interface.ui_main_windows import Ui_MainWindows
        from .windows.frame_less_widget import FrameLessWidget

        class MainWidget(FrameLessWidget, Ui_MainWindows):
            def __init__(self):
                FrameLessWidget.__init__(self)
                Ui_MainWindows.__init__(self)
                self.setupUi(self)
                self.totalStackWidget.setAttribute(Qt.WA_TranslucentBackground)
                self.widget.setAttribute(Qt.WA_TranslucentBackground)

            def showFullScreen(self):
                self.widget.setVisible(False)
                self.verticalLayout.setContentsMargins(0, 0, 0, 0)
                return FrameLessWidget.showFullScreen(self)

            def showNormal(self):
                self.widget.setVisible(True)
                self.verticalLayout.setContentsMargins(3, 3, 3, 3)
                return FrameLessWidget.showNormal(self)

            def showMaximized(self):
                self.widget.setVisible(True)
                self.verticalLayout.setContentsMargins(3, 3, 3, 3)
                return FrameLessWidget.showMaximized(self)

            def setSubTitle(self, text):
                self.widget.subTitle.setText(text)
                return

        Main = MainWidget
        MainType = 2
    except Exception as es:
        Log.Error(es)

if not Main:
    from interface.ui_main import Ui_Main
    from PySide6.QtWidgets import QMainWindow

    class MainWidget(QMainWindow, Ui_Main):
        def __init__(self):
            QMainWindow.__init__(self)
            Ui_Main.__init__(self)
            self.setupUi(self)

        def setSubTitle(self, text):
            return

    Main = MainWidget
