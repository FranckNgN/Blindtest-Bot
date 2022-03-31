from ast import Str
import googleapiclient.discovery
import pandas as pd
import os

def getYtPlaylistInfoDf(channelId: str) -> pd.DataFrame:
    cwdPath = os.getcwd() + '\\'
    dataConfig = pd.read_csv(cwdPath + 'dataConfig.csv') #retrieve youtube API key from excel
    ytKey = dataConfig['youtubeAPI'][0]

    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = ytKey)

    request = youtube.playlists().list(
        part = "snippet",
        channelId = channelId,
        maxResults = 50)

    response = request.execute()

    playlists = []
    while request is not None:
        response = request.execute()
        playlists += response["items"]
        request = youtube.playlists().list_next(request, response)

    playlistsInfoDf = pd.DataFrame(playlists)
    playlistsInfoDf = playlistsInfoDf.loc[playlistsInfoDf.etag != 'o8vtZVZLSSHZcpfGC3qJ8MGSJ9g'] # delete non anime playlist, #TODO to check why deleted playlist is still showing in the api
    snippetColumnZip = playlistsInfoDf['snippet'].apply(pd.Series) #Split snippet column

    playlistsInfoDf = pd.concat([playlistsInfoDf, snippetColumnZip], axis = 1) 

    return playlistsInfoDf

getYtPlaylistInfo(channel_id)