import os
from twilio.rest import Client

def make_call(word, phone_number):
    '''
    create call with corresponding message, receiving phone number, 
    and outgoing phone number
    '''
    account_sid = 'ACe3c94d6cc6715b520edef665fe6bcbb2'
    auth_token = 'ebb2aa2f84dbfe5fcec6a2fd45e89f94'

    #concatenates phone number with country code (assume CAN/USA country code)
    phone_number = "1" + phone_number
    
    client = Client(account_sid, auth_token)

    call = client.calls.create(
                        twiml='<Response><Say>{}</Say></Response>'.format(word), #xml formatted word
                        to='{}'.format(phone_number), 
                        from_='+18154166403'
                    )

    print("You will receive a call momentarily! Your call sid is: " + call.sid)