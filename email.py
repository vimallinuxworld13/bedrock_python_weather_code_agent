import json

def lambda_handler(event, context):
    # TODO implement
    print("i m Vimal")
    print(event )
    
    emailID = event['parameters'][0]['value']
    print(emailID)
    
    
    action_response = {
        "actionGroup": event["actionGroup"],
        "apiPath": event["apiPath"],
        "httpMethod": event["httpMethod"],
        "parameters": event["parameters"],
        "httpStatusCode": 200,
        "responseBody": {
				"application/json": {
					"body": {"emailDescription": "email send successfull to students"}
				}
				}
    }
    
    session_attributes = event["sessionAttributes"]
    prompt_session_attributes = event["promptSessionAttributes"]
    
    return {
        "messageVersion": "1.0",
        "response": action_response,
        "sessionAttributes": session_attributes,
        "promptSessionAttributes": prompt_session_attributes,
    }
    
    
