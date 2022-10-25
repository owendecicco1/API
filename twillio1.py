import keys2
from twilio.rest import Client

client = Client(keys2.accountSSID,keys2.authToken)

TwilioNUMBER = "+18507808632"

myCellPhone = "+12015270829"

textmessage = client.messages.create(to = myCellPhone,from_= TwilioNUMBER,
                body = "Hello!")

print(textmessage.status)

#make a phone call

call = client.calls.create(url = "http://demo.twilio.com/docs/voice.xml", to = myCellPhone, from_ = TwilioNUMBER)
