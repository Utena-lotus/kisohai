from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# APIキーの情報

key = '57e28173b09910751cab95b1a13e0fac'
secret = '0a4d00e9edac35da'
waitTime = 1

#保存フォルダの指定
noodlesname = sys.argv[1]
savedir = './' + noodlesname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = noodlesname,
    perPage = 400,
    media = 'photos',
    sort = 'relevance',
    safeSearch =1,
    extras = 'url_q, licence'
)

photos = result['photos']
# 返り値を表示する
# pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q,filepath)
    time.sleep(waitTime)