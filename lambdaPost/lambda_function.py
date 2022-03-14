import boto3
import uuid
import json
client = boto3.client('dynamodb')

uid = str(uuid.uuid4())
def lambda_handler(event, context):
    uid = str(uuid.uuid4())
    print(event)
    data = client.put_item(
        TableName='users',
        Item={
            'user_id': {
                'S': uid
            },
            'name': {
                'S': event["name"]
            },
            'age': {
                'N': event["age"]
            }
        }
    )



    response = {
        'statusCode': 200,
        'body': 'User no. ' + uid + ' created!',
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response
