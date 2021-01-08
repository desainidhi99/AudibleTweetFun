# +18154166403

import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACe3c94d6cc6715b520edef665fe6bcbb2'
auth_token = 'd92586876aa596ff1b2dacb3e478c312'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        to='+16178931229',
                        from_='+18154166403'
                    )

print(call.sid)