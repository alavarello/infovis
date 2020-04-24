import requests
import json
# Code copied from: https://curl.trillworks.com/

headers = {
    'authority': 'www.epicmix.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'sec-fetch-dest': 'empty',
    'x-requested-with': 'XMLHttpRequest',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.epicmix.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://www.epicmix.com/dashboard/my-dashboard.aspx',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cookie': 'fbm_148545448507002=base_domain=.epicmix.com; OptanonAlertBoxClosed=2020-04-19T18:59:05.057Z; AKA_A2=A; bm_mi=065196C3E3F74A3CC14551A2025DA443~gBjISizc1XqNPlUc/iXG/9HjdE7LP5T5ECdru/FWcZCbGmYUz6rPa4Yvy+2m7tsNzlT0kagIcjDRcHGc9BebMUtUceZYEsKYgDOBjY7yoe6LWGxPThNpzDg+959LK/eURZsexXQUmShxaHsXbRBg8f5uJA9g407j8d3z+0HKi6rFPMzH11/IwX2rezIx8xU5OYoNIaB22XdX3PONIuF4BIvMkAwPx8tq47AamiZLgQJLBrygODSH8WgjimDcKph4n8fJtMYD1i5iEN7dnxGNdw==; ak_bmsc=6BDF7DC5FD6634C1CCCB21CC7D137CB5170E572FDC7B00004205A25E55E9CB03~pl+yQb3bQEbMgt3A+YFwg+xFQFIHumbA9g6yu8ER4rXXb3wzQK1RYCSW5dchH03N9GZHKYRpQTwyFFd4o9R70hLBYJ7mzTIDV1jmHtuQehgQzY1oQPF1lZvpkgg90Q9trDg8Ub/cPsMfSID1thaWTzcjiU0q+juaH3TM7IVRGdwpcG20XSgaBLcJqZTp+wRGdgh4+XLC9B2Ka/r29nJ5vGN01MHCQOnykN87NZouxy3XYLkr2WzAeJsp47T/xSZ78m; .ASPXAUTH=C9FE08A682AE74DE018403BFDCE185D2E50014054CC731EA43C9505CB629B32282E1C5FC5CD181CEA367F5DD7FAD91A4A66534405CCF469D5825F36D1BB47D5E26E78E7396D621F10EA42B5A6B5D26605EEF01FE29B540C6413FF63F1F3370481E5204B0C0270C656D4B7B5D1F86A43A460A17B9F97621E9F6A8AF90ECF158DCE8D12C536FBA4DC54FC7DACD6C031CF26BE19E336C53A6804B3DDDFAA4738AE742A72850; ASP.NET_SessionId=j2bapeafkknukqgygc0kdnhv; ASP.NET_SessionId=j2bapeafkknukqgygc0kdnhv; OptanonConsent=isIABGlobal=false&datestamp=Thu+Apr+23+2020+18%3A15%3A28+GMT-0300+(Argentina+Standard+Time)&version=5.13.0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&hosts=&AwaitingReconsent=false&geolocation=%3B; fbsr_148545448507002=ei0Ye4G7--x1YoDXJFCf5ke_vyFAr9BNNAq5GoIEfLE.eyJ1c2VyX2lkIjoiMTAyMDg1NDQ5MjkzODAxOTAiLCJjb2RlIjoiQVFBWnlvc2hQcTl2Q3dVbU9YbFhQd2xMUlBoYk9UM3pycXNpQlNYQk9nRjhrMlMya2ViUGJzRzZCSlVNdHQ3eDNXeDJrWjBUWmRfVEtsd3NncFlqdHdYZFFIaF93RnpYem9tSDc1dm9zLVdrMjVoUG4xcFdZOGQxaHRFRG1rU2M2bU9acG84VTBIVEN1aHhYY3UxTTFUNXdrMTVfODEwM2FyTDNnMkhyS2kxTkFnUWZyOW13WEU3dlFYXzRuTzYtRmJ5aXlXQzE2ZjV1dDg5SThXUDhaWHBkclR3MjdXUnptaWdYUmZ3QmRESXpiRzhkc1lYazdXUUU2c0JEYlpRM1RzaXk2M01TcUE3NmhJbVFLcldHaE1sV29vcE54RFhBTmFud21GOFZ5dFBBQzFLRFhraDk1RWQ4NmNyeFQ5cUtCR3d6eUlyWUVyLUJzaE1HdzVjaWJCODMiLCJvYXV0aF90b2tlbiI6IkVBQUNIR2U2dzlub0JBTG1mTXVSN0lnYXg3dTlDM3lHSWdNdHJaQ1JiM3FrakFLVUF3eG44WGI3MTNDUG5Belk2WGdTQW1Idjg1djBNRVFVdXJkcWVXUFR5cUtmZ0txWHh2ODdxMmtRcUVob1pBdTNuY24wbE5RS1Q2dmx5c2FXSHJ3ZzBSVjNCdGROTUlJcE1ObFZ6TE5IcUlDWkJvTlFyczZENDlXUDZkZkoxdk4yYWlSdUF4ZTM1bHNJdk5Ua0tSWTZyRE00c0FaRFpEIiwiYWxnb3JpdGhtIjoiSE1BQy1TSEEyNTYiLCJpc3N1ZWRfYXQiOjE1ODc2NzY1Mjh9; bm_sv=EAE620E2ED6C7D2908B6E18217B37A45~JtTAxp8CYXvQbvnBt5nHYmFy7SXVi6spDgQ4GvXt7bxPZHh8Bb4TspPK3HTraDIaRXk5sRdYIxSIlOPvE6PuakG/YMlMVfkqSsDhfmLCGLCrkj6jsDN02cNWUfrtSx9Cozsrr5hW2uSLPhcOuzUV6VgyTS0MrEkSsPewBEVXssY=; s_pers=%20s_nr%3D1585594277319%7C1588186277319%3B%20s_vnum%3D1588186277313%2526vn%253D3%7C1588186277313%3B%20s_fid%3D14206C65DE4B548B-08EE6B9A894E9B60%7C1650748927788%3B%20s_invisit%3Dtrue%7C1587678727793%3B%20s_lv%3D1587676927795%7C1682284927795%3B%20s_lv_s%3DLess%2520than%25207%2520days%7C1587678727795%3B; s_sess=%20s_camp_dedupe%3DOther%2520Websitesundefinedwww.google.comn%252Fa%3B%20s_cc%3Dtrue%3B%20s_sq%3D%3B%20s_cp_persist_passtype%3D%2528RF%2529VRI%2520Employee%2520Pass%2520Media%3B%20s_cp_persist_gender%3DMale%3B%20s_cp_persist_state%3DCO%3B%20s_cp_persist_country%3DUSA%3B',
}

days = []

for possible_tag_time in range(4000, 4200):

    data = {
    'ResortId': '1',
    'TimeTagId': str(possible_tag_time)
    }
    response = requests.post('https://www.epicmix.com/VailResorts/sites/epicmix/api/Stats/LiftRides.ashx', headers=headers, data=data)
    try:
        day = json.loads(response.content)
    except:
        continue

    days.append(day)
    print(day.get('Day', None))


with open('lift.json','w') as f:
    json.dump(days, f, indent=4)
