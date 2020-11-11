import boto3
import config
import sys
import os

path     = ''
filename = ''

argv = sys.argv
argc = len(argv)

if argc == 2:
    filename = argv[1]
    path = os.path.dirname(os.path.realpath(__file__))

if argc == 3:
    path = argv[1]
    filename = argv[2]

abs_path = os.path.join(path,filename)

secrets = config.get()

AccessKey = secrets['ACCESS_KEY']
SecretKey = secrets['SECRET_KEY']
ID = secrets['ID']
Deployment = secrets['DEPLOYMENT']

aws_path = Deployment + '/Relays/' + ID + "/" + filename

session = boto3.Session(aws_access_key_id=AccessKey, aws_secret_access_key=SecretKey)
s3 = session.resource('s3')

try:
    with open(abs_path, "rb") as f:
        s3.Bucket("besi-c").put_object(Key=aws_path, Body=f)
except Exception as e:
    print(e)