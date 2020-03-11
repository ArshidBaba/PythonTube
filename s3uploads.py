import logging 
import boto3
from botocore.exceptions import ClientError
from os import listdir
from os.path import isfile, join
import pickle

#when script runs on my local machine
# mypath = '/home/arshid/Hash/youtube/lectures'

#when script runs on an ec2 instance
mypath = '/home/ubuntu/hashlearn/lectures'    

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

s3_client = boto3.client('s3')

videos_info = {}

for name in onlyfiles:
    try:
        response = s3_client.upload_file('/home/arshid/Hash/youtube/lectures/'+name, 'hl-tmp-videos', 
                                            'lectures/'+name)

        print(response)
        url = 'https://%s.s3.amazonaws.com/%s' % ("hl-tmp-videos", 'lectures/'+name)
        videos_info[name] = url
    
    except ClientError as e:
        logging.error(e)
with open('videosinfo.txt', 'wb') as file:
    pickle.dump(videos_info, file)
