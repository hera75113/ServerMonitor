import requests


def monitor_website(url):
    r = requests.get(url)
    
    if r.status_code == 200:
        print(r.status_code)
        return r.url, r.status_code, r.reason
    elif r.status_code != 200:
        print("RESPONSE FAILED")
        return r.url, r.status_code, r.reason


def tracert(): #TODO
    pass