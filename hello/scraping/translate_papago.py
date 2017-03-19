from requests import Request, Session

def translate_with_papago(line, source='en', target='ko'):

    headers = {
        'X-Naver-Client-Id': '5vdKa3fN5_McdR7oz3at',
        'X-Naver-Client-Secret': 'nmdxT9lVWz',
    }

    data = {
        'source': 'en',
        'target': 'ko',
        'text': "But, before you get started on that, let's talk about some of the other kinds"}
    url = 'https://openapi.naver.com/v1/language/translate'

    s = Session()

    req = Request('POST', url, data=data, headers=headers)
    prepared = req.prepare()
    res = s.send(prepared)

    try:
        res = s.send(prepared)
    except Exception as err:
        print(err)
        return ('')
    try:
        data = res.json()['message']['result']['translatedText']
        return data
    except Exception as err:
        return ('')