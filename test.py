import os
import streamlit as st
from github import Github

# Load GitHub access token from environment variable
#token = os.environ["GITHUB_TOKEN"] = "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"

import requests
#url = 'https://github.com/csknyy/monster/blob/b0555c860210870ef7eff781899f6194fc1b4fec/update_this.txt'
url = 'https://raw.githubusercontent.com/csknyy/monster/blob/b0555c860210870ef7eff781899f6194fc1b4fec/update_this.txt'
page = requests.get(url)
st.write(page.text)
