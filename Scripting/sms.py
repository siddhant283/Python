from twilio.rest import Client 
 
account_sid = 'AC77e781b1587f66cba95ddb96bfcfb7c0' 
auth_token = 'efaa68d6c13e25214803e8cccd501a05' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG7f6c99b07e316e3ac88daffeb0a269e2', 
                              body='heloooo',      
                              to='+917984132784' 
                          ) 
 
print(message.sid)