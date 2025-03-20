import os
import requests
import json
from dotenv import load_dotenv
load_dotenv()


WHATSAPP_API_KEY = os.environ.get('WHATSAPP_API_KEY')
WHATSAPP_NUMBER = os.environ.get('WHATSAPP_NUMBER')
WHATSAPP_TO = os.environ.get('WHATSAPP_TO')


def run():

    with open('../res/verses.json', 'r') as json_data:
        # https://www.youtube.com/watch?v=-51jxlQaxyA
        verses = json.load(json_data)
        json_data.close()

    print("Running Whatsapp Bible")
    index = 0
    verse = verses[index % len(verses)]
    text = f"#Stay Blessed\n\n${verse.text}\n\n*${verse.title}*"
    image = verse.image

    # https://developers.facebook.com/docs/whatsapp/cloud-api/messages/image-messages
    url = f"https://graph.facebook.com/v22.0/{WHATSAPP_NUMBER}/messages"
    headers = {'Authorization': f'Bearer {WHATSAPP_API_KEY}'}
    body = {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_TO,
        "type": "image",
        "image": {
            "link": image,
            "caption": text,
        }
    }

    # Make API call - to Whatsapp Cloud
    try:
        res = requests.post(url=url, data=body, headers=headers)
        print(res.json())
    except:
        print('Something went wrong')


if __name__ == '__main__':
    run()
