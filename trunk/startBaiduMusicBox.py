# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.phonon import Phonon

from BaiduMusicBox import Ui_BaiduMusicBox
from aboutDialog import Ui_aboutDialog
from dirSettingsDialog import Ui_dirSettingsDialog

import baiduMusic

import sys,os,time
reload(sys)
sys.setdefaultencoding('utf8')

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_BaiduMusicBox()
        self.ui.setupUi(self)

        # 读取配置文件 并初始化相关设置
        self.rcfile = os.getcwd() + os.sep + 'BaiduMusicBox.rc_' + os.name
        self.readConfig()
        self.settingsInit()

        # 用于标示lrc状态
        self.lrcFlag = 1

        # 用于标示downloadTreeWidgetItem的序号
        self.seq = 0

        # 用于存放选择下载的项目序号
        self.indexList = []

        # 相关信息初始化
        self.suffix = []
        self.title = []
        self.artist = []

        self.mp3filenames = []
        
        # mp3对象
        self.m_media = Phonon.MediaObject(self)
        self.m_media.setTickInterval(1000) # 设置tickInterval为1000ms，默认是0

        self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory,self)
        Phonon.createPath(self.m_media, self.audioOutput)

        self.m_media.aboutToFinish.connect(self.musicEnqueue)
        self.m_media.currentSourceChanged.connect(self.musicActionPlay)
        self.m_media.stateChanged.connect(self.musicStateChanged)
        self.m_media.tick.connect(self.musicTick)

        self.ui.seekSlider.setMediaObject(self.m_media)
        self.ui.volumeSlider.setAudioOutput(self.audioOutput)

        # 播放列表

        self.playlistfile = os.getcwd() + os.sep + 'playlist_' + os.name
        self.playlist = []
        self.readPlaylist()

        # 信号绑定：
        self.ui.searchButton.clicked.connect(self.searchFunc)
        self.ui.downloadButton.clicked.connect(self.downloadFunc)

        self.ui.keywordEdit.returnPressed.connect(self.searchFunc) 
        self.ui.keywordEdit.textChanged.connect(self.enableButton)
        self.ui.infoTreeWidget.itemDoubleClicked.connect(self.doubleClickSlot)
        self.ui.musicTreeWidget.itemDoubleClicked.connect(self.setMediaSource)
        
        self.ui.importAction.triggered.connect(self.importMusic)
        self.ui.dirSettingsAction.triggered.connect(self.dirSettingsFunc)

        self.ui.aboutAction.triggered.connect(self.aboutFunc)
        self.ui.aboutQtAction.triggered.connect(self.aboutQtFunc)

        # 每次点击infoTreeWidget调用一次checkAll,有待改进.
        self.ui.infoTreeWidget.clicked.connect(self.checkAll)

        self.ui.playButton.clicked.connect(self.musicActionPlay)
        self.ui.pauseButton.clicked.connect(self.musicActionPause)
        self.ui.stopButton.clicked.connect(self.musicActionStop)
        self.ui.prevButton.clicked.connect(self.musicActionPrev)
        self.ui.nextButton.clicked.connect(self.musicActionNext)

        self.ui.defaultModeAction.triggered.connect(self.setDefaultMode)
        self.ui.randomModeAction.triggered.connect(self.setRandomMode)
        self.ui.singleModeAction.triggered.connect(self.setSingleMode)

        self.ui.musicViewAction.triggered.connect(self.setMusicView)
        self.ui.infoViewAction.triggered.connect(self.setInfoView)
        self.ui.downViewAction.triggered.connect(self.setDownView)
        self.ui.lyricViewAction.triggered.connect(self.setLyricView)
        # keywordEdit相关特性设置
        self.ui.keywordEdit.setDragEnabled(True)

        # infoTreeWidget外观设置
        self.ui.infoTreeWidget.setColumnWidth(0,80)
        self.ui.infoTreeWidget.setColumnWidth(1,200)
        self.ui.infoTreeWidget.setColumnWidth(2,160)

        self.ui.musicTreeWidget.setColumnWidth(0,80)
        self.ui.musicTreeWidget.setColumnWidth(1,160)
        self.ui.musicTreeWidget.setColumnWidth(2,200)

        # “搜索”、“下载”按钮默认禁用
        self.ui.searchButton.setEnabled(False)
        self.ui.downloadButton.setEnabled(False)

        # 生成20个QTreeWidgetItem
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)
        item_0 =  QtGui.QTreeWidgetItem(self.ui.downloadTreeWidget)

    def readConfig(self):
        """Read config file when started."""
        self.mp3Location = ''
        self.lrcLocation = ''
        self.playMode = 0

        if os.path.exists(self.rcfile):
            f = open(self.rcfile)
            lines = f.readlines()
            f.close()
            for line in lines:
                # 过滤注释行
                if line.startswith('#'):
                    continue
                if line.find('mp3Location') != -1:
                    self.mp3Location = str(line.split('=')[1]).replace('\n','').decode('utf-8')
                    continue
                elif line.find('lrcLocation') != -1:
                    self.lrcLocation = str(line.split('=')[1]).replace('\n','').decode('utf-8')
                    continue
                elif line.find('playMode') != -1:
                    self.playMode = int(str(line.split('=')[1]).replace('\n',''))
            del lines

        if not self.mp3Location:
            self.mp3Location = os.getcwd() + os.sep + 'Download'

        if not self.lrcLocation:
            self.lrcLocation = self.mp3Location + os.sep + 'lyrics'

    def writeConfig(self):
        """Write options to default config file."""
        if os.path.exists(self.rcfile):
            f = open(self.rcfile)
            lines = f.readlines()
            f.close()
        else:
            lines = []
        newConfig = []
        if lines:
            for line in lines:
                # 过滤注释行
                if line.find('mp3Location') != -1:
                    line = str('mp3Location=' + self.mp3Location).decode('utf-8')
                elif line.find('lrcLocation') != -1:
                    line = str('lrcLocation=' + self.lrcLocation).decode('utf-8')
                elif line.find('playMode') != -1:
                    line = str('playMode=' + str(self.playMode)).decode('utf-8')
                if line:
                    newConfig.append(line)

            newConfig = '\n'.join(newConfig)

        else:
            newConfig = str('mp3Location=' + self.mp3Location + '\n'
                    + 'lrcLocation=' + self.lrcLocation + '\n'
                    + 'playMode=' + str(self.playMode)).decode('utf-8')
        f = open(self.rcfile,'w') 
        f.write(newConfig)
        f.close()
        del newConfig,lines

    def settingsInit(self):
        """Initiate corresponding UI settings."""
        if self.playMode == 0:
            self.ui.defaultModeAction.setChecked(True)
        elif self.playMode == 1:
            self.ui.randomModeAction.setChecked(True)
        elif self.playMode == 2:
            self.ui.singleModeAction.setChecked(True)

    def aboutFunc(self):
        """Pop aboutDialog when called."""
        self.aboutDialog = aboutDialog(self)
        self.aboutDialog.show()
