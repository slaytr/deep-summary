from github import Github
from pathlib import Path
from collections import defaultdict
import requests
import csv
import re


GITHUB_TOKEN = "<token here>"

g = Github(GITHUB_TOKEN)

# print([repo for repo in g.get_user().get_repos()])
pulls = g.get_repo('slaytr/beel.dev').get_pulls()
for pull in pulls:
    print(pull.user)
    print(pull.base)
    print(pull.head)

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

repos = [
    "dabit3/write-with-me"
]

# repos = [
#     "facebook/react",
#     "taniarascia/takenote",
#     "sanyuan0704/react-cloud-music",
#     "karlhadwen/todoist",
#     "paulhoughton/mortgage",
#     "xjh22222228/tomato-work",
#     "dabit3/write-with-me",
#     "oldboyxx/jira_clone",
#     "withspectrum/spectrum",
#     "rahuldkjain/github-profile-readme-generator",
#     "ritz078/moose",
#     "codelitdev/courselit",
#     "chaoming/fireact",
# ]

for repo in repos:
    # Create Repo PR Directory
    directory = "pulls/" + repo
    Path(directory).mkdir(parents=True, exist_ok=True)

    # Check file does not already exist

    # Send Request for Diff
    # diff_url = "https://patch-diff.githubusercontent.com/raw/dabit3/write-with-me/pull/3.diff"
    # diff_url = "https://patch-diff.githubusercontent.com/raw/dabit3/write-with-me/pull/4.diff"
    #
    # # Get all file extensions, remove line count, added line count, line count difference, number of changed files
    # response = requests.get(diff_url)
    # print(response.text)
    #
    # file_ext_dict_negative = defaultdict(int)
    # file_ext_dict_positive = defaultdict(int)
    #
    # # get file extensions
    # negative_re = re.compile('^---.*(\.[^.]+)$^---', flags=re.MULTILINE)
    # matches = negative_re.search(response.text)
    # if matches:
    #     for match in matches.groups():
    #         file_ext_dict_negative[match] += 1
    #

    # print(file_ext_dict_negative.items())

    # get positive file changes
    # positive_re = re.compile('^\+\+\+.*(\.[^\.]+)$', flags=re.MULTILINE)
    # matches = positive_re.search(response.text)
    # if matches:
    #     for match in matches.groups():
    #         print(match)
