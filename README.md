# boto-project
These scripts are task with Boto

setup boto in local :

1. sudo pip install boto3
2. vim "~/.aws/config"

[default]
output = json
region = us-east-1

3. sudo vim ~/.aws/credentials

[default]
aws_access_key_id = xxxxxxxxxxxxxxxx
aws_secret_access_key = xxxxxxxxxxxxxxxxxx


1. Add collection_EC2.py : this script collection all inforamtion from instances 

  