#        QtGui.QMessageBox.about(self,'PyQt','BaiduMusicBox(百度音乐盒)\n lwldcr@gmail.com'.decode('utf-8'))

    def aboutQtFunc(self):
        """Pop about Qt MessageBox."""
        QtGui.QMessageBox.aboutQt(self,'PyQt')


    def dirSettingsFunc(self):
        """Pop dirSettingsDialog when called."""

        self.dirSettingsDialog = dirSettingsDialog(self)

        self.dirSettingsDialog.mp3Location = self.mp3Location
        self.dirSettingsDialog.lrcLocation = self.lrcLocation
        self.dirSettingsDialog.ui.mp3LocationEdit.setText(self.mp3Location)
        self.dirSettingsDialog.ui.lrcLocationEdit.setText(self.lrcLocation)

        self.dirSettingsDialog.exec_()  # 使用exec_()会出现“段错误”
#        self.dirSettingsDialog.show() # 使用show()不能改变相关变量
        
        # 如果在dirSettingsDialog中的改变做了确认，则更新相关信息
        if self.dirSettingsDialog.result() == 1:
            self.mp3Location = self.dirSettingsDialog.mp3Location
            self.lrcLocation = self.dirSettingsDialog.lrcLocation
            self.writeConfig()
        else:
            return

    def contextMenuEvent(self,event):
        """Pop menu when right button clicked."""
        # 鼠标右键菜单
        

        musicMenu = QtGui.QMenu(self)
        downloadAction = musicMenu.addAction(u"下载".decode('utf-8'))
        # currentPos = QtGui.QCursor.pos()

        # 如果鼠标指针位置处是infoTreeWidget的一个item，则弹出菜单.
        # 此处貌似不判断是哪个treeWidget?? 通过tabWidget.currentIndex判断当前处在哪个tab.
        if self.ui.infoTreeWidget.itemAt(event.pos()) and self.ui.tabWidget.currentIndex() == 0:
        ##    action = musicMenu.exec_(self.mapToGlobal(event.pos()))
            #action = musicMenu.exec_(QtGui.QCursor.pos())
        ##    if action == downloadAction:
        ##        self.downloadFunc()
            pass
        elif self.ui.downloadTreeWidget.itemAt(event.pos()):
            pass
        
    def enableButton(self):
        """Enable searchButton when called."""
        self.ui.searchButton.setEnabled(True)
                       
    def popMessage(self,title,text):
        """Used to pop different messages according to parameters given."""
        OK = '确定'.decode('utf-8')
        message = QtGui.QMessageBox(self)
        message.setText(text.decode('utf-8'))
        message.setWindowTitle(title.decode('utf-8'))
        message.addButton(OK,QtGui.QMessageBox.AcceptRole)
        message.exec_()

        response = message.clickedButton().text()
        if response == OK:
            return 1


    def generateText(self,filename,filestatus):
        """Generate text according to given argument and return."""
        if filename:
            filetitle = u"下载成功"
            if filestatus == 10:
                filetext = u"已经存在"
            elif filestatus == 20:
                filetext = u"下载成功"
            else:
                filetext = u"下载失败"
        else:
            filetitle = u"下载失败"
            filetext = u"文件不存在"
        filetext = str(filename + filetext)

        return filetitle,filetext

    
    def searchFunc(self):
        """Search keywords input by user and display search results."""
        keywords = str(self.ui.keywordEdit.text()) # 若不做str转换，默认是Qstring对象，不可使用split()等方法
        if keywords:
            self.ui.searchButton.setEnabled(True)

        if not keywords:
            title = '悟空'
            text = '你又顽皮了'
            self.popMessage(title,text)
            return
        
        listUrl = baiduMusic.generateUrl(keywords)
        if listUrl:
            result = baiduMusic.generateList(listUrl)
            try:
                # 有搜索结果
                seq,suffix,title,artist,album = result
            except TypeError:
                # 无网络连接时，自动退出程序
                if str(result).isdigit():
                    if result == 10:
                        title = '网络错误'
                        text = '无法访问互联网，请检查网络连接'
                        res = self.popMessage(title,text)
                        if res == 1:
                            self.close()
                        return

                # 网络通畅时，根据返回值做不同处理
                # 没有搜到结果
                    elif result == 20:
                        title = '没有搜索结果'
                        text = '没有找到匹配结果，请修改关键词重试'
                        res = self.popMessage(title,text)
                        if res == 1:
                            self.ui.keywordEdit.setFocus()
                            self.ui.keywordEdit.selectAll()
                        return
            
            self.ui.infoTreeWidget.clear()
            # 切换到显示搜索结果的tab
            self.ui.tabWidget.setCurrentIndex(1)

            i = 0
            for  i in xrange(0,15):
                a = QtGui.QTreeWidgetItem(self.ui.infoTreeWidget)
                try:
                    a.setText(0,seq[i].decode('utf-8'))
                    a.setText(1,title[i].decode('utf-8'))
                    a.setText(2,artist[i].decode('utf-8'))
                    a.setText(3,album[i].decode('utf-8'))

                    # 设置checkbox
                    #a.setFlags(a.flags() & ~QtCore.Qt.ItemIsUserCheckable)
                    a.setCheckState(0,QtCore.Qt.Unchecked)
                except:
                    a.setText(0,'')
                    a.setText(1,'')
                    a.setText(2,'')
                    a.setText(3,'')

            a = QtGui.QTreeWidgetItem(self.ui.infoTreeWidget)
            a.setText(1,'全选'.decode('utf-8'))
            a.setCheckState(0,QtCore.Qt.Unchecked)

            self.suffix = suffix
            self.title = title
            self.artist = artist

        if self.suffix:
            self.ui.downloadButton.setEnabled(True)

    def reportHook(self,blocks_read,block_size,total_size,seq):
        """Display downloading progress."""
        if not blocks_read:
            print ("Connection opened from PyQt.")
        if total_size < 0:
            print "Read %d blocks" % blocks_read
        else:
            percentage =  blocks_read*block_size * 100.0 / total_size
            totalsize = total_size/(1024.0 * 1024.0)
            text = "已完成: %.2f %%" % percentage

            self.ui.downloadTreeWidget.topLevelItem(seq-1).setText(0,str(seq).decode('utf-8'))
            self.ui.downloadTreeWidget.topLevelItem(seq-1).setText(1,str(self.mp3filenames[seq-1]).decode('utf-8'))
            self.ui.downloadTreeWidget.topLevelItem(seq-1).setText(2,str(self.mp3Location).decode('utf-8'))
            self.ui.downloadTreeWidget.topLevelItem(seq-1).setText(3,str('%.2f MB' % totalsize).decode('utf-8'))
            self.ui.downloadTreeWidget.topLevelItem(seq-1).setText(6,str(text).decode('utf-8'))

            time.sleep(1)

    def checkAll(self):
        """Change all items' checkstat when 全选 checkbox changes."""
        # 0: QtCore.Qt.Unchecked
        # 1: 方块选中
        # 2: QtCore.Qt.Checked
        num = self.ui.infoTreeWidget.indexOfTopLevelItem(self.ui.infoTreeWidget.currentItem())
        if num == 15:
            if self.ui.infoTreeWidget.topLevelItem(15).checkState(0) == 2:
                state = 2
            else:
                state = 0
        else:
            return

        i = 0
        for i in xrange(0,15):
            if self.ui.infoTreeWidget.topLevelItem(i).text(0):
                self.ui.infoTreeWidget.topLevelItem(i).setCheckState(0,state)

    def downloadFunc(self):
        """Download mp3 and lrc files."""

        it = QtGui.QTreeWidgetItemIterator(self.ui.infoTreeWidget)
        temp = [] # 存放重复添加的任务
        while it:
            try:
                if it.value().checkState(0):
                    v = int(it.value().text(0))-1
                    if v not in self.indexList:
                        # 任务不存在
                        if len(self.indexList) < 20:
                            self.indexList.append(v)
                        else:
                            self.popMessage("任务太多","任务数超过20，请稍后再添加!")
                            break
                    else:
                        # 任务已经存在
                        self.indexList.remove(v)
                        temp.append(v)
                        self.popMessage('任务已存在','"%s"已在下载列表中' % self.title[v])
                it += 1
            except:
                break
        
        # 执行选中的下载任务
        for i in self.indexList:
            self.downloadFile(i)
            time.sleep(0.1)

        for e in temp: # 将重复添加的任务和新近添加的任务序号合并，代表所有正在运行的任务序号列表.
            self.indexList.append(e)

    def doubleClickSlot(self):
        """Called when infoTreeWidgetItem doubleClicked."""
        num = self.ui.infoTreeWidget.indexOfTopLevelItem(self.ui.infoTreeWidget.currentItem())
        if num == 15:
            return

        if num not in self.indexList:
            self.indexList.append(num)
            self.downloadFile(num)

    def downloadFile(self,i):
        """Implementation of downloadin function."""
        # 切换到显示搜索结果的tab
        self.ui.tabWidget.setCurrentIndex(2)

        # 获取downloadThread的序号
        self.seq += 1

        name = self.title[i] + '-' + self.artist[i] + '.mp3'
        self.mp3filenames.append(name) 

        self.data = ('http://music.baidu.com' + self.suffix[i],self.title[i],self.artist[i])
        self.thread = downloadThread(self,(self.data[0],self.data[1],self.data[2],self.mp3Location,self.lrcLocation,self.reportHook,self.seq))
        self.thread.finished.connect(self.downloadFinished)
        self.thread.start()
        
    def downloadFinished(self):
        mp3name,mp3status = self.thread.mp3name,self.thread.mp3status
        lrcname,lrcstatus = self.thread.lrcname,self.thread.lrcstatus
        
        mp3title,mp3text = self.generateText(mp3name,mp3status)

        # 如果已经存在，那么显示下载信息的item序号减1，以免显示空行
        if mp3status == 10:
            self.seq -= 1

        lrctitle,lrctext = self.generateText(lrcname,lrcstatus)
        text = mp3text + '\n' + lrctext

        if mp3title == lrctitle and mp3title == u"下载成功":
            title = mp3title
        else:
            title = u"下载失败"

        res = self.popMessage(title,text)
        if res == 1:
            self.ui.keywordEdit.setFocus()
            self.ui.keywordEdit.selectAll()
            return

    def formatTime(self,time):
        """Format integer miliseconds into MM:SS type."""
        if time:
            secs = int(time/1000%60)
            mins = int(time/1000/60)
            if 0 <= mins < 10:
                mins = '0' + str(mins)
            if 0 <= secs< 10:
                secs = '0' + str(secs)
            return str(mins) + ':' + str(secs)
        else:
            return '00:00'

    def musicTick(self):
        """Show current time of music."""
        text = self.formatTime(self.m_media.currentTime()) + "/" + self.formatTime(self.m_media.totalTime())
        self.ui.musicLabel.setText(text)
        self.showLyric()

    def musicActionPlay(self):
        """Start play music."""
        # 重置lrcFlag
        self.lrcFlag = 1
        # 如果没有currentSource().fileName()，那么先设置
        if not self.m_media.currentSource().fileName():
            self.setMediaSource()
            # 此处currentSourceChanged()信号，再次执行本函数
            # 信号stateChanged(),槽 self.musicStateChanged()
            return

        # 将当前播放曲目置为currentItem
        currentIndex = self.getCurrentSourceIndex() 
        self.ui.musicTreeWidget.setCurrentItem(self.ui.musicTreeWidget.topLevelItem(currentIndex))

        # 更新Cover Image
        self.showCover()

        # 若之前不是暂停状态，将lyricBrowser清空
        if self.m_media.state() != 4:
            self.ui.lyricBrowser.setText('')

        if self.m_media.state() == 2:
            return
        self.m_media.play()

    def musicActionPause(self):
        """Pause playing."""
        self.m_media.pause()

    def musicActionStop(self):
        """Pause playing."""
        self.m_media.stop()
    
    def musicActionPrev(self):
        """Play previous music file in playlist."""
        currentIndex = self.getCurrentSourceIndex()
        if self.playMode == 0:
            if currentIndex != 0:
                prevIndex = currentIndex - 1
            else:
                prevIndex = len(self.playlist) - 1
        elif self.playMode == 1:
            import random
            prevIndex = random.randint(0,len(self.playlist)-1)
        else:
            prevIndex = currentIndex

        previousFile = self.playlist[prevIndex]
        self.m_media.setCurrentSource(Phonon.MediaSource(previousFile))

    def musicActionNext(self):
        """Play next music file in playlist."""
        currentIndex = self.getCurrentSourceIndex() 
        if self.playMode == 0:
            if currentIndex != len(self.playlist) - 1:
                nextIndex = currentIndex + 1
            else:
                nextIndex = 0
        elif self.playMode == 1:
            import random
            nextIndex = random.randint(0,len(self.playlist))
        else:
            nextIndex = currentIndex

        nextFile = self.playlist[nextIndex]
        self.m_media.setCurrentSource(Phonon.MediaSource(nextFile))

    def musicStateChanged(self):
        """When music state changed,change playbutton text accordingly."""
        # Phonon.State:
        # Phonon.LoadingState:   0
        # Phonon.StoppedState:   1
        # Phonon.PlayingState:   2
        # Phonon.BufferingState: 3
        # Phonon.PausedState:    4
        # Phonon.ErrorState:     5

        currentState = self.m_media.state()
        if currentState == 2:
            self.ui.pauseButton.setEnabled(True)
            self.ui.stopButton.setEnabled(True)
            self.ui.playButton.setEnabled(False)
        elif currentState == 4:
            self.ui.pauseButton.setEnabled(False)
            self.ui.playButton.setEnabled(True)
        elif currentState == 1:
            self.ui.stopButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(False)
            self.ui.playButton.setEnabled(True)
        else:
            self.ui.playButton.setEnabled(True)
            self.ui.stopButton.setEnabled(False)
            self.ui.pauseButton.setEnabled(False)

    def getCurrentSourceIndex(self):
        """Get current playing music file index."""
        # self.m_media.currentSource().fileName()返回格式:
        # C:/xxx/xxx.mp3
        currentSourceFile = str(self.m_media.currentSource().fileName().split('/')[-1])

        for elem in self.playlist:
            if elem.find(currentSourceFile) != -1:
                indexOfCurrent = self.playlist.index(elem)
                break
        if not indexOfCurrent:
            indexOfCurrent = 0
        return indexOfCurrent

    def setMediaSource(self):
        """Set music source when called."""
        if not self.ui.musicTreeWidget.currentItem():
            self.ui.musicTreeWidget.setCurrentItem(self.ui.musicTreeWidget.topLevelItem(0))

        try:
            currentTitle = self.ui.musicTreeWidget.currentItem().text(1)
        except AttributeError:
            QtGui.QMessageBox.critical(self,'PyQt','当前列表为空！请先导入文件.'.decode('utf-8'))
            return

        f = open(self.playlistfile,'r+')
        for line in f:
            if line.find(currentTitle) != -1:
                filename = line.replace('\n','').decode('utf-8')
                break

        self.m_media.setCurrentSource(Phonon.MediaSource(filename))
    
    def musicEnqueue(self):
        """Control m_media object queue."""
        currentIndex = self.getCurrentSourceIndex() 
        if self.playMode == 0:
            if currentIndex != len(self.playlist) - 1:
                nextIndex = currentIndex + 1
            else:
                nextIndex = 0
        elif self.playMode == 1:
            import random
            nextIndex = random.randint(0,len(self.playlist))
        else:
            nextIndex = currentIndex

        nextFile = self.playlist[nextIndex]
        self.m_media.enqueue(Phonon.MediaSource(str(nextFile).decode('utf-8')))

    def getMusicInfo(self,filename,sep=''):
        """Get music information."""
        import id3reader

        if not sep:
            sep = self.systemSep()
            
        try:
            id3r = id3reader.Reader(str(filename).decode('utf-8'))
        except:
            id3r = ''

        # id3r.getValue(key)
        # Available keys:
        # album,performer,title,track,year
        if id3r:
	        title = id3r.getValue('title')
	        if not title:
	            title = filename.split(sep)[-1]
	        artist = id3r.getValue('performer')
	        album = id3r.getValue('album') 

        return title, artist, album

    def systemSep(self):
        """Return seperator according to system type."""
        if os.name == 'nt':
            sep = '\\'
        else:
            sep = '/'
        return sep

    def importMusic(self):
        """Import music files from local hard disk."""
        fd = QtGui.QFileDialog(self)
        # 添加filter，没效果？
        fd.setNameFilter("*.mp3")
        # FileMode:
        # QtGui.QFileDialog.AnyFile:       0
        # QtGui.QFileDialog.ExistingFile:  1
        # QtGui.QFileDialog.Directory:     2
        # QtGui.QFileDialog.ExistingFiles: 3
        fd.setFileMode(3)

        # Entering playlist
        if os.path.exists(self.playlistfile):
            f = open(self.playlistfile,'r+')
            f.seek(0,2)
        else:
            f = open(self.playlistfile,'w')

        len1 = len(self.playlist)
        for filename in fd.getOpenFileNames():
            filename = str(filename)
            self.playlist.append(filename)
            f.write('\n' + filename)
            
            a = QtGui.QTreeWidgetItem(self.ui.musicTreeWidget)
            (title,artist,album) = self.getMusicInfo(filename)
            a.setText(0,str(len(self.playlist)).decode('utf-8'))
            a.setText(1,str(title).decode('utf-8'))
            a.setText(2,str(artist).decode('utf-8'))
            a.setText(3,str(album).decode('utf-8'))

        f.close()

        # import成功后，弹出提示信息
        len2 = len(self.playlist)
        newAddedLength = len2 - len1
        if newAddedLength:
            QtGui.QMessageBox.information(self,'添加歌曲成功'.decode('utf-8'),
                    str('新增 %d 首音乐'%(newAddedLength)).decode('utf-8'))


   
    def displayPlaylist(self):
        """Display music list in music tab."""
        if not self.playlist:
            return

        i = 1
        for item in self.playlist:
            a = QtGui.QTreeWidgetItem(self.ui.musicTreeWidget)
            (title,artist,album) = self.getMusicInfo(item)
            a.setText(0,str(i).decode('utf-8'))
            a.setText(1,str(title).decode('utf-8'))
            a.setText(2,str(artist).decode('utf-8'))
            a.setText(3,str(album).decode('utf-8'))
             
            i += 1

    def readPlaylist(self):
        """Read playlist function."""
        if not os.path.exists(self.playlistfile):
            return
        else:
            f = open(self.playlistfile,'r')
            for line in f: 
                if line != '\n':
                    if os.path.exists(line.replace('\n','').decode('utf-8')):
                        self.playlist.append(line.replace('\n','').decode('utf-8'))
            f.close()
            self.displayPlaylist()

    def setDefaultMode(self):
        """Set default playing mode."""
        self.playMode = 0
        self.ui.defaultModeAction.setChecked(True)
        self.ui.randomModeAction.setChecked(False)
        self.ui.singleModeAction.setChecked(False)
        self.writeConfig()

    def setRandomMode(self):
        """Set random playing mode."""
        self.playMode = 1
        self.ui.defaultModeAction.setChecked(False)
        self.ui.randomModeAction.setChecked(True)
        self.ui.singleModeAction.setChecked(False)
        self.writeConfig()

    def setSingleMode(self):
        """Set single cycling mode."""
        self.playMode = 2
        self.ui.defaultModeAction.setChecked(False)
        self.ui.randomModeAction.setChecked(False)
        self.ui.singleModeAction.setChecked(True)
        self.writeConfig()

    def setMusicView(self):
        """Set musicView checked."""
        self.setView('music')

    def setInfoView(self):
        """Set infoView checked."""
        self.setView('info')

    def setDownView(self):
        """Set downView checked."""
        self.setView('download')

    def setLyricView(self):
        """Set lyricView checked."""
        self.setView('lyric')

    def setView(self,viewName):
        """Set current view."""
        flagDict = {}
        words = ['music','info','download','lyric']
        for word in words:
            if word == viewName:
                flagDict[word] = 1
            else:
                flagDict[word] = 0

        self.ui.tabWidget.setCurrentIndex(words.index(viewName))

        self.ui.musicViewAction.setChecked(flagDict['music'])
        self.ui.infoViewAction.setChecked(flagDict['info'])
        self.ui.downViewAction.setChecked(flagDict['download'])
        self.ui.lyricViewAction.setChecked(flagDict['lyric'])

    def showLyric(self):
        """Display lyric according to music been played."""
        currentIndex = self.getCurrentSourceIndex()
        currentFile = self.playlist[currentIndex]

        if not self.lrcFlag:
            return

        (title,artist,album) = self.getMusicInfo(currentFile)
        currentLrc = self.lrcLocation + os.sep + title + '-' + artist + '.lrc'
        if not os.path.exists(currentLrc):
            self.ui.lyricBrowser.append("歌词不存在".decode('utf-8'))
            keyword = title + ' ' + artist
            self.downloadLyric(keyword)

        # 下载失败，则返回
        if not os.path.exists(currentLrc):
            self.lrcFlag = 0
            return

        f = open(currentLrc)
        lines = f.readlines()
        f.close()

        timeTag = self.formatTime(self.m_media.currentTime())
        for line in lines:
            if line.find(timeTag) != -1:
                #self.ui.lyricBrowser.append(re.sub('\[.*?\]','',line.decode('utf-8')))
                self.ui.lyricBrowser.append(line.split(']')[-1].decode('utf-8'))
                # for linux and libvlc only
                #time.sleep(1)

    def showCover(self):
        """Show cover image."""
        currentIndex = self.getCurrentSourceIndex()
        currentFile = self.playlist[currentIndex]
        album = self.getMusicInfo(currentFile)[2]
        if not album:
            albumFullPath = os.getcwd() + os.sep + 'Download' + os.sep + 'Covers' + os.sep + 'Default' + '.jpg'
        else:
            self.coverLocation = self.mp3Location + os.sep + 'Covers'
            albumFullPath = self.coverLocation + os.sep + album + '.jpg'

        if not os.path.exists(albumFullPath):
            self.downloadCoverImg(album)
        # 如果下载失败
        if not os.path.exists(albumFullPath):
            albumFullPath = os.getcwd() + os.sep + 'Download' + os.sep + 'Covers' + os.sep + 'Default' + '.jpg'
            
        if os.path.exists(albumFullPath):
            self.ui.coverPixmap.load(albumFullPath)
            self.ui.coverPixmap = self.ui.coverPixmap.scaledToHeight(230)
            self.ui.scene.addPixmap(self.ui.coverPixmap)
            self.ui.coverView.setScene(self.ui.scene)

    def downloadCoverImg(self,album):
        """Download cover images."""
        return baiduMusic.downloadCoverImg(album,self.coverLocation)

    def downloadLyric(self,keyword):
        """Download lyric when necessary."""
        listUrl = baiduMusic.generateUrl(keyword)
        if listUrl:
            try:
                templst = baiduMusic.generateList(listUrl)[1:4]
                suffix,title,artist = templst[0][0],templst[1][0],templst[2][0]
                mp3Url = 'http://music.baidu.com/' + suffix
                baiduMusic.downloadLrcFile(mp3Url,title,artist,self.lrcLocation)
            except:
                pass


class aboutDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_aboutDialog()
        self.ui.setupUi(self)

class dirSettingsDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_dirSettingsDialog()
        self.ui.setupUi(self)

        # 信号绑定
        self.ui.okButton.clicked.connect(self.getLocation)
        self.ui.cancelButton.clicked.connect(self.Close)
        self.ui.mp3LocationButton.clicked.connect(self.getMp3FileLocation)
        self.ui.lrcLocationButton.clicked.connect(self.getLrcFileLocation)

    def getFileLocation(self,dirtype):
        """Open a FileDialog and choose an existing directory."""
        fd = QtGui.QFileDialog(self)
        dirname = fd.getExistingDirectory()
        if dirtype == 'mp3':
            self.ui.mp3LocationEdit.setText(dirname)
        elif dirtype == 'lrc':
            self.ui.lrcLocationEdit.setText(dirname)
        return

    def getMp3FileLocation(self):
        return self.getFileLocation('mp3')

    def getLrcFileLocation(self):
        return self.getFileLocation('lrc')

    def getLocation(self):
        """Get mp3 & lrc dirname from dirSettingsDialog."""
        self.mp3Location = self.ui.mp3LocationEdit.text()
        self.lrcLocation = self.ui.lrcLocationEdit.text()
        self.done(1) # return 1 and close dirSettingsDialog

    def Close(self):
        self.done(0)

class downloadThread(QtCore.QThread):
    """Define a thread class for every downloading."""
    def __init__(self,parent=None,args=()):
        QtCore.QThread.__init__(self,parent)
        self.args = args
    def run(self):
        if len(self.args) == 7:
            # 添加自己定义的reportHook之后，返回一次信息线程就结束了？ time模块问题.
            self.mp3name,self.mp3status = baiduMusic.downloadMp3File(self.args[0] + '/download',self.args[1],self.args[2],self.args[3],self.args[5],self.args[6])
            self.lrcname,self.lrcstatus = baiduMusic.downloadLrcFile(self.args[0],self.args[1],self.args[2],self.args[4],self.args[5],self.args[6]) 
        if not (self.mp3name and self.lrcname):
            self.wait()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    app.setApplicationName("BaiduMusicBox")
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
