import requests
import json
def main():
    resp = requests.get('hhtp://www.baidu.com', python='python')
    data_model = json.loads(resp.text)
    for new in data_model['neslist']:
        print(new['title'])

if __name__ == '__main__':
    main()