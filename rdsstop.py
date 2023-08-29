import json
import boto3

def lambda_handler(event, context):
    rds_client = boto3.client('rds', region_name='ap-south-1')

    # List all DB instances
    db_instances = rds_client.describe_db_instances()

    for db_instance in db_instances['DBInstances']:
        instance_identifier = db_instance['DBInstanceIdentifier']

        # Get tags for the DB instance
        tags = rds_client.list_tags_for_resource(ResourceName=db_instance['DBInstanceArn'])['TagList']

        # Check if the specified tag exists with the desired value
        if any(tag['Key'] == 'start' and tag['Value'] == 'yes' for tag in tags):
            response = rds_client.stop_db_instance(DBInstanceIdentifier=instance_identifier)
            print(f"Stopped RDS Instance: {instance_identifier}")
            print(response)
