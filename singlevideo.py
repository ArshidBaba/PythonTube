from pytube import YouTube, Stream
from time import sleep

link = open('video_ids.txt', 'r')



for i in link:
    print(i[1:12])
    try:
        yt = YouTube("https://www.youtube.com/watch?v="+i[1:12])
        print(yt.title)

        print(yt.thumbnail_url)
        # do = yt.streams.all()
        # print(type(do))
        print(yt.streams.all())

        stream = yt.streams.filter(progressive=True, res="720p").first()

        print(stream)
        print(type(stream))
        print("Downloading "+yt.title)
        stream.download(output_path='/home/arshid/Hash/youtube/lectures', filename=yt.title+"_"+i)
        # stream.download(output_path='/home/ubuntu/hashlearn/lectures', filename=yt.title+"_"+i)
        print("Downloaded "+yt.title+" successfully")
        link2 = open('successful_video_ids.txt', "a")
        link2.write(i)
        link2.close()
        sleep(10)
    except Exception as e:
        print("An Exception Occured: " + str(e))
        failed_link = open("failed_downloads.txt","a")
        failed_link.write(i)
        failed_link.close()




