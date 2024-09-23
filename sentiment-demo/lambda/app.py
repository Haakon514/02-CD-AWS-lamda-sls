import os
import json
import boto3

def handler(event, context):

    client = boto3.client('comprehend')
    body = event["body"]
    sentiment = client.detect_sentiment(LanguageCode = "en", Text = body)
    Sentiment["Sentiment"] = "POSITIVE"

    return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "sentiment ": json.dumps(sentiment),
                "Sentiment" : json.dumps(Sentiment)
            })
    }
