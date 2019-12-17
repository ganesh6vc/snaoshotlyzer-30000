import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.group()
def instances():
    "Command for instances"
@instances.command('list')
@click.option('--project', default=None, help ="Only instances with project(tag Project<name>)")
def list_instances(project):
    "LIST EC2 instances"
    instances =[]
    if project:
        filters =[{'Name':'tag:Project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags = {t['Key']:t['Value'] for t in i.tags or []}
        # print(i)
        print(','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Project', '<no project>')
            )))
    return

@instances.command('stop')
@click.option('--project', default=None, help ="Only instances with project(tag Project<name>)")
def stop_instances(project):
    "STOP EC2 instances"
    instances =[]
    if project:
        filters =[{'Name':'tag:Project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        print("Stopping instance {0}...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project', default=None, help ="Only instances with project(tag Project<name>)")
def stop_instances(project):
    "START EC2 instances"
    instances =[]
    if project:
        filters =[{'Name':'tag:Project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        print("Starting instance {0}...".format(i.id))
        i.start()
    return

if __name__ == '__main__':
    instances()
