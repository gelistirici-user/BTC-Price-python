from dhooks import Webhook
import requests
import datetime
import time
import json

def config():
    with open('config.json', 'r', encoding='UTF-8') as f:
        return json.loads(f.read())

def send_hook(hook, message):
    hook = Webhook(hook)
    hook.send(message)

if __name__ == "__main__":
    print("R10 - Gelistirici")
    url = 'https://api.coindesk.com/v1/bpi/currentprice/CNY.json'
    headers = {"user-agent": "Mozilla/5.0"}
    config = config()

    while True:
        r = requests.get(url, headers=headers)
        content = json.loads(r.text)

        active_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        price = content['bpi']['USD']['rate_float']

        result = f" - BTC/USD **{price} $** değerinde. **[{active_time}]**"

        send_hook(config['webhook'], result)
        print(result.replace('**', ''))

        time.sleep(config['timeout'])


