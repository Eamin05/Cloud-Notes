import boto3

client = boto3.client('rds')
response = client.create_db_instance(
    AllocatedStorage=400,
    DBInstanceClass='db.r6gd.large',
    DBInstanceIdentifier='mydbinstance',
    Engine='MySQL',
    MasterUserPassword='admin2931',
    MasterUsername='admin',
    Port=3307,
)

print(response)