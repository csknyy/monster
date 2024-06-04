from github import Github
import os

API_token = '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'
username = 'csknyy@hotmail.com'
password = 'At@han2014'

g = Github(login_or_token=username,password=password)
#g = Github(API_token)
repo = g.get_repo("csknyy/monster", lazy=False)
#issues = repo.get_issues(state="open")

st.write(repo)
