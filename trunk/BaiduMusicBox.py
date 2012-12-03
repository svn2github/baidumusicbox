# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaiduMusicBox.ui'
#
# Created: Sat Nov 24 15:42:28 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BaiduMusicBox(object):
    def setupUi(self, BaiduMusicBox):
        BaiduMusicBox.setObjectName(_fromUtf8("BaiduMusicBox"))
        BaiduMusicBox.resize(849, 607)
        self.centralwidget = QtGui.QWidget(BaiduMusicBox)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 801, 541))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.keywordEdit = QtGui.QLineEdit(self.layoutWidget)
        self.keywordEdit.setObjectName(_fromUtf8("keywordEdit"))
        self.horizontalLayout.addWidget(self.keywordEdit)
        self.searchButton = QtGui.QPushButton(self.layoutWidget)
        self.searchButton.setObjectName(_fromUtf8("searchButton"))
        self.downloadButton = QtGui.QPushButton(self.layoutWidget)
        self.downloadButton.setObjectName(_fromUtf8("downloadButton"))

        self.horizontalLayout.addWidget(self.searchButton)
        self.horizontalLayout.addWidget(self.downloadButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtGui.QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        # TabPosition:
        # QTabWidget.North: 0
        # QTabWidget.South: 1
        # QTabWidget.West:  2
        # QTabWidget.East:  3
        self.tabWidget.setTabPosition(QtGui.QTabWidget.West)
        self.musicTab = QtGui.QWidget()
        self.musicTab.setObjectName(_fromUtf8("musicTab"))

        self.musicScrollArea = QtGui.QScrollArea(self.musicTab)
        self.musicScrollArea.setGeometry(QtCore.QRect(0, 0, 781, 431))
        self.musicScrollArea.setMinimumSize(QtCore.QSize(780,420))
        self.musicScrollArea.setWidgetResizable(True)
        self.musicTreeWidget = QtGui.QTreeWidget()
        self.musicTreeWidget.setObjectName(_fromUtf8("musicTreeWidget"))
        self.musicScrollArea.setWidget(self.musicTreeWidget)
        self.tabWidget.addTab(self.musicTab, _fromUtf8("音乐"))

        self.prevButton = QtGui.QPushButton("P&rev",self.tabWidget)
        self.prevButton.setGeometry(QtCore.QRect(30,440,60,30))
        self.prevButton.setObjectName(_fromUtf8("Prev"))

        self.playButton = QtGui.QPushButton("&Play",self.tabWidget)
        self.playButton.setGeometry(QtCore.QRect(100,440,60,30))
        self.playButton.setObjectName(_fromUtf8("Play"))

        self.pauseButton = QtGui.QPushButton("Pa&use",self.tabWidget)
        self.pauseButton.setGeometry(QtCore.QRect(170,440,60,30))
        self.pauseButton.setObjectName(_fromUtf8("Pause"))
        self.pauseButton.setEnabled(False)

        self.stopButton = QtGui.QPushButton("S&top",self.tabWidget)
        self.stopButton.setGeometry(QtCore.QRect(240,440,60,30))
        self.stopButton.setObjectName(_fromUtf8("Stop"))
        self.stopButton.setEnabled(False)

        self.nextButton = QtGui.QPushButton("&Next",self.tabWidget)
        self.nextButton.setGeometry(QtCore.QRect(310,440,60,30))
        self.nextButton.setObjectName(_fromUtf8("Next"))

        self.seekSlider = Phonon.SeekSlider(self.tabWidget)
        self.seekSlider.setGeometry(QtCore.QRect(410,445,360,20))

        self.musicLabel = QtGui.QLabel(self.tabWidget)
        self.musicLabel.setGeometry(QtCore.QRect(535,470,280,25))

        self.volumeSlider = Phonon.VolumeSlider(self.tabWidget)
        self.volumeSlider.setGeometry(QtCore.QRect(50,480,240,20))
        self.volumeSlider.setOrientation(1) # 0: vertical 1: horizontal

        self.closeButton = QtGui.QPushButton(self.tabWidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.closeButton.setGeometry(QtCore.QRect(680, 475, 80, 30))

        self.infoTab = QtGui.QWidget()
        self.infoTab.setObjectName(_fromUtf8("infoTab"))
        self.infoTreeWidget = QtGui.QTreeWidget(self.infoTab)
        self.infoTreeWidget.setGeometry(QtCore.QRect(0, 0, 781, 431))
        self.infoTreeWidget.setObjectName(_fromUtf8("infoTreeWidget"))
        self.tabWidget.addTab(self.infoTab, _fromUtf8("搜索"))

        self.downloadTab = QtGui.QWidget()
        self.downloadTab.setObjectName(_fromUtf8("downloadTab"))
        self.downloadTreeWidget = QtGui.QTreeWidget(self.downloadTab)
        self.downloadTreeWidget.setGeometry(QtCore.QRect(0, 0, 781, 431))
        self.downloadTreeWidget.setObjectName(_fromUtf8("downloadTreeWidget"))
        self.tabWidget.addTab(self.downloadTab, _fromUtf8("下载"))

        self.lyricTab = QtGui.QWidget()
        self.lyricTab.setObjectName(_fromUtf8("lyricTab"))
        self.lyricBrowser = QtGui.QTextBrowser(self.lyricTab)
        self.lyricBrowser.setGeometry(QtCore.QRect(20, 0, 760, 431))
        self.lyricBrowser.setAlignment(QtCore.Qt.AlignCenter)

        self.coverPixmap = QtGui.QPixmap()
        # scaled之后需要赋值回coverPixmap
        self.coverPixmap.load(os.getcwd() + os.sep + 'Download' + os.sep + 'Covers' + os.sep + 'Default.jpg')
        self.coverPixmap = self.coverPixmap.scaledToHeight(230)

        self.scene = QtGui.QGraphicsScene(self.lyricTab)
        self.scene.setObjectName(_fromUtf8("scene"))
        self.scene.addPixmap(self.coverPixmap)
        self.coverView = QtGui.QGraphicsView(self.lyricTab)
        self.coverView.setScene(self.scene)
        self.coverView.setGeometry(QtCore.QRect(400, 100, 300, 240))

        self.tabWidget.addTab(self.lyricTab, _fromUtf8("歌词"))

        self.verticalLayout.addWidget(self.tabWidget)

        BaiduMusicBox.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(BaiduMusicBox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 849, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.fileMenu = QtGui.QMenu(_fromUtf8("文件(&F)"),self.menubar)
        self.fileMenu.setObjectName(_fromUtf8("fileMenu"))

        self.settingsMenu = QtGui.QMenu(_fromUtf8("设置(&S)"), self.menubar)
        self.settingsMenu.setObjectName(_fromUtf8("settingsMenu"))

        BaiduMusicBox.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(BaiduMusicBox)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        BaiduMusicBox.setStatusBar(self.statusbar)

        self.importAction = QtGui.QAction(BaiduMusicBox)
        self.importAction.setObjectName(_fromUtf8("importAction"))
        self.exitAction = QtGui.QAction(BaiduMusicBox)
        self.exitAction.setObjectName(_fromUtf8("exitAction"))
        self.fileMenu.addAction(self.importAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)
        self.menubar.addAction(self.fileMenu.menuAction())

        self.dirSettingsAction = QtGui.QAction(BaiduMusicBox)
        self.dirSettingsAction.setObjectName(_fromUtf8("dirSettingsAction"))

        # 播放模式
        # 一般模式(顺序循环)
        self.defaultModeAction = QtGui.QAction(BaiduMusicBox)
        self.defaultModeAction.setObjectName(_fromUtf8("defaultModeAction"))
        self.defaultModeAction.setCheckable(True)

        # 随机模式
        self.randomModeAction = QtGui.QAction(BaiduMusicBox)
        self.randomModeAction.setObjectName(_fromUtf8("randomModeAction"))
        self.randomModeAction.setCheckable(True)
        # 单曲模式
        self.singleModeAction = QtGui.QAction(BaiduMusicBox)
        self.singleModeAction.setObjectName(_fromUtf8("singleModeAction"))
        self.singleModeAction.setCheckable(True)

        self.modeMenu = QtGui.QMenu(self.settingsMenu)
        self.modeMenu.setObjectName(_fromUtf8("modeMenu"))

        self.modeMenu.addSeparator()
        self.modeMenu.addAction(self.defaultModeAction)
        self.modeMenu.addSeparator()
        self.modeMenu.addAction(self.randomModeAction)
        self.modeMenu.addAction(self.singleModeAction)

        self.settingsMenu.addAction(self.dirSettingsAction)
        self.settingsMenu.addSeparator()
        self.settingsMenu.addAction(self.modeMenu.menuAction())
        self.menubar.addAction(self.settingsMenu.menuAction())

        self.viewMenu = QtGui.QMenu(_fromUtf8("视图(&V)"), self.menubar)
        self.viewMenu.setObjectName(_fromUtf8("viewMenu"))
        self.menubar.addAction(self.viewMenu.menuAction())
        
        self.musicViewAction = QtGui.QAction(BaiduMusicBox)
        self.musicViewAction.setObjectName(_fromUtf8("musicViewAction"))
        self.musicViewAction.setCheckable(True)
        self.musicViewAction.setChecked(True)
        self.musicViewAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "音乐视图", None, QtGui.QApplication.UnicodeUTF8))

        self.infoViewAction = QtGui.QAction(BaiduMusicBox)
        self.infoViewAction.setObjectName(_fromUtf8("infoViewAction"))
        self.infoViewAction.setCheckable(True)
        self.infoViewAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "搜索视图", None, QtGui.QApplication.UnicodeUTF8))

        self.downViewAction = QtGui.QAction(BaiduMusicBox)
        self.downViewAction.setObjectName(_fromUtf8("downViewAction"))
        self.downViewAction.setCheckable(True)
        self.downViewAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "下载视图", None, QtGui.QApplication.UnicodeUTF8))

        self.lyricViewAction = QtGui.QAction(BaiduMusicBox)
        self.lyricViewAction.setObjectName(_fromUtf8("lyricViewAction"))
        self.lyricViewAction.setCheckable(True)
        self.lyricViewAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "歌词视图", None, QtGui.QApplication.UnicodeUTF8))

        self.viewMenu.addAction(self.musicViewAction)
        self.viewMenu.addAction(self.infoViewAction)
        self.viewMenu.addAction(self.downViewAction)
        self.viewMenu.addAction(self.lyricViewAction)

        self.aboutAction = QtGui.QAction(BaiduMusicBox)
        self.aboutAction.setObjectName(_fromUtf8("aboutAction"))
        self.aboutAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "关于", None, QtGui.QApplication.UnicodeUTF8))

        self.aboutQtAction = QtGui.QAction(BaiduMusicBox)
        self.aboutQtAction.setObjectName(_fromUtf8("aboutQtAction"))
        self.aboutQtAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "关于Qt", None, QtGui.QApplication.UnicodeUTF8))
        
        self.aboutMenu = QtGui.QMenu(_fromUtf8("关于(&A)"), self.menubar)
        self.aboutMenu.setObjectName(_fromUtf8("aboutMenu"))
