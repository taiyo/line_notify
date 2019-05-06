import os
import requests

def line(message):
  url = 'https://notify-api.line.me/api/notify'
  token = os.getenv('TOKEN')
  headers = {'Authorization': 'Bearer ' + token}
  payload = {'message':  message}
  requests.post(url, headers=headers, params=payload)