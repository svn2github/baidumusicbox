# -*- coding: utf-8 -*-

# 2012/11/20
# lwldcr@gmail.com

"""Download mp3 files from music.baidu.com."""

import os,urllib,re,time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')#加了这两句就无法在IDLE里运行？？？

#print sys.getdefaultencoding()

baseUrl = 'http://music.baidu.com/'
DefaultMusicDir = 'Download'

def generateUrl(keywords):
    """Generate full url with keywords given."""
    
    if not keywords:
        print u"缺少搜索关键字".decode('utf-8')
        return None
    searchUrl = baseUrl + 'search?key=' + '+'.join(keywords.split())
    return searchUrl

def generateList(listUrl):
    """Generate search result lists.
    seqList: search results' sequences.
    suffixList: search results' url suffixes.
    titleList: search results' titles.
    artistList: search results' artists.
    albumList: search results' albums."""

    if not listUrl:
        return False
    else:
        try:
            searchHtml = urllib.urlopen(str(listUrl)).read()
        except IOError:
            searchHtml = ''

    if not searchHtml:
        return 10 # 10代表网络不通
    
    # 只取前15个结果
    seqList = re.findall('index-num index-hook.*?>.*?([0-9]+).*?<',searchHtml,re.S)[:15] # ['01','02',...]
    suffixList = re.findall('<a href="(/song/[0-9]*?)"',searchHtml,re.S) # ['/song/13685414', '/song/11275689',...]
    #titleList = re.findall('<a href="/song/.*?title="(.*?)"',searchHtml,re.S) #['Moves Like Jagger', 'Moves Like Jagger',...]
    titleListTemp = re.findall('<a href="/song/.*?title="(.*?)(审批文号：[a-zA-Z0-9]*?)?"',searchHtml,re.S) #['Moves Like Jagger', 'Moves Like Jagger',...]
    artistList = re.findall('<span class="author_list".*?title="(.*?)"',searchHtml,re.S)[:16]
    albumList = re.findall('<a href="/album/.*?" title="(.*?)"',searchHtml,re.S)[:16]
    # 如果在歌曲列表的顶端出现一个嵌入的专辑播放器，那么会多截取一个artist以及album,需要额外处理

    titleList = []
    for e in titleListTemp:
        titleList.append(e[0])

    if not (seqList and suffixList and titleList and artistList and albumList):
        return 20 # 20 代表没有搜索结果
        
    if re.search('<a href=".*?" onclick=".*?" title',searchHtml):
        artistList = artistList[1:]
        albumList = albumList[1:]
    else:
        artistList = artistList[:-1]
        if len(albumList) == 16:
            albumList = albumList[:-1] # albumList一般只有几个元素

    while len(albumList) != 15:
        albumList.append('No Album Info')

    if __name__ == '__main__':
        try:
            for i in xrange(0,15):
                text = str(seqList[i]+'\t'+titleList[i]+'\t'+artistList[i]+'\t'+albumList[i]).decode('utf-8')
                #print "%s: %s   %s  %s" % (seqList[i],titleList[i],artistList[i],albumList[i])
                print text
        except:
            pass

        print u"输入选择下载的歌曲序号（默认=1,q=退出）：".decode('utf-8'),
        choice = raw_input()
        if not choice:
            choice = 0
            
        if str(choice).lower() == 'q':
            print 'Exiting...'
            sys.exit(0)

        if choice and 0 < int(choice) <= 15:
            choice = int(choice) - 1
        else:
            choice = 0

        return suffixList[choice],titleList[choice],artistList[choice],albumList[choice] # 当做脚本运行时，返回一个元组

    else:
        return seqList,suffixList,titleList,artistList,albumList # 当做模块运行时，返回五个列表

def reportHook(blocks_read,block_size,total_size,seq=''):
    """报告下载信息."""
    if not blocks_read:
        print "Connection opened."
    if total_size < 0:
        print "Read %d blocks" % blocks_read
    else:
        print "Downloading: %.2f %%, totalsize: %d KB" % ( blocks_read*block_size * 100.0 / total_size, total_size/1024.0)
        time.sleep(1)

