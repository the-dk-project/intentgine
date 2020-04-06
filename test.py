import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('profile')

def get_item():
    response = table.get_item(
    Key={
            'mobile': '1'
        }
    )

    item = response['Item']
    name = item['fname']

    print(item)
    print("Hello, {}" .format(name))

def put_item():
    table.put_item(
    Item={
            'username': 'ruanb',
            'first_name': 'ruan',
            'last_name': 'bekker',
            'age': 30,
            'account_type': 'administrator',
        }
    )

def create_table():
    dynamodb.create_table(
        TableName='staff',
        KeySchema=[
            {
                'AttributeName': 'username', 
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name', 
                'KeyType': 'RANGE'
            }
        ], 
        AttributeDefinitions=[
            {
                'AttributeName': 'username', 
                'AttributeType': 'S'
            }, 
            {
                'AttributeName': 'last_name', 
                'AttributeType': 'S'
            }, 
        ], 
        ProvisionedThroughput={
            'ReadCapacityUnits': 1, 
            'WriteCapacityUnits': 1
        }
    )

get_item()