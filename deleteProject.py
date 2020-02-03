import sys
import os
import getpass
from termcolor import colored, cprint
from github import Github as git


options = [
    ['-p|--project-name', 'Your new project name(required)'],
    ['-l|--language',
        'Your project language(required). Available language: PHP (php), JavaScript (js)'],
    ['-t|--text-editor',
        'Your command to open your favorite text editor. Ex: code, subl, etc.(required)'],
    ['-c|--php-framework',
        'Framework that you will use. All php framework that use composer are available. Usage: -c [composer dir] or --php-framework [composer dir], ex: -c laravel/laravel'],
    ['--npm|--node-modules', 'Framework that you will use. All node modules are available. Usage: --npm [node modules] or --node-modules [node modules], ex --npm express socket.io'],
    ['-g|--github', 'To confirm this project upload to github repos or not.'],
]


def main():
    header()
    if sys.argv[1] == '':
        error()
        sys.exit(0)
    loggedin = False
    user = object
    username = ''
    while not loggedin:
        username = raw_input("Username for 'https://github.com': ")
        password = getpass.getpass(prompt="Password for 'https://" + username + "@github.com: ")
        user = git(username, password).get_user()
        try:
            user.login
            loggedin = True
        except:
            cprint("Your credentials are wrong!", "red")
    cprint("Searching your repo in github", "yellow")
    try:
        repo = user.get_repo(username + "/" + sys.argv[1])
        cprint("Repository found in https://github.com/" + username + "/" + sys.argv[1], "green")
        cprint("Deleting repository", "yellow")
        repo.delete()
        cprint("Successfully delete repo", "green")
    except:
        cprint("No repo found in github", "yellow")

    cprint("Process complete", "green")


def header():
    print('')
    print('')
    print colored(
        '     ( A       ( U      ( U  ( T T T T T    ( O O O ', 'cyan')
    print colored(
        '    ( A A      ( U      ( U      ( T      ( O    ( O ', 'cyan')
    print colored(
        '   ( A ( A     ( U      ( U      ( T      ( O    ( O ', 'cyan')
    print colored('  ( A   ( A    ( U      ( U      ( T      ( O    ( O     ',
                  'cyan'), colored(' ( P P ( Y   Y', 'yellow')
    print colored(' ( A A A A A    ( U     ( U      ( T      ( O    ( O     ',
                  'cyan'), colored(' ( P  P ( Y Y', 'yellow')
    print colored('( A       ( A     ( U U U        ( T        ( O O O  ( O)',
                  'cyan'), colored(' ( P P   ( Y', 'yellow')
    print colored('                                                         ',
                  'cyan'), colored(' ( P    ( Y', 'yellow')
    print colored('                                                         ',
                  'cyan'), colored(' ( P   ( Y', 'yellow')
    print('')
    print('')


def error():
    cprint("Usage :", "yellow")
    cprint("  create [option] [argument]\n", 'white')
    cprint("  delete [project-name]\n", 'white')
    cprint("Ex :", "yellow")
    cprint("  create -p demo -l js -t code --npm --save express socket.io\n", 'white')
    cprint("  delete demo\n", 'white')
    cprint("Options :", "yellow")
    global options
    for option in options:
        print colored('  %-20s' % option[0],
                      'green'), colored(option[1], 'white')

if __name__ == "__main__":
    main()
