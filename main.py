from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import uvicorn
import requests
import generator
import re


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/config", response_class=PlainTextResponse)
def test_route():
    session = requests.Session()

    # Creating Account
    headers = {
        'authority': 'www.aghayevpn.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://www.aghayevpn.com',
        'referer': 'https://www.aghayevpn.com/clientarea/register',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = {
        'countryCode': '98',
        'phone': '9111111111',
        'email': generator.generate() + "@gmail.com",
        'password': '123m321M@',
    }

    response = session.post('https://www.aghayevpn.com/clientarea/register', headers=headers, data=data)

    # Activating Trial
    headers = {
        'authority': 'www.aghayevpn.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'dnt': '1',
        'origin': 'https://www.aghayevpn.com',
        'referer': 'https://www.aghayevpn.com/clientarea/subscriptions',
        'sec-ch-ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    }

    data = {
        'package_id': '1',
    }

    response = session.post('https://www.aghayevpn.com/clientarea/subscriptions', headers=headers, data=data)
    print(response)

    # Getting Link
    page = session.get("https://www.aghayevpn.com/clientarea/subscriptions")
    sub_link = re.search(r"https://get.novinshop.enterprises/generic...=\d*", page.text)
    subscription = requests.get(sub_link.group())
    return subscription.text

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)