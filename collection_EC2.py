#!/usr/bin/env python

import boto.ec2
import csv


csv_file = open('/home/dror/Documents/boto/instances.csv','w+')

# A reservation corresponds to a command to start instances. You can see what instances are associated with a reservation:
def process_instance_list(connection):
    map(build_instance_list,connection.get_all_instances())
    print ("Reservation",connection.get_all_instances())

def build_instance_list(reservation):
    map(write_instances,reservation.instances)
    print ("name instances:",reservation.instances)


def write_instances(instance):
  environment = '-'
  if 'environment' in instance.tags:
    environment = instance.tags['environment']
  csv_file.write("{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}{10}{11}\n".format(instance.id,instance.tags['Name'],environment,instance.private_ip_address,instance.state,instance.placement,instance.architecture, instance.vpc_id, instance.kernel, instance.instance_type, instance.image_id, instance.launch_time))
  #csv_file.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n"%(instance.id,instance.tags['Name'],environment,instance.private_ip_address,
  #  instance.state,instance.placement,instance.architecture, instance.vpc_id, instance.kernel, instance.instance_type, instance.image_id, instance.launch_time))
  csv_file.flush()

if __name__=="__main__":
  #connection = EC2Connection(aws_access_key_id='xxxxxxx',aws_secret_access_key='yyyyyyyyyyy')
  connection = boto.ec2.connect_to_region('us-east-1')

process_instance_list(connection)

csv_file.close()