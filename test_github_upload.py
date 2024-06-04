API_token = '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'
username = 'csknyy@hotmail.com'
password = 'At@han2014'

from github import Github
import os

#g = Github(username, password)
g = Github(API_token)
repo = g.get_repo("csknyy/monster", lazy=False)
#issues = repo.get_issues(state="open")

st.write(repo)
