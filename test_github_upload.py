API_token = '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'

from github import Github
import os

token = os.getenv('GITHUB_TOKEN', API_token)
g = Github(token)
repo = g.get_repo("csknyy/monster")
issues = repo.get_issues(state="open")

st.write(issues)
