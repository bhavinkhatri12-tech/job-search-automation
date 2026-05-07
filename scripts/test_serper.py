import os, requests
key=os.environ.get('SERPER_API_KEY')
if not key:
    try:
        with open('.env') as f:
            for line in f:
                if line.strip().startswith('SERPER_API_KEY='):
                    key=line.strip().split('=',1)[1]
    except:
        key=None
print('Using Serper key:', 'FOUND' if key else 'MISSING')
if key:
    url='https://google.serper.dev/search'
    headers={'X-API-KEY': key}
    payload={'q':'HR jobs in Nova Scotia site:indeed.ca','num':1}
    try:
        r=requests.post(url,json=payload,headers=headers,timeout=15)
        print('Status:', r.status_code)
        print('Response snippet:', r.text[:1000])
    except Exception as e:
        print('Request error:', e)
else:
    print('No key to test')
