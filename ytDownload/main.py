from pytube import Channel
from ytDownload import YTPlaylistInfo as ytPlayInf
import pandas as pd
import os
from importlib import reload


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

            videoDLDic['videoTitle'].append(videoName)
            videoDLDic['videoURL'].append(videoUrl)
            videoDLDic['videoView'].append(videoViews)

            st = video.streams.get_highest_resolution()
            
            if doDL:
                st.download(output_path = outputPathAnime) 

if __name__ == "__main__":
    if True: #Do parameters
        doDL = True
        doDLTypeAnime = False
        doOldMethod = False

    if True: #Channel setting
        if doDLTypeAnime: #DL ANIME SONG
            channelId = "UC8-FX4KsHFaNy0DQH7BXrdg" # Channel ID set to SenTh
            typeVideo = 'Anime'
        else:
            channelId = "UC8-FX4KsHFaNy0DQH7BXrdg"
            typeVideo = 'Film'

        channelUrl = 'https://www.youtube.com/channel/' + channelId
        cwdPath = os.getcwd() + '\\'
        dlSongName = 'alreadyDLSong' + typeVideo + '.csv'

        c = Channel(channelUrl)
    
    playlistsInfoDic = ytPlayInf.getYtPlaylistInfoDf(channelId).to_dict() #get info for each playlist in youtube
    playlistDic = ytPlayInf.createPlaylistDic(playlistsInfoDic, doOldMethod = doOldMethod)

    if True:
        paramDic = {}
        paramDic['output_path'] = 'D:\Videos\\' + typeVideo + '\\'
        paramDic['extDL'] = '.mp4'

        videoDLDic = {}
        videoDLDic['videoTitle'] = []
        videoDLDic['videoURL'] = []
        videoDLDic['videoView'] = []

    #---------------------------------------- Download video for each playlist and each video ---------------------------------------------------------------
    dlYoutubeVideo(paramDic, playlistDic, videoDLDic, doDL)# DL song and updates videoDLDic

    #Create a dictionnary and store DL songs into an Excel
    pd.DataFrame(videoDLDic).to_csv(cwdPath + dlSongName, index = False)