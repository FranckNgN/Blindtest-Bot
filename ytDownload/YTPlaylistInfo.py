from ast import Str
import googleapiclient.discovery
import pandas as pd
import os
from pytube import Playlist

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

def createPlaylistDic(playlistsInfoDic:dict, doOldMethod = True):
    playlistDic = {}

    if doOldMethod:
        playlistList = [
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F2wzyb_WDIgJEdzl6w8F6G'),  # Code Geass
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HerBoNty1XAYD4g26xjwnm'),  # Naruto
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GZdEx8UjvAQ4l1Fmdofp6D'),  # Naruto Shippuden
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GUVTMmFj0abv7NeeeCAycR'),  # Bleach
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Fh_XLX8Ly8U6DWepv4iipS'),  # Angel Beats
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GYxXvn72A4ovXBxIaZfbSj'),  # Black Lagoon
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FP_OUsjHkF529ljZjQWKdx'),  # Ao no Exorcist
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GdAf2FxhLNLRAUzNd679GP'),  # Boku no Hero
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EXCwI8yLNCRLLZzUlS-q4j'),  # Bungou Stray Dogs
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_E-06egHQ_0Vy4V0G4w0T5N'),  # Captain Tsubasa
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EHdT-1jB0_nVumE1nuY49v'),
            # Mysterieuse Cite Dor
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F96QkibwX23Rpogx30EkV0'),  # City Hunter
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Ef7BZRNL6gy4jA0i9l_P6N'),  # Code Lyoko
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FqgjHAItydbXI-qRj9vUAE'),  # Cowboy Bebop
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GKqh8AeISX4b3lL1l8Qk6f'),  # Deadman Wonderland
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EfAwYWbk92hKA04Y4zR1o7'),  # Death Note
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FwyAbE964rYzmO_xGwSHz7'),  # Detective Conan
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GMfKOR0EdeYwxlag_84BOt'),  # Dragon Ball & co
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_H4jxa8ol3wkXaIkjTHa9Bt'),
            # Koutetsujou no Kabaneri
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FtalwCzmzqllwfN6mQVhrx'),  # Durarara
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EVWDYFgbdxcNHl8qjRYjXo'),  # Erased
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F4eX9Wyn9k3RRTo3OHT2GB'),  # Evangelion
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F-c14oBifnPVXbgrBBndg-'),  # Eyeshield 21
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Hb_eYufrtZ4_64eXioHl9C'),  # Fate & co
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HPeiXfHKd819hqbt4yfhyX'),  # One Punch Man
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GTyaiQFqiF_f7Y3dF_OAdS'),
            # Full Metal Alchemist
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HohkEJSj2TEzh8l7cvvC0g'),  # GTO
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Flfwst2z_QTqCkPjtcVNe1'),  # Kimetsu no Yaiba
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Ef3xxUt0JTyx6MJjVu9c0D'),  # SNK
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GJO2UE8Tl3jwk_C3kN0xKq'),  # Vinland Saga
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HRe7YKAMFCWPoTZIAeaVx4'),
            # Yakusoku no Neverland
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GCtoInJSFypsNSmm0lFgEe'),  # Boruto
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GC6TUMe22nrTfd8ebrXLnG'),  # Laputa
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EeOCYAiwC09SRGpCK5woZ8'),  # Pokemon
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_H5tpaoIkGz2RSigZdLxL_c'),  # One Piece
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_E-yGGH5olegkA3WWkC5thF'),  # Mononoke Hime
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EIzbLiPsYtFPMs3Kj3zgLj'),  # Bakemonogatary
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HeTxavmyMAamiFkADICpsx'),  # Hyouka
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_G9aZx2eaFCAIe4Da2GMLZ-'),  # Kyoukai no Kanata
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FfK0WL5yM3obqEpAfX8Q_4'),  # GrandBlue
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EcU6ehzJR0XwfIRBGP9uz6'),  # Parasyte
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EN-gM64gSixgPhL6juo94p'),  # Tengen Toppa
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HwaZc--hPXsTQeXIOte8Z0'),  # Steins Gate
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HntoomaIh4pNkErluHJDxS'),  # Aldnoah Zero
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HyATz3oIqmxKM0yT6Rd4Xr'),  # Rave Master
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EZedbCZQbuDv0FBsyqrUuX'),  # Hunter x Hunter
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GzndQGF4cnGXpFaCCNpUjP'),  # Samurai Shamploo
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Fs4qb2S0lKxthJXe_B4wpc'),  # Dr Stone
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GStDkZBxCd8r6NDGuJEUnt'),  # Jujutsu Kaisen
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F9BI3uAeHs3AkILIX9foh8'),  # Yu Yu Hakusho
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EdD5I7yIcf8xgdmbzWrpO0'),  # Shokugeki no Soma
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GBxlJM71jUqMElaOMG7Ur-'),  # Hunter x Hunter
            Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_ETmvU7CmuuLE_cSzqMZkSG'),  # Hajime no Ippo
        ]#Create manually a list of playlist song from the youtube channel added one by one by hand

        for playList in playlistList:#create a playlist dic where the key is the name of the anime and the values is the playlist object
            playlistDic[playList.title] = playList

    else:
        n = len(playlistsInfoDic['title'])#Number of anime playlists in the youtube channel
        for playlistsIth in range(n):
            playlistName = playlistsInfoDic['title'][playlistsIth]
            playlistYTUrl = "https://www.youtube.com/playlist?list=" + playlistsInfoDic['id'][playlistsIth]

            playlistDic[playlistName] = playlistYTUrl

        for anime in list(playlistDic.keys()):
            playlistDic[anime] = Playlist(playlistDic[anime])

    return playlistDic

# # TEST
# cwdPath = os.getcwd() + '\\'
# dataConfig = pd.read_csv(cwdPath + 'dataConfig.csv') #retrieve youtube API key from excel

# channelIdOld = "UC8-FX4KsHFaNy0DQH7BXrdg" 
# channelIdNew = "UCFnYVA7HrwUojzxRXkhMo9w" 

# ytKey = dataConfig.loc[dataConfig['Channel ID'] == channelIdOld]['youtubeAPI'][0]

# youtube = googleapiclient.discovery.build("youtube", "v3", developerKey = ytKey)
# request = youtube.playlists().list(
#         part = "snippet",
#         channelId = channelIdOld,
#         maxResults = 50)

# playlists = []
# while request is not None:
#     response = request.execute()
#     playlists += response["items"]
#     request = youtube.playlists().list_next(request, response)

# playlistsInfoDf = pd.DataFrame(playlists)
# playlistsInfoDf = playlistsInfoDf.loc[playlistsInfoDf.etag != 'o8vtZVZLSSHZcpfGC3qJ8MGSJ9g'] # delete non anime playlist, #TODO to check why deleted playlist is still showing in the api
# snippetColumnZip = playlistsInfoDf['snippet'].apply(pd.Series) #Split snippet column

# playlistsInfoDf = pd.concat([playlistsInfoDf, snippetColumnZip], axis = 1) 