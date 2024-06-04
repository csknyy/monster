from github import Github
import os

token = os.getenv('GITHUB_TOKEN', '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')
g = Github(token)
repo = g.get_repo("csknyy/monster")
issues = repo.get_issues(state="open")

st.write(issues)
