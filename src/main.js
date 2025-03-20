require('dotenv').config()
const axios = require('axios');
const verses = require('../res/verses.json');

// Get Environment Variables
const WHATSAPP_API_KEY = process.env.WHATSAPP_API_KEY;
const WHATSAPP_NUMBER = process.env.WHATSAPP_NUMBER;
const WHATSAPP_TO = process.env.WHATSAPP_TO;


async function run() {
    console.log('Running Whatsapp Message')

    const index = (new Date().getMonth() * 31) + new Date().getDate()
    const verse = verses[index % verses.length];
    const text = `#Stay Blessed\n\n${verse.text}\n\n*${verse.title}*`
    const image = verse.image;

    // https://developers.facebook.com/docs/whatsapp/cloud-api/messages/image-messages
    const url = `https://graph.facebook.com/v22.0/${WHATSAPP_NUMBER}/messages`
    const headers = { 'Authorization': 'Bearer ' + WHATSAPP_API_KEY }
    const body = {
        "messaging_product": "whatsapp",
        "to": WHATSAPP_TO,
        "type":"image",
        "image": {
            "link": image,
            "caption": text,
        }
    }

    // Make API call - to Whatsapp Cloud
    try {
        const res = await axios.post(url, body, { headers })
        console.log(res.data);
    } catch (e) {
        console.log(e.response.data)
    }
}

run();