def downloadMp3File(mp3Url,title,artist='',Dir='',progressFunc=reportHook, itemSeq=''):
    """Download mp3 file chosen in generateList()."""
    if Dir:
        musicDir = Dir
    else:
        musicDir = os.getcwd() + os.sep + DefaultMusicDir
        
    if not os.path.exists(musicDir):
        os.mkdir(musicDir)

    downloadHtml = urllib.urlopen(mp3Url).read()
    mp3Location = baseUrl + re.findall('a href="(/data/.*?)"',downloadHtml,re.S)[0]
    mp3FileName = str(musicDir + os.sep + title + ('' if not artist else '-'+artist) + '.mp3').decode('utf-8')

    if os.path.exists(mp3FileName):
        if __name__ == '__main__':
            print '"%s" 已经存在.' % mp3FileName
        return mp3FileName,10
    else:
        urllib.urlretrieve(mp3Location,mp3FileName,progressFunc,seq=itemSeq)

    if os.path.exists(mp3FileName):
        if __name__ == '__main__':
            print '"%s" 下载成功.' % mp3FileName
        return mp3FileName,20
    else:
        if __name__ == '__main__':
            print '"%s" 下载失败.' % mp3FileName
        return None,False
    
def downloadLrcFile(mp3Url,title,artist='',Dir='',progressFunc=reportHook,itemSeq=''):
    """Download lrc file of chosen mp3 file."""
    if Dir:
        lrcDir = Dir
    else:
        lrcDir = os.getcwd() + os.sep + DefaultMusicDir + os.sep + 'lyrics'
        
    if not os.path.exists(lrcDir):
        os.mkdir(lrcDir)

    mp3Html = urllib.urlopen(mp3Url).read()
    lrcFileName = str(lrcDir + os.sep + title + ('' if not artist else '-' + artist) + '.lrc').decode('utf-8')

    if os.path.exists(lrcFileName):
        if __name__ == '__main__':
            print '"%s" 已经存在.' % lrcFileName
        return lrcFileName,10
    else:
        lrcLocation = baseUrl + re.findall('href":"(.*?)"',mp3Html,re.S)[0]
        urllib.urlretrieve(lrcLocation,lrcFileName,progressFunc,seq=itemSeq)

    if os.path.exists(lrcFileName):
        if __name__ == '__main__':
            print '"%s" 下载成功' % lrcFileName
        return lrcFileName,20
    else:
        if __name__ == '__main__':
            print '"%s" 下载失败' % lrcFileName
        return None,False

def downloadCoverImg(album,Dir=''):
    if not Dir:
        coverDir =  Dir
    else:
        coverDir = os.getcwd() + os.sep + DefaultMusicDir + os.sep + 'Covers'
    if not os.path.exists(coverDir):
        os.mkdir(coverDir)

    coverImgName = str(coverDir + os.sep + album + '.jpg').decode('utf-8')
    if os.path.exists(coverImgName):
        if __name__ == '__main__':
            print '"%s" 已经存在.' % lrcFileName
        return coverImgName,10
    else:
        albumSearchUrl = baseUrl + '/search/album?key=' + album.decode('utf-8')
        try:
            albumSearchHtml = urllib.urlopen(str(albumSearchUrl)).read()
        except IOError:
            return None,False

        albumUrlSuffix = re.findall('<a href="(/album/[0-9]*?)"',albumSearchHtml,re.S)[0]
        albumHtml = urllib.urlopen(str(baseUrl + albumUrlSuffix)).read()
        try:
            coverLocation = re.findall('<span class="cover"><img src="(http://.*?)"',albumHtml,re.S)[0]
        except IndexError:
            # 如果没有结果
            return None,False

        if coverLocation:
            urllib.urlretrieve(coverLocation,coverImgName)

    if os.path.exists(coverImgName):
        if __name__ == '__main__':
            print '"%s" 下载成功' % lrcFileName
        return coverImgName,20
    else:
        if __name__ == '__main__':
            print '"%s" 下载失败' % lrcFileName
        return None,False

    

if __name__ == "__main__":
    print u"输入搜索歌名:".decode('utf-8'),

    if os.name == "posix":
        keywords = raw_input().decode('utf-8')
    elif os.name == 'nt':
        keywords = raw_input().decode('gbk')

    if not keywords:
        print u'输入错误'.decode('utf-8')
        sys.exit(1)
    listUrl = generateUrl(keywords)
    if listUrl:
        result = generateList(listUrl)

        try:
            (suffix,title,artist,album) = result
            mp3Url = baseUrl + suffix
            downloadMp3File(mp3Url + '/download',title,artist)
            downloadLrcFile(mp3Url,title,artist)
            downloadCoverImg(album)
            raw_input("Press ENTER to continue...")
        except TypeError:
            if str(result).isdigit():
                if result == 10:
                    print u'网络错误'.decode('utf-8')
                elif result == 20:
                    print u'没有找到合适结果'.decode('utf-8')
                    raw_input('Press ENTER to continue...')
            sys.exit(1)

    else:
        sys.exit(1)
