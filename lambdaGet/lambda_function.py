import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):

    data = client.get_item(
        TableName='users',
        Key={
            'user_id': {
                'S':event['pathParameters']['user_id']
            }
        }
    )

    if 'Item' in data:
        response = {
            'statusCode': 200,
            'body': json.dumps(data),
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
            },
        }
    else:
        response = {
            'statusCode': 404,
            'body': "Data Not Found"
        }
    return response