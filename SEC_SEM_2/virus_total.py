import json
import requests
import pandas as pd

api_url = 'https://www.virustotal.com/vtapi/v2/file/scan'
params = dict(apikey='cc16c6aea3a851f8fc4f42848a8d974b73102674ab451e0bd52b1cd1cb77e92c')
with open('SEC_SEM_1/Перечень сформированных угроз.xlsx', 'rb') as file:
    files = dict(file=('SEC_SEM_1/Перечень сформированных угроз.xlsx', file))
    response = requests.post(api_url, files=files, params=params)
if response.status_code == 200:
    result=response.json()
    # print(json.dumps(result, sort_keys=False, indent=4))

api_url = 'https://www.virustotal.com/vtapi/v2/file/report'
params = dict(apikey='cc16c6aea3a851f8fc4f42848a8d974b73102674ab451e0bd52b1cd1cb77e92c', resource='e36327216f06770cae69d087fe5a95ce6fb5a3ca5dd698d1133f3cb41347313b-1711802764')
response = requests.get(api_url, params=params)
if response.status_code == 200:
    result=response.json()
    print(json.dumps(result, sort_keys=False, indent=4))
    total = []
    for key in result['scans']:
        totli = {
        'Antivirus' : key, 
        'Detected' : result['scans'][key]['detected'],
        'Version' : result['scans'][key]['version'],
        'Update' : result['scans'][key]['update'],
        'Result' : result['scans'][key]['result']
        }
        total.append(totli)
    df = pd.DataFrame(total)
    df.to_csv('SEC_SEM_2/V_T.csv')