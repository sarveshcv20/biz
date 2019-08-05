#!/usr/bin/python

# Variables to be supplied
# 1. .boto file is assumed to be in place or pass cred explicitly 2.Region 3.recipient and sender mail-id 4. sender mail credentials for smtp client 

# Importing python modules
import boto3
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# Declaring variables
open_sgs = {"SG" : {}}
grp_data = []
region = "eu-central-1"
ec2=boto3.client('ec2', region )
security_groups = ec2.describe_security_groups()
security_groups = security_groups["SecurityGroups"]
recipients = ['sarveshanand94@gmail.com']

# Func to sendmail
def send_email(email_body,recipients,subject):
  msg = MIMEMultipart()
  msg['From'] = 'sarveshanand94@gmail.com'
  msg['To'] = (',').join(recipients)
  msg['Subject'] = subject
  msg.attach(MIMEText(email_body, 'plain'))
  password = 'XXXXXX'
  email = smtplib.SMTP('smtp.gmail.com:587')
  email.starttls()
  email.login(msg['From'], password)
  email.sendmail(msg['From'], recipients, msg.as_string())
  email.quit()

# Program starts here
# Finding exposed sg's
for security_group in security_groups:
    security_ip_permissions = security_group['IpPermissions']
    security_group_name = security_group['GroupName']
    security_group_id = security_group['GroupId']
    for per_rule in security_ip_permissions:
        for item in per_rule['IpRanges']:
            if 'CidrIp' in item.keys():
                if item['CidrIp'] == '0.0.0.0/0':
                    open_sgs['SG'][security_group_name] = security_group_id

# Converting dict into list
for key,value in open_sgs['SG'].iteritems():
    tmp = '%s : %s' %(key,value)
    grp_data.append(tmp)

if len(grp_data) > 0:
    print grp_data
    msg = "Below Security groups are found to be exposed to outside world\n\n%s" % ("\n".join(grp_data))
    send_email(msg, recipients,"EXPOSED SECURITY GROUPS IN REGION %s" %(region))
