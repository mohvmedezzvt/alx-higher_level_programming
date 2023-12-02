#!/usr/bin/python3
"""Lists 10 commits (from the most recent to oldest) of a GitHub repository.
"""
import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    r = requests.get(url)
    r.raise_for_status()
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get('sha', 'Unknown SHA')
        author_name = commit.get('commit', {}).get('author', {}).get(
                                                            'name',
                                                            'Unknown Author')
        print(f"{sha}: {author_name}")
