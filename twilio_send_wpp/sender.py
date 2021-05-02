from twilio.rest import Client
import os
os.environ['TWILIO_ACCOUNT_SID'] = 'AC7f8465727505d9060bf41903bb8e47ab'
os.environ['TWILIO_AUTH_TOKEN'] = 'f092c0f1accc19c951467979ad90392f'

# as credenciais são recuperadas das variáveis de ambiente TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN
client = Client()

# esse é o numero de teste da sandbox da Twilio
from_whatsapp_number='whatsapp:+14155238886'
# substitua esse número com o seu próprio número do Whatsapp
to_whatsapp_number='whatsapp:+5531993153549'

client.messages.create(body='Ahoy, world!',
                      from_=from_whatsapp_number,
                      to=to_whatsapp_number)

