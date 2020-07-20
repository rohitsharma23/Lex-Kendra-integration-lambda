import json

def lambda_handler(event, context):
    #'x-amz-lex:kendra-search-response-answer-1' - Use this to return the FAQ answer that matches the utterance
    #'x-amz-lex:kendra-search-response-question_answer-question-1' - Use this to return the FAQ question
    #'x-amz-lex:kendra-search-response-question_answer-answer-1' - Use this to return the FAQ answer
    #'x-amz-lex:kendra-search-response-document-1' - Use this to return the excerpt (Kendra suggested answer)
    return {
    'dialogAction': {
        'type': 'Close',
        'fulfillmentState': 'Fulfilled',
        'message': {
            'contentType': 'PlainText',
            'content': event["requestAttributes"]["x-amz-lex:kendra-search-response-document-1"]
        }
    }
}