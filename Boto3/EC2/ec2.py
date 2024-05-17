import boto3

def create_ec2_instance():
    # Create an EC2 client service client
    ec2_client = boto3.client('ec2')

    # Call the run_instances method to create an instance
    response = ec2_client.run_instances(
        ImageId='ami-013e83f579886baeb',  # Use the correct AMI ID
        MinCount=1,        
        MaxCount=1,
        InstanceType='t2.micro',  # Specify the instance type
        KeyName='newKP',  # Specify your key pair name
        SecurityGroupIds=['sg-0f8c83efc56ba9fa6'],  # Specify your security group
        TagSpecifications=[  # Optionally add tags to the instance
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': 'Boto3Instance2'},
                ]
            },
        ]
    )

    # Extracting instance ID from the response
    print(response)
    instance_id = response['Instances'][0]['InstanceId']
    print("EC2 Instance created:", instance_id)

# Ensure AWS credentials are set up in your environment and call the function
create_ec2_instance()