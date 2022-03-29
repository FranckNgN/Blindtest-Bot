from pytube import Playlist
from pytube import Channel
import pandas as pd
import os

#retrieve playlist and song from a youtube channel
#%%

doDL = False
channelUrl = 'https://www.youtube.com/channel/UC8-FX4KsHFaNy0DQH7BXrdg'

c = Channel(channelUrl)

#%%
if __name__ == "__main__":
    playlistDic = {}
    playlistList = [
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F2wzyb_WDIgJEdzl6w8F6G'), #Code Geass
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HerBoNty1XAYD4g26xjwnm'), #Naruto
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GZdEx8UjvAQ4l1Fmdofp6D'), #Naruto Shippuden
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GUVTMmFj0abv7NeeeCAycR'), #Bleach
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Fh_XLX8Ly8U6DWepv4iipS'), #Angel Beats
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GYxXvn72A4ovXBxIaZfbSj'), #Black Lagoon
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FP_OUsjHkF529ljZjQWKdx'), #Ao no Exorcist
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GdAf2FxhLNLRAUzNd679GP'), #Boku no Hero
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EXCwI8yLNCRLLZzUlS-q4j'), #Bungou Stray Dogs
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_E-06egHQ_0Vy4V0G4w0T5N'), #Captain Tsubasa
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EHdT-1jB0_nVumE1nuY49v'), #Mysterieuse Cite Dor
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F96QkibwX23Rpogx30EkV0'), #City Hunter
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Ef7BZRNL6gy4jA0i9l_P6N'), #Code Lyoko
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FqgjHAItydbXI-qRj9vUAE'), #Cowboy Bebop
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GKqh8AeISX4b3lL1l8Qk6f'), #Deadman Wonderland
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EfAwYWbk92hKA04Y4zR1o7'), #Death Note
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FwyAbE964rYzmO_xGwSHz7'), #Detective Conan
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GMfKOR0EdeYwxlag_84BOt'), #Dragon Ball & co
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_H4jxa8ol3wkXaIkjTHa9Bt'), #Koutetsujou no Kabaneri
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FtalwCzmzqllwfN6mQVhrx'), #Durarara
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EVWDYFgbdxcNHl8qjRYjXo'), #Erased
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F4eX9Wyn9k3RRTo3OHT2GB'), #Evangelion
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_F-c14oBifnPVXbgrBBndg-'), #Eyeshield 21
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Hb_eYufrtZ4_64eXioHl9C'), #Fate & co
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HPeiXfHKd819hqbt4yfhyX'), #One Punch Man
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GTyaiQFqiF_f7Y3dF_OAdS'), #Full Metal Alchemist
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HohkEJSj2TEzh8l7cvvC0g'), #GTO
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Flfwst2z_QTqCkPjtcVNe1'), #Kimetsu no Yaiba
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Ef3xxUt0JTyx6MJjVu9c0D'), #SNK
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GJO2UE8Tl3jwk_C3kN0xKq'), #Vinland Saga
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HRe7YKAMFCWPoTZIAeaVx4'), #Yakusoku no Neverland
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GCtoInJSFypsNSmm0lFgEe'), #Boruto
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EeOCYAiwC09SRGpCK5woZ8'), #Pokemon
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_H5tpaoIkGz2RSigZdLxL_c'), #One Piece
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_E-yGGH5olegkA3WWkC5thF'), #Mononoke Hime
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EIzbLiPsYtFPMs3Kj3zgLj'), #Bakemonogatary
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HeTxavmyMAamiFkADICpsx'), #Hyouka
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_G9aZx2eaFCAIe4Da2GMLZ-'), #Kyoukai no Kanata
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_FfK0WL5yM3obqEpAfX8Q_4'), #GrandBlue
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EcU6ehzJR0XwfIRBGP9uz6'), #Parasyte
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EN-gM64gSixgPhL6juo94p'), #Tengen Toppa
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HwaZc--hPXsTQeXIOte8Z0'), #Steins Gate
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HntoomaIh4pNkErluHJDxS'), #Aldnoah Zero
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_HyATz3oIqmxKM0yT6Rd4Xr'), #Rave Master
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_EZedbCZQbuDv0FBsyqrUuX'), #Hunter x Hunter
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GzndQGF4cnGXpFaCCNpUjP'), #Samurai Shamploo
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_Fs4qb2S0lKxthJXe_B4wpc'), #Dr Stone
        Playlist('https://www.youtube.com/playlist?list=PLsAXDMQVId_GStDkZBxCd8r6NDGuJEUnt'), #Dr Stone
        ] 

    for playList in playlistList:
        playlistDic[playList.title] = playList

    if True:
        paramDic = {}
        paramDic['output_path'] = 'D:\Videos\Anime\\'
        paramDic['extDL'] = '.mp4'

        videoDLDic = {}
        videoDLDic['videoTitle'] = []
        videoDLDic['videoURL'] = []
        videoDLDic['videoView'] = []

    #---------------------------------------- Download video for each playlist and each video ---------------------------------------------------------------
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
            #video.streams.first().download()

    #Create a dictionnary and store DL songs into an Excel
    pd.DataFrame(videoDLDic).to_csv(r'D:\Project\TwitchBot\ytDL\alreadyDLSong.csv', index = False)