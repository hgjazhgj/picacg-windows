# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_navigation.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

from component.label.head_label import HeadLabel
from component.scroll_area.smooth_scroll_area import SmoothScrollArea
import images_rc

class Ui_Navigation(object):
    def setupUi(self, Navigation):
        if not Navigation.objectName():
            Navigation.setObjectName(u"Navigation")
        Navigation.resize(248, 473)
        Navigation.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Navigation)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Navigation)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.picLabel = HeadLabel(self.widget)
        self.picLabel.setObjectName(u"picLabel")
        self.picLabel.setMinimumSize(QSize(100, 100))
        self.picLabel.setMaximumSize(QSize(100, 100))
        self.picLabel.setPixmap(QPixmap(u":/png/icon/placeholder_avatar.png"))
        self.picLabel.setScaledContents(True)

        self.verticalLayout.addWidget(self.picLabel, 0, Qt.AlignHCenter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setFocusPolicy(Qt.NoFocus)

        self.horizontalLayout_2.addWidget(self.loginButton)

        self.signButton = QPushButton(self.widget)
        self.signButton.setObjectName(u"signButton")
        sizePolicy.setHeightForWidth(self.signButton.sizePolicy().hasHeightForWidth())
        self.signButton.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.signButton)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.nameLabel = QLabel(self.widget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.verticalLayout.addWidget(self.nameLabel)

        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setMinimumSize(QSize(150, 0))

        self.verticalLayout.addWidget(self.titleLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.expLabel = QLabel(self.widget)
        self.expLabel.setObjectName(u"expLabel")

        self.horizontalLayout.addWidget(self.expLabel)

        self.levelLabel = QLabel(self.widget)
        self.levelLabel.setObjectName(u"levelLabel")

        self.horizontalLayout.addWidget(self.levelLabel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.scrollArea = SmoothScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 211, 654))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 9, 0, 9)
        self.label = QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.collectButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup = QButtonGroup(Navigation)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.collectButton)
        self.collectButton.setObjectName(u"collectButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.collectButton.sizePolicy().hasHeightForWidth())
        self.collectButton.setSizePolicy(sizePolicy1)
        self.collectButton.setMinimumSize(QSize(150, 40))
        self.collectButton.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/images/menu/Contact.png", QSize(), QIcon.Normal, QIcon.Off)
        self.collectButton.setIcon(icon)
        self.collectButton.setIconSize(QSize(32, 32))
        self.collectButton.setCheckable(True)
        self.collectButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.collectButton)

        self.myCommentButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.myCommentButton)
        self.myCommentButton.setObjectName(u"myCommentButton")
        sizePolicy1.setHeightForWidth(self.myCommentButton.sizePolicy().hasHeightForWidth())
        self.myCommentButton.setSizePolicy(sizePolicy1)
        self.myCommentButton.setMinimumSize(QSize(150, 40))
        self.myCommentButton.setFocusPolicy(Qt.NoFocus)
        self.myCommentButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/theme/svg/user_comment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.myCommentButton.setIcon(icon1)
        self.myCommentButton.setIconSize(QSize(32, 32))
        self.myCommentButton.setCheckable(True)
        self.myCommentButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.myCommentButton)

        self.lookButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.lookButton)
        self.lookButton.setObjectName(u"lookButton")
        sizePolicy1.setHeightForWidth(self.lookButton.sizePolicy().hasHeightForWidth())
        self.lookButton.setSizePolicy(sizePolicy1)
        self.lookButton.setMinimumSize(QSize(150, 40))
        self.lookButton.setFocusPolicy(Qt.NoFocus)
        self.lookButton.setIcon(icon)
        self.lookButton.setIconSize(QSize(32, 32))
        self.lookButton.setCheckable(True)
        self.lookButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.lookButton)

        self.line = QFrame(self.scrollAreaWidgetContents)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.label_2 = QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.indexButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.indexButton)
        self.indexButton.setObjectName(u"indexButton")
        sizePolicy1.setHeightForWidth(self.indexButton.sizePolicy().hasHeightForWidth())
        self.indexButton.setSizePolicy(sizePolicy1)
        self.indexButton.setMinimumSize(QSize(150, 40))
        self.indexButton.setFocusPolicy(Qt.NoFocus)
        self.indexButton.setIcon(icon)
        self.indexButton.setIconSize(QSize(32, 32))
        self.indexButton.setCheckable(True)
        self.indexButton.setChecked(True)
        self.indexButton.setPopupMode(QToolButton.DelayedPopup)
        self.indexButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.indexButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.indexButton)

        self.searchButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.searchButton)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy1.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy1)
        self.searchButton.setMinimumSize(QSize(150, 40))
        self.searchButton.setFocusPolicy(Qt.NoFocus)
        self.searchButton.setIcon(icon)
        self.searchButton.setIconSize(QSize(32, 32))
        self.searchButton.setCheckable(True)
        self.searchButton.setPopupMode(QToolButton.DelayedPopup)
        self.searchButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.searchButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.searchButton)

        self.msgButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.msgButton)
        self.msgButton.setObjectName(u"msgButton")
        sizePolicy1.setHeightForWidth(self.msgButton.sizePolicy().hasHeightForWidth())
        self.msgButton.setSizePolicy(sizePolicy1)
        self.msgButton.setMinimumSize(QSize(150, 40))
        self.msgButton.setFocusPolicy(Qt.NoFocus)
        self.msgButton.setIcon(icon)
        self.msgButton.setIconSize(QSize(32, 32))
        self.msgButton.setCheckable(True)
        self.msgButton.setPopupMode(QToolButton.DelayedPopup)
        self.msgButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.msgButton.setArrowType(Qt.NoArrow)

        self.verticalLayout_3.addWidget(self.msgButton)

        self.categoryButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.categoryButton)
        self.categoryButton.setObjectName(u"categoryButton")
        sizePolicy1.setHeightForWidth(self.categoryButton.sizePolicy().hasHeightForWidth())
        self.categoryButton.setSizePolicy(sizePolicy1)
        self.categoryButton.setMinimumSize(QSize(150, 40))
        self.categoryButton.setFocusPolicy(Qt.NoFocus)
        self.categoryButton.setIcon(icon)
        self.categoryButton.setIconSize(QSize(32, 32))
        self.categoryButton.setCheckable(True)
        self.categoryButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.categoryButton)

        self.rankButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.rankButton)
        self.rankButton.setObjectName(u"rankButton")
        sizePolicy1.setHeightForWidth(self.rankButton.sizePolicy().hasHeightForWidth())
        self.rankButton.setSizePolicy(sizePolicy1)
        self.rankButton.setMinimumSize(QSize(150, 40))
        self.rankButton.setFocusPolicy(Qt.NoFocus)
        self.rankButton.setIcon(icon)
        self.rankButton.setIconSize(QSize(32, 32))
        self.rankButton.setCheckable(True)
        self.rankButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.rankButton)

        self.chatButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.chatButton)
        self.chatButton.setObjectName(u"chatButton")
        sizePolicy1.setHeightForWidth(self.chatButton.sizePolicy().hasHeightForWidth())
        self.chatButton.setSizePolicy(sizePolicy1)
        self.chatButton.setMinimumSize(QSize(150, 40))
        self.chatButton.setFocusPolicy(Qt.NoFocus)
        self.chatButton.setIcon(icon)
        self.chatButton.setIconSize(QSize(32, 32))
        self.chatButton.setCheckable(True)
        self.chatButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.chatButton)

        self.gameButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.gameButton)
        self.gameButton.setObjectName(u"gameButton")
        sizePolicy1.setHeightForWidth(self.gameButton.sizePolicy().hasHeightForWidth())
        self.gameButton.setSizePolicy(sizePolicy1)
        self.gameButton.setMinimumSize(QSize(150, 40))
        self.gameButton.setFocusPolicy(Qt.NoFocus)
        self.gameButton.setIcon(icon)
        self.gameButton.setIconSize(QSize(32, 32))
        self.gameButton.setCheckable(True)
        self.gameButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.gameButton)

        self.line_2 = QFrame(self.scrollAreaWidgetContents)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.label_3 = QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.downloadButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.downloadButton)
        self.downloadButton.setObjectName(u"downloadButton")
        sizePolicy1.setHeightForWidth(self.downloadButton.sizePolicy().hasHeightForWidth())
        self.downloadButton.setSizePolicy(sizePolicy1)
        self.downloadButton.setMinimumSize(QSize(150, 40))
        self.downloadButton.setFocusPolicy(Qt.NoFocus)
        self.downloadButton.setIcon(icon)
        self.downloadButton.setIconSize(QSize(32, 32))
        self.downloadButton.setCheckable(True)
        self.downloadButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.downloadButton)

        self.waifu2xButton = QToolButton(self.scrollAreaWidgetContents)
        self.buttonGroup.addButton(self.waifu2xButton)
        self.waifu2xButton.setObjectName(u"waifu2xButton")
        sizePolicy1.setHeightForWidth(self.waifu2xButton.sizePolicy().hasHeightForWidth())
        self.waifu2xButton.setSizePolicy(sizePolicy1)
        self.waifu2xButton.setMinimumSize(QSize(150, 40))
        self.waifu2xButton.setFocusPolicy(Qt.NoFocus)
        self.waifu2xButton.setIcon(icon)
        self.waifu2xButton.setIconSize(QSize(32, 32))
        self.waifu2xButton.setCheckable(True)
        self.waifu2xButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.waifu2xButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.helpButton = QToolButton(self.widget)
        self.buttonGroup.addButton(self.helpButton)
        self.helpButton.setObjectName(u"helpButton")
        sizePolicy1.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy1)
        self.helpButton.setMinimumSize(QSize(0, 40))
        self.helpButton.setFocusPolicy(Qt.NoFocus)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QSize(32, 32))
        self.helpButton.setCheckable(True)
        self.helpButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout.addWidget(self.helpButton)

        self.settingButton = QToolButton(self.widget)
        self.buttonGroup.addButton(self.settingButton)
        self.settingButton.setObjectName(u"settingButton")
        sizePolicy1.setHeightForWidth(self.settingButton.sizePolicy().hasHeightForWidth())
        self.settingButton.setSizePolicy(sizePolicy1)
        self.settingButton.setMinimumSize(QSize(150, 40))
        self.settingButton.setFocusPolicy(Qt.NoFocus)
        self.settingButton.setStyleSheet(u"")
        self.settingButton.setIcon(icon)
        self.settingButton.setIconSize(QSize(32, 32))
        self.settingButton.setCheckable(True)
        self.settingButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.settingButton.setAutoRaise(False)

        self.verticalLayout.addWidget(self.settingButton)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(Navigation)

        QMetaObject.connectSlotsByName(Navigation)
    # setupUi

    def retranslateUi(self, Navigation):
        Navigation.setWindowTitle(QCoreApplication.translate("Navigation", u"\u5bfc\u822a", None))
        self.picLabel.setText("")
        self.loginButton.setText(QCoreApplication.translate("Navigation", u"\u767b\u5f55", None))
        self.signButton.setText(QCoreApplication.translate("Navigation", u"\u6253\u5361", None))
        self.nameLabel.setText("")
        self.titleLabel.setText("")
        self.expLabel.setText("")
        self.levelLabel.setText("")
        self.label.setText(QCoreApplication.translate("Navigation", u"\u7528\u6237", None))
        self.collectButton.setText(QCoreApplication.translate("Navigation", u"\u6211\u7684\u6536\u85cf", None))
        self.myCommentButton.setText(QCoreApplication.translate("Navigation", u"\u6211\u7684\u8bc4\u8bba", None))
        self.lookButton.setText(QCoreApplication.translate("Navigation", u"\u89c2\u770b\u8bb0\u5f55", None))
        self.label_2.setText(QCoreApplication.translate("Navigation", u"\u5bfc\u822a", None))
        self.indexButton.setText(QCoreApplication.translate("Navigation", u"\u9996\u9875", None))
        self.searchButton.setText(QCoreApplication.translate("Navigation", u"\u641c\u7d22", None))
        self.msgButton.setText(QCoreApplication.translate("Navigation", u"\u7559\u8a00\u677f", None))
        self.categoryButton.setText(QCoreApplication.translate("Navigation", u"\u5206\u7c7b", None))
        self.rankButton.setText(QCoreApplication.translate("Navigation", u"\u6392\u884c\u699c", None))
        self.chatButton.setText(QCoreApplication.translate("Navigation", u"\u804a\u5929\u5ba4", None))
        self.gameButton.setText(QCoreApplication.translate("Navigation", u"\u6e38\u620f\u533a", None))
        self.label_3.setText(QCoreApplication.translate("Navigation", u"\u5176\u4ed6", None))
        self.downloadButton.setText(QCoreApplication.translate("Navigation", u"\u4e0b\u8f7d", None))
        self.waifu2xButton.setText(QCoreApplication.translate("Navigation", u"Waifu2x", None))
        self.helpButton.setText(QCoreApplication.translate("Navigation", u"\u5e2e\u52a9", None))
        self.settingButton.setText(QCoreApplication.translate("Navigation", u"\u8bbe\u7f6e", None))
    # retranslateUi

