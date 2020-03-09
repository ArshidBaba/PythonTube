from pytube import YouTube, Stream

link = open('video_ids.txt', 'r')

for i in link:
    print(i)
    try:
        yt = YouTube("https://www.youtube.com/watch?v="+i)
        print(yt.title)

        print(yt.thumbnail_url)
        # do = yt.streams.all()
        # print(type(do))
        print(yt.streams.all())

        stream = yt.streams.filter(progressive=True, res="720p").first()

        print(stream)
        print(type(stream))
        print("Downloading "+yt.title)
        stream.download(filename=yt.title+"_"+i)
        print("Downloaded "+yt.title+" successfully")
    except Exception as e:
        print("An Exception Occured: " + str(e))
        failed_link = open("failed_downloads.txt","a")
        failed_link.write(i)
        failed_link.close()




