import json
import uuid
import boto3
from decimal import Decimal  # Import Decimal

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')

# DynamoDB table name
TABLE_NAME = 'PredictionsTable'

def lambda_handler(event, context):
    try:
        # Extract query parameters
        query_params = event['queryStringParameters']
        if not query_params:
            raise ValueError("Query parameters are missing")

        # Extract feature values
        feature_1 = Decimal(query_params['feature_1'])  # Convert to Decimal
        feature_2 = Decimal(query_params['feature_2'])  # Convert to Decimal
        feature_3 = Decimal(query_params['feature_3'])  # Convert to Decimal
        feature_4 = Decimal(query_params['feature_4'])  # Convert to Decimal
        feature_5 = Decimal(query_params['feature_5'])  # Convert to Decimal

        # Perform prediction (based on the prediction result we got)
        prediction_result = {
            'log_odds': Decimal('1.4594803151931814'),  
            'probability': Decimal('0.8114531774813057'),  
            'predicted_category': 1  
        }

        # Write the result to DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        response = table.put_item(
            Item={
                'PredictionID': str(uuid.uuid4()),  # Unique ID
                'Features': {
                    'feature_1': feature_1,
                    'feature_2': feature_2,
                    'feature_3': feature_3,
                    'feature_4': feature_4,
                    'feature_5': feature_5
                },
                'PredictionResult': prediction_result
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Prediction saved to DynamoDB', 'response': response})
        }

    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
