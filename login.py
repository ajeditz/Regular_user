import requests
from pprint import pprint
import  os

from dotenv import load_dotenv
load_dotenv()

email=os.getenv("email")
password=os.getenv("password")

def auth_token(email,password):
    url = "https://gopaddibackend.vgtechdemo.com/api/v1/auth/login?"
    payload = {
        "email": email,
        "password": password
    }
    response = requests.request("POST", url, json=payload)
    response_json=response.json()
    data=response_json.get('data')
    token=data.get('token')
    userDetails=data.get('user_details')
    city=userDetails.get('city',{}).get('name')
    email=userDetails.get('email')
    first_name=userDetails.get('first_name')
    last_name=userDetails.get('last_name')
    is_paddiAi_user=userDetails.get('is_paddiAi_user')
    phone_number=userDetails.get('phone_number')
    final_response={
        "first_name":first_name,
        "last_name":last_name,
        "is_paddiAi_user":is_paddiAi_user,
        "phone_number":phone_number,
        "email":email,
        "city":city,
        "token":token,
    }

    

    return final_response

if __name__=="__main__":
    pprint(auth_token(email, password))

# import requests

# url = "https://gopaddibackend.vgtechdemo.com/api/v1/auth/login"

# payload = {
#     "email": "dawangepratik13@gmail.com",
#     "password": "Pratik@123"
# }
# response = requests.request("POST", url, json=payload)

# print(response.text)