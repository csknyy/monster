API_token = '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'

from github import Github
import os

g = Github(API_token)
repo = g.get_repo("csknyy")
issues = repo.get_issues(state="open")

st.write(issues)
