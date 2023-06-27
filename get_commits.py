import requests
import os

#This function will get the commits from the vscode repo which will be used as input to the OpenAI model
def get_commits_from_vscode_repo():
    url = "https://api.github.com/repos/microsoft/vscode/commits"
    headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "Your-User-Agent"
    }

    response = requests.get(url, headers=headers)
    response_json = response.json()

    if response.status_code == 200:
        commits = response_json  # Extract the commits from the response
        return commits
    else:
        print(f"Error: {response.status_code} - {response_json['message']}")
        return None

# Get commits from the vscode repo
commits = get_commits_from_vscode_repo()

# Write commits to a text file
with open('commits.txt', 'w') as f:
    for commit in commits:
        f.write(commit['commit']['message'] + "\n")







