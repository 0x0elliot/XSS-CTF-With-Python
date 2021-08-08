import requests
import json

with open('config.py', "r") as config_file:
    content = config_file.read()
    json_content = json.loads(content)

config = json_content
print(config)

#config = {}

#config['RECAPTCHA_PRIVATE_KEY'] = ""

#config['RECAPTCHA_PUBLIC_KEY'] = ""

def checkRecaptcha(response, secretkey):

    url = "https://www.google.com/recaptcha/api/siteverify"
    data = {"secret": secretkey, "response": response}

    r = requests.post(url, data = data)

    jsonobj = json.loads(r.text)

    if jsonobj['success']:
        return True
    
    return False
