import requests

headers = {
    'X-Naver-Client-Id': '5vdKa3fN5_McdR7oz3at',
    'X-Naver-Client-Secret': 'nmdxT9lVWz',
}

url = 'https://openapi.naver.com/v1/search/blog.json?query=kitri'
res = requests.get(url, headers=headers)

res_json = res.json()

for items in res_json['items']:
    print(items['title'])

