from github import Github
import os

import base64
import requests
import streamlit as st

user = 'csknyy'
repo_name = 'monster'
path_to_file = 'update_this.csv'
url = f'https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}'
req = requests.get(url)

st.write(req)

#if req.status_code == requests.codes.ok:
req = req.json()  # the response is a JSON
# req is now a dict with keys: name, encoding, url, size ...
# and content. But it is encoded with base64.
content = base64.b64decode(req['content'])
jsonString = content.decode('utf-8')
#finalJson = json.loads(jsonString)
st.write(jsonString)
#else:
#    st.write('Content was not found.')
