import json
import math

# Defining the coefficients and intercept from your logistic regression model
COEFFICIENTS = [0.40511806, 0.30750015, -0.36742172, 0.40366636, 0.07474148]  # Coefficients for the features
INTERCEPT = -0.08294645  # Intercept term

# Defining feature means and standard deviations (from training data)
# These were calculated during training and are being hardcoded here for consistent scaling.
FEATURE_MEANS = [-0.0005071, -0.00113819, -0.0033188, -0.00357543, -0.00017482]
FEATURE_STDS = [1.00116478, 0.99520665, 0.99778344, 1.01097902, 0.99562047]

# Logistic regression prediction function
def lambda_handler(event, context):
    try:
        # Extracting query parameters from the event
        query_params = event['queryStringParameters']
        if not query_params:
            raise ValueError("Query parameters are missing")
        
        # Extracting feature values from query parameters
        feature_1 = float(query_params['feature_1'])  # lead_time
        feature_2 = float(query_params['feature_2'])  # previous_cancellations
        feature_3 = float(query_params['feature_3'])  # total_of_special_requests
        feature_4 = float(query_params['feature_4'])  # adr
        feature_5 = float(query_params['feature_5'])  # stays_in_week_nights
        
        # Combining features into a list
        features = [feature_1, feature_2, feature_3, feature_4, feature_5]
        
        # Preprocessing features manually using z-score normalization
        # Formula: z = (x - mean) / std
        normalized_features = [
            (features[i] - FEATURE_MEANS[i]) / FEATURE_STDS[i]
            for i in range(len(features))
        ]
        
        # Computing the log-odds (linear combination of coefficients and features)
        log_odds = INTERCEPT + sum(
            COEFFICIENTS[i] * normalized_features[i] for i in range(len(COEFFICIENTS))
        )
        
        # Converting log-odds to probability
        probability = 1 / (1 + math.exp(-log_odds))
        
        # Converting probability to predicted category (positive or negative)
        predicted_category = 1 if probability >= 0.5 else 0
        
        # Returning the result as a JSON response
        return {
            'statusCode': 200,
            'body': json.dumps({
                'log_odds': log_odds,
                'probability': probability,
                'predicted_category': predicted_category
            })
        }
    
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }
