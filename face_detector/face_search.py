import requests
import webbrowser
import sys 

imagePath = sys.argv[1]
searchUrl = 'http://www.google.hr/searchbyimage/upload'
multipart = {'encoded_image': (imagePath, open(imagePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
webbrowser.open(fetchUrl)