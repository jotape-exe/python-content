from pytube import YouTube

url = input(str("Url para download: "))
video = YouTube(url)

stream = video.streams.get_highest_resolution()

stream.download(output_path = 'C:/Users/joao_/Downloads')