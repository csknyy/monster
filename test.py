#import os
#import streamlit as st
#from github import Github

# Load GitHub access token from environment variable
#token = os.environ["GITHUB_TOKEN"] = "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"

#import requests
#url = 'https://github.com/csknyy/monster/blob/b0555c860210870ef7eff781899f6194fc1b4fec/update_this.txt'
#page = requests.get(url)
#st.write(page.text)

import base64
import requests
import streamlit as st

user = 'csknyy'
repo_name = 'monster'
path_to_file = 'update_this.txt'
url = f'https://api.github.com/repos/{user}/{repo_name}/contents/{path_to_file}'
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    content = base64.decodestring(req['content'])
    st.write(content)
else:
    st.write('Content was not found.')
