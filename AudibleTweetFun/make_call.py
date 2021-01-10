import os
from twilio.rest import Client

def create_client():
    '''
    uses twilio api id and authorization token to create client 
    for twilio access
    '''
    account_sid = 'ACe3c94d6cc6715b520edef665fe6bcbb2'
    auth_token = 'd92586876aa596ff1b2dacb3e478c312'
    
    client = Client(account_sid, auth_token)

def make_call(word):
    '''
    create call with corresponding message, to phone number, 
    and from phone number
    '''
    call = client.calls.create(
                        twiml='<Response><Say>{}</Say></Response>'.format(word), #xml formatted word
                        to='+16178931229',
                        from_='+18154166403'
                    )

    print(call.sid)