from fastapi import APIRouter

r = APIRouter()

r.get('/gupshup/', response_model=bool)
'''
GET all messages
'''
def get_all_messages(messages):
    print(messages)
    return True


r.get('/gupshup/{id}', response_model=bool)
'''
GET one message
'''
def get_one_message(message):
    print(message)
    return True
