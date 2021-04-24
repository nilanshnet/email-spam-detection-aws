import json
import boto3
import email
import sms_spam_classifier_utilities as utilities


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    session = boto3.Session(
        aws_access_key_id='AKIAV4XBFVS6MPVLBKES',
        aws_secret_access_key='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',
    )
    s3_session = session.client('s3')
    response = s3_session.get_object(Bucket=bucket, Key=key)

    email_obj = email.message_from_bytes(response['Body'].read())
    from_email = email_obj.get('From')
    body = email_obj.get_payload()[0].get_payload()

    train_url = ''
    runtime = session.client('runtime.sagemaker')
    vocabulary_length = 9013
    input_mail = [body.strip()]
    temp_1 = utilities.one_hot_encode(input_mail, vocabulary_length)
    input_mail = utilities.vectorize_sequences(temp_1, vocabulary_length)
    data = json.dumps(input_mail)
    response = runtime.invoke_endpoint(EndpointName=train_url, ContentType='application/json', Body=data)
    res = json.loads(response["Body"].read())

    if res['predicted_label'][0][0] == 0:
        label = 'Ok'
    else:
        label = 'Spam'
    score = round(res['predicted_probability'][0][0], 4)
    print(res)

    message = "We received your email sent at " + str(email_obj.get('To')) + " with the subject " + str(email_obj.get('Subject')) + ".\nHere \
is a 240 character sample of the email body:\n\n" + body + "\nThe email was \
categorized as " + label + " with a " + score + "% confidence."

    email_client = session.client('ses')
    response_email = email_client.send_email(
        Destination={'ToAddresses': [from_email]},
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': message,
                },
            },
            'Subject': {
                'Charset': 'UTF-8',
                'Data': 'Spam analysis of you email',
            },
        },
        Source=str(email_obj.get('To')),
    )
    print(response_email)
    return {}