#        self.aboutMenu.setTitle(QtGui.QApplication.translate("BaiduMusicBox", "关于", None, QtGui.QApplication.UnicodeUTF8))
        self.menubar.addAction(self.aboutMenu.menuAction())

        self.aboutMenu.addAction(self.aboutAction)
        self.aboutMenu.addAction(self.aboutQtAction)

        self.retranslateUi(BaiduMusicBox)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BaiduMusicBox.close)
        QtCore.QObject.connect(self.exitAction, QtCore.SIGNAL(_fromUtf8("triggered()")), BaiduMusicBox.close)
        QtCore.QMetaObject.connectSlotsByName(BaiduMusicBox)

    def retranslateUi(self, BaiduMusicBox):
        BaiduMusicBox.setWindowTitle(QtGui.QApplication.translate("BaiduMusicBox", "百度音乐盒", None, QtGui.QApplication.UnicodeUTF8))
        self.keywordEdit.setToolTip(QtGui.QApplication.translate("BaiduMusicBox", "<html><head/><body><p>建议搜索关键字：</p><p>“歌曲”</p><p>“歌曲 演唱者”</p><p>“演唱者”</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("BaiduMusicBox", "搜索", None, QtGui.QApplication.UnicodeUTF8))
        self.musicTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("BaiduMusicBox", "序号", None, QtGui.QApplication.UnicodeUTF8))
        self.musicTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("BaiduMusicBox", "歌曲", None, QtGui.QApplication.UnicodeUTF8))
        self.musicTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("BaiduMusicBox", "演唱者", None, QtGui.QApplication.UnicodeUTF8))
        self.musicTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("BaiduMusicBox", "来自专辑", None, QtGui.QApplication.UnicodeUTF8))

        self.infoTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("BaiduMusicBox", "序号", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("BaiduMusicBox", "歌曲", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("BaiduMusicBox", "演唱者", None, QtGui.QApplication.UnicodeUTF8))
        self.infoTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("BaiduMusicBox", "来自专辑", None, QtGui.QApplication.UnicodeUTF8))

        self.downloadTreeWidget.headerItem().setText(0, QtGui.QApplication.translate("BaiduMusicBox", "任务序号", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(1, QtGui.QApplication.translate("BaiduMusicBox", "文件名称", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(2, QtGui.QApplication.translate("BaiduMusicBox", "下载目录", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(3, QtGui.QApplication.translate("BaiduMusicBox", "文件大小", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(4, QtGui.QApplication.translate("BaiduMusicBox", "已用时间", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(5, QtGui.QApplication.translate("BaiduMusicBox", "剩余时间", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadTreeWidget.headerItem().setText(6, QtGui.QApplication.translate("BaiduMusicBox", "下载进度", None, QtGui.QApplication.UnicodeUTF8))

        self.downloadButton.setText(QtGui.QApplication.translate("BaiduMusicBox", "下载", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("BaiduMusicBox", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.importAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "导入", None, QtGui.QApplication.UnicodeUTF8))
        self.dirSettingsAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "目录设置", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.modeMenu.setTitle(QtGui.QApplication.translate("BaiduMusicBox", "播放模式", None, QtGui.QApplication.UnicodeUTF8))
        self.defaultModeAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "顺序循环", None, QtGui.QApplication.UnicodeUTF8))
        self.randomModeAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "随机播放", None, QtGui.QApplication.UnicodeUTF8))
        self.singleModeAction.setText(QtGui.QApplication.translate("BaiduMusicBox", "单曲循环", None, QtGui.QApplication.UnicodeUTF8))
