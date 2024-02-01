from pytube import Channel
from ytDownload import YTPlaylistInfo as ytPlayInf
import pandas as pd
import os
from importlib import reload
from datetime import date

reload(ytPlayInf)

def dlYoutubeVideo(paramDic:dict, playlistDic:dict, videoDLDic: dict, doDL = True) -> None:
    for playlistName, playlist in playlistDic.items():#Loop through the different youtube playlist
        print("Downloading :", playlistName)
        outputPathAnime = paramDic['output_path'] + playlistName

        if not os.path.exists(outputPathAnime): #If the anime folder does not exist => create one, else pass
            os.mkdir(outputPathAnime)

        for video in playlist.videos:#for each video in the playlist
            videoName = video.title
            videoUrl = video.watch_url
            videoViews = video.views

            videoDLDic['videoPlaylist'].append(playlistName)
            videoDLDic['videoTitle'].append(videoName)
            videoDLDic['videoURL'].append(videoUrl)
            videoDLDic['videoView'].append(videoViews)

            if doDL:
                st = video.streams.get_highest_resolution()
                st.download(output_path = outputPathAnime) 

if __name__ == "__main__":
    if True: #Do parameters
        doDL = True
        doDLTypeAnime = True
        doOldMethod = False

    if True: #Channel setting
        if doDLTypeAnime: #DL ANIME SONG
            channelId = "UC8-FX4KsHFaNy0DQH7BXrdg" # Channel ID set to SenTh// new SenTh ID: UCFnYVA7HrwUojzxRXkhMo9w
            typeVideo = 'Anime'

        else: #DL FILM SONG
            channelId = "UCp7LMeHbEKnKwQpxNWuLNJA" # Channel ID set to senthFilm
            typeVideo = 'Film'

        channelUrl = 'https://www.youtube.com/channel/' + channelId
        cwdPath = os.getcwd() + '\\'
        dlSongName = 'alreadyDLSong' + typeVideo + '.xlsx'

        c = Channel(channelUrl)
    
    playlistsInfoDic = ytPlayInf.getYtPlaylistInfoDf(channelId).to_dict() #get info for each playlist in youtube
    playlistDic = ytPlayInf.createPlaylistDic(playlistsInfoDic, doOldMethod = doOldMethod)

    if True:
        paramDic = {}
        paramDic['output_path'] = 'D:\Videos\\Blind Test\\' + typeVideo + '\\'
        paramDic['extDL'] = '.mp4'

        videoDLDic = {}
        videoDLDic['videoPlaylist'] = []
        videoDLDic['videoTitle'] = []
        videoDLDic['songType'] = []
        videoDLDic['songName'] = []
        videoDLDic['songCompositor'] = []
        videoDLDic['videoURL'] = []
        videoDLDic['videoView'] = []
        videoDLDic['popularity'] = []
        videoDLDic['videoType'] = []
        videoDLDic['dateDL'] = []

    #---------------------------------------- Download video for each playlist and each video ---------------------------------------------------------------
    dlYoutubeVideo(paramDic, playlistDic, videoDLDic, doDL)# DL song and updates videoDLDic

    def videoDLDicUpdt(videoDLDic, doDLTypeAnime):
        numbVideoDL = len(videoDLDic['videoTitle'])
        videoDLDic['videoType'] = ['Anime'  if doDLTypeAnime else 'Film' for numbVideo in range(numbVideoDL)]# if doDLTypeAnime else 'Film'
        videoDLDic['dateDL'] = [date.today() for numbVideo in range(numbVideoDL)]
        videoDLDic['isAvailable'] = [True for numbVideo in range(numbVideoDL)]

    #Create a dictionnary and store DL songs into an Excel
    videoDLDicUpdt(videoDLDic, doDLTypeAnime)

    def createVideoDic(playlistDic:dict):
        videoDLDic = {}
        videoDLDic['videoPlaylist'] = []
        videoDLDic['videoTitle'] = []
        videoDLDic['songType'] = []
        videoDLDic['songName'] = []
        videoDLDic['songCompositor'] = []
        videoDLDic['videoURL'] = []
        videoDLDic['videoView'] = []
        videoDLDic['popularity'] = []
        videoDLDic['videoType'] = []
        videoDLDic['dateDL'] = []
        videoDLDic['isAvailable'] = []

        for playlistName, playlist in playlistDic.items():
            for video in playlist.videos:#for each video in the playlist
                videoName = video.title
                videoUrl = video.watch_url
                videoViews = video.views

                videoDLDic['videoPlaylist'].append(playlistName)
                videoDLDic['videoTitle'].append(videoName)
                videoDLDic['videoURL'].append(videoUrl)
                videoDLDic['videoView'].append(videoViews)

                videoDLDic['songType'].append('NA')
                videoDLDic['songName'].append('NA')
                videoDLDic['songCompositor'].append('NA')
                videoDLDic['popularity'].append('NA')

        numbVideoDL = len(videoDLDic['videoTitle'])
        videoDLDic['videoType'] = ['Anime'  if doDLTypeAnime else 'Film' for numbVideo in range(numbVideoDL)]# if doDLTypeAnime else 'Film'
        videoDLDic['dateDL'] = [date.today() for numbVideo in range(numbVideoDL)]
        videoDLDic['lastUpdate'] = [date.today() for numbVideo in range(numbVideoDL)]
        videoDLDic['isAvailableOnChanell'] = [True for numbVideo in range(numbVideoDL)]
        return videoDLDic

newDlSong = createVideoDic(playlistDic)
pd.DataFrame(list(newDlSong.values()),index = newDlSong.keys()).T.to_csv('test.csv')
