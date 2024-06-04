API_token = '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'
username = 'csknyy@hotmail.com'
password = 'At@han2014'

from github import Github
import os

g = Github(username, password)
repo = g.get_repo("csknyy/monster", lazy=False)
#issues = repo.get_issues(state="open")

st.write(repo)
