from github import Github

g = Github('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')

username = 'csknyy'
repo-name = 'monster'
path_to_file = 'update_this.csv'

repo = g.get_repo('sandbox/gh_api')

input_text = st.text_input("Enter input")

repo.create_file(path_to_file, 'upload csv', input_text, branch=repo-name)
