# snaoshotlyzer-30000
Demo project to manage AWS EC2 Instances and snapshots

## About

This project is a demo , and used boto3 to manage AWS Ec2 Instances and snapshots

## Configuring
shotty uses the config file created by the AWS cli. e.g.

`aws configure --profile shotty`

## Running

`pipenv run "python shotty/shotty.py" <command> <--project==PROJECT`

**command** is list,start or stop
**project** tag is optional
