from os import listdir
from os.path import isfile, join
mypath = '/home/arshid/Hash/youtube/Scripts'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)