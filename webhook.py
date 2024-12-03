from flask import Flask, request
from pprint import pprint
app= Flask(__name__)

from login import auth_token
import os
from dotenv import load_dotenv
load_dotenv()




@app.route('/',methods=['POST'])
def webhook():
    req=request.get_json(force=True)
    sessionInfo=req.get('sessionInfo',{})
    session=sessionInfo.get('session',{})
    pprint(req)
    email=os.getenv("email")  #Enter custom email id and password
    password=os.getenv("password") #Enter custom email id and password

    info=auth_token(email, password)
    fname=info.get('first_name')
    lname=info.get('last_name')
    is_paddiAi_user=info.get('is_paddiAi_user')
    phone_number=info.get('phone_number')
    email=info.get('email')
    city=info.get('city')
    token=info.get('token')
    if is_paddiAi_user==1:
        regularUser=True
    else:
        regularUser=False

    response={
        "sessionInfo":{"session": session,
                    "parameters": {
                        "userName":"Pratik",
                        "regularUser":True,
                        "userPhoneNumber":phone_number,
                        "userEmail":email,
                        "userToken":token,
                        "city":city
                    }
                    }
    }


    return response


if __name__=="__main__":
    app.run(debug=True, port=8080)