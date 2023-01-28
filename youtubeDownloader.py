import pytube

url = input("Enter Video url : ")
path = "/home/ashuthe1/YoutubeDownloads"

pytube.YouTube(url).streams.get_highest_resolution().download(path)