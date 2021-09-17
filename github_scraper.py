from github import Github
from pathlib import Path
from collections import defaultdict
import requests
import csv
import re


GITHUB_TOKEN = "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"

g = Github(GITHUB_TOKEN)

# Get the Pull Requests
# pulls = g.get_repo('slaytr/beel.dev').get_pulls()
# for pull in pulls:
#     print(pull.changed_files)
#     print(pull.additions)
#     print(pull.deletions)
#     print(pull.user.login)

# pulls = g.get_repo('dabit3/write-with-me').get_pulls()
# for pull in pulls:
#     print(pull.diff_url)
#
# # https://patch-diff.githubusercontent.com/raw/dabit3/write-with-me/pull/3.diff
#
# file_directory = "pulls"
#
# response = requests.get('https://patch-diff.githubusercontent.com/raw/dabit3/write-with-me/pull/3.diff')
#
# full_path = "https://patch-diff.githubusercontent.com/raw/dabit3/write-with-me/pull/3.diff"
#
# github_path = "dabit3/write-with-me"
# with open(f'{file_directory}/{github_path}', 'w') as f:
#     f.write(response.text)

# repos = [
#     "dabit3/write-with-me"
# ]

repos = [
    "slaytr/beel.dev",
    # "facebook/react",
    "taniarascia/takenote",
    "sanyuan0704/react-cloud-music",
    "karlhadwen/todoist",
    "paulhoughton/mortgage",
    "xjh22222228/tomato-work",
    "dabit3/write-with-me",
    "oldboyxx/jira_clone",
    "withspectrum/spectrum",
    "rahuldkjain/github-profile-readme-generator",
    "ritz078/moose",
    "codelitdev/courselit",
    "chaoming/fireact",
]

with open('pulls/data_without_react.csv', 'a', newline='') as f:
    csv_file = csv.writer(f)
    for repo in repos:
        pulls = g.get_repo(repo).get_pulls()
        for pull in pulls:
            line = [repo, pull.user.login, pull.id, pull.number, pull.changed_files, pull.additions, pull.deletions]
            if "dependabot" not in pull.user.login:
                csv_file.writerow(line)

