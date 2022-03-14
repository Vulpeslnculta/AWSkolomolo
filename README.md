# AWSkolomolo

#### Little private comment before I'll start to explain how I've managed to get it done: That was tough.

### So, I've started by creating REST API in AWS API Gateway, named it kolo, and created methods for Get and Post, and a Get method is in /kolo/{user_id} indentation

### Then I've created dynamoDB named 'users' with key in form of user_id, after that I've created a role in AWS IAM to give access to DynamoDB table

### After that I've created two AWS Lambda functions, one for each method, called PostLambda and GetLambda (both available for you to see in thos repository in according folders)

### And now I can use both of methods:

#### GET: 
https://15ktwrw855.execute-api.eu-central-1.amazonaws.com/api/kolo/{user_id_here}

#### Example body for POST: 
curl -H "Content-Type: application/json" -X POST -d "{\"name\" : \"Nikodem\", \"age\" : \"19\"}" 
https://15ktwrw855.execute-api.eu-central-1.amazonaws.com/api/kolo

#### I know it is far form perfect, but that's what I menage to do in three days, with more time and merithorical help from collegues I'll do it better and faster
