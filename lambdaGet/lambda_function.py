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
        data1 = data['Item']['name']['S']
        data2 = data['Item']['age']['N']
        response = {
            'statusCode': 200,
            'body': "{"+"\n"+"\"name\":"+json.dumps(data1)+"\n"+"\"age\":"+json.dumps(data2)+"\n"+"}",
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