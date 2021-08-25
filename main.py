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




    





a = """def get_timeout():
    with open('timeout.txt', 'r', encoding='UTF-8') as f:
        content = f.read()
        return int(content)

hook = Webhook('webhhook uri')
timeout = get_timeout()

while True:
    now = datetime.datetime.now()
    active_time = now.strftime("%Y-%m-%d %H:%M:%S")

    data = get_data('https://api.coindesk.com/v1/bpi/currentprice/CNY.json')

    USD = data['bpi']['USD']['rate_float']

    content = f" - BTC/USDT **{USD} $** değerinde. **[{active_time}]**"

    hook.send(content)
    print(f'Gönderildi. {active_time}')

    time.sleep(timeout)"""
