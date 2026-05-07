import os
print('ENV SERPER_API_KEY via os.environ=', os.environ.get('SERPER_API_KEY'))
try:
    with open('.env') as f:
        print('\n.env contents:')
        print(f.read())
except Exception as e:
    print('read .env error', e)
