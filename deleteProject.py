import sys
import os
import getpass
from termcolor import colored, cprint
from github import Github

def main():
    username = raw_input("Username for 'www.github.com': ")
    password = getpass.getpass("Password for '" + username + "'@github.com: ")
    user = Github(username, password)
    cprint("Searching your repo in github", "yellow")
    try:
        repo = user.get_repo(username + "/" + sys.argv[1])
        cprint("Repository found in github.com/" + username + "/" + sys.argv[1], "green")
        cprint("Deleting repository", "yellow")
        repo.delete()
        cprint("Successfully delete repo", "green")
    except:
        cprint("No repo found in github", "yellow")

    cprint("Process complete", "green")

if __name__ == "__main__":
    main()
