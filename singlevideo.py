from pytube import YouTube

# yt = YouTube('https://www.youtube.com/watch?v=2ALEMLZKnfA')
link = open('video_ids.txt', 'r')
# link.close()

for i in link:
    print(i)
    try:
        yt = YouTube("https://www.youtube.com/watch?v="+i)
        print(yt.title)

        print(yt.thumbnail_url)

        print(yt.streams.all())

        stream = yt.streams.first()

        print(stream)
        print("Downloading "+yt.title)
        stream.download(filename=yt.title+"_"+i)
        print("Downloaded "+yt.title)
    except:
        print("Connection Error")
        failed_link = open("failed_downloads.txt","a")
        failed_link.write(i)
        failed_link.close()




