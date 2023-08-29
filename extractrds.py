import json
import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('ses', region_name='ap-south-1')
    rds_client = boto3.client('rds', region_name='ap-south-1')

    # Specify the tag key and value to filter instances
    tag_key = 'RCB'
    tag_value = 'Champion'

    email_body = f"Sample Summary Email:\n\n"
    email_body += f"Good Evening,\n\n"
    email_body += f"Here is a list of RDS Resources running on your account as on {datetime.datetime.now()}:\n\n"

    # Extract RDS instance tags based on the specified tag key and value
    response = rds_client.describe_db_instances()
    for instance in response['DBInstances']:
        tags = instance.get('TagList', [])
        environment_tag = next((tag for tag in tags if tag['Key'] == tag_key and tag['Value'] == tag_value), None)
        if environment_tag:
            instance_id = instance['DBInstanceIdentifier']
            engine = instance['Engine']
            instance_class = instance['DBInstanceClass']
            endpoint = instance['Endpoint']['Address']
            availability_zone = instance['AvailabilityZone']
            status = instance['DBInstanceStatus']

            email_body += f"Instance ID: {instance_id}\n"
            email_body += f"Engine: {engine}\n"
            email_body += f"Instance Class: {instance_class}\n"
            email_body += f"Endpoint: {endpoint}\n"
            email_body += f"Availability Zone: {availability_zone}\n"
            email_body += f"Status: {status}\n\n"

    # Adding line breaks and additional content
    email_body += "\n\nThank You,\nKind Regards!\nTeam AWS"

    response = client.send_email(
        Destination={
            'ToAddresses': ['akshaykhanna7798@gmail.com']
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': email_body,
                }
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Sample Summary Email',
                },
            },
        Source='ick.june8@gmail.com'
    )

    print(response)

    return {
        'statusCode': 200,
        'body': json.dumps("Email Sent Successfully. MessageId is: " + response['MessageId'])
    }
