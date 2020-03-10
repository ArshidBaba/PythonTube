import logging 
import boto3
from botocore.exceptions import ClientError
from os import listdir
from os.path import isfile, join

#when script runs on my local machine
mypath = '/home/arshid/Hash/youtube/lectures'

#when script runs on ec2
# mypath = '/home/ubuntu/hashlearn/lectures'    

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

s3_client = boto3.client('s3')

for name in onlyfiles:
    try:
        response = s3_client.upload_file('/home/arshid/Hash/youtube/lectures/'+name, 'hl-tmp-videos', 
                                            'lectures/'+name)
        print(response)
    except ClientError as e:
        logging.error(e)
