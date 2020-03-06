from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=2ALEMLZKnfA')
link = open('video_ids.txt', 'r')

for i in link:
    print(i)
    try:
        yt = YouTube("https://www.youtube.com/watch?v="+i)
        print(yt.title)

        print(yt.thumbnail_url)

        print(yt.streams.all())

        stream = yt.streams.first()

        print(stream)

        stream.download()
    except:
        print("Connection Error")




