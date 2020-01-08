# !bin/python2.7
import sys
import os
import subprocess
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
    option(sys.argv)
    # print("Author: afikrim <afikrim10@student.ub.ac.id>")


def option(argv):
    i = 0
    project_name = language = composer_repos = text_editor = ''
    node_package = []
    git_repo = False
    while i != len(argv):
        if argv[i] in ['-p', '--project-name']:
            if argv[i + 1] == '':
                error()
            project_name = argv[i + 1]
        elif argv[i] in ['-l', '--language']:
            if argv[i + 1] == '':
                error()
            language = argv[i + 1]
        elif argv[i] in ['-c', '--php-framework']:
            if argv[i + 1] == '':
                error()
            composer_repos = argv[i + 1]
        elif argv[i] in ['--npm', '--node-modules']:
            j = 1
            while (i + j) < len(argv) and argv[i + j] not in '-p -l -c -t -g --project-name --language --php-framework --text-editor --github':
                node_package.append(argv[i + j])
                j += 1
        elif argv[i] in ['-t', '--text-editor']:
            if argv[i + 1] == '':
                error()
            text_editor = argv[i + 1]
        elif argv[i] in ['-g', '--github']:
            git_repo = True
        i += 1

    run_command(project_name, language, composer_repos,
                node_package, text_editor, git_repo)


def run_command(project_name='', language='', composer_repos='', node_package=[], text_editor='', git_repo=False):
    hasPhp = object
    hasMysql = object
    hasComposer = object
    hasNodejs = object
    if project_name == '' or language == '' or text_editor == '':
        error()
        sys.exit(1)
    if language.lower() == 'php':
        hasPhp = hasPhp()
        hasMysql = hasMysql()
        if not hasPhp or not hasMysql:
            cprint("Look like you haven't install apache server on your machine, you can install an application for your apache server from here : https://www.apachefriends.org/index.html")
            sys.exit(1)

        if composer_repos != '':
            if not hasComposer():
                cprint(
                    "Look like you haven't install composer. You can get it from here : https://getcomposer.org/download/")
                sys.exit(1)
            install_framework(project_name, composer_repos, '')
        else:
            cprint("Creating project without framework", 'yellow')
            try:
                os.system(
                    "mkdir " + sys.argv[1] + '/' + project_name + ";cd " + project_name+";touch index.php"+";touch README.md")
                cprint("Successfully create new directory.", 'yellow')
            except:
                cprint("Something went wrong. Closing program")
                sys.exit(1)

    if language.lower() in ['js', 'javascript']:
        os.system("mkdir " + sys.argv[1] + '/' + project_name)
        if not hasNodejs():
            cprint("Look like you haven't install nodejs on your machine, you can get it from here : https://nodejs.org/en/download/")
            sys.exit(1)

        if node_package != []:
            install_framework(project_name, '', node_package)
        else:
            cprint("Creating project without framework", 'yellow')
        try:
            os.system(
                "cd " + sys.argv[1] + '/' + project_name + ";touch index.js" + ";touch README.md")
            cprint("Successfully create new directory.", 'yellow')
        except:
            cprint("Something went wrong. Closing program")
            sys.exit(1)
    if git_repo:
        cprint("Processing to github...", "yellow")
        create_repos(project_name)
    cprint("Opening text editor", 'yellow')
    os.system(text_editor + " " + sys.argv[1] + '/' + project_name)
    sys.exit()


def install_framework(project_name='', composer_repos='', node_package=[]):
    if composer_repos != '':
        os.system("cd " + sys.argv[1] + ";composer create-project " +
                  composer_repos + " " + project_name)
    elif node_package != []:
        packages = ''
        for p in node_package:
            packages += p + " "
        os.system("cd " + sys.argv[1] + '/' +
                  project_name + ";npm init; npm i " + packages)


def create_repos(project_name=''):
    loggedin = False
    user = object
    while not loggedin:
        username = raw_input("Username: ")
        password = getpass.getpass(prompt="Password: ")
        user = git(username, password).get_user()
        try:
            user.login
            loggedin = True
        except:
            cprint("Your credentials are wrong!", "red")
    repo = user.create_repo(project_name)
    cprint("Successfully create repository", "green")


def hasPhp():
    try:
        os.system("php -v")
        return True
    except:
        return False


def hasMysql():
    try:
        os.system("mysql --version")
        return True
    except:
        return False


def hasComposer():
    try:
        os.system("composer")
        return True
    except:
        return False


def hasNodejs():
    try:
        os.system("node -v")
        return True
    except:
        return False


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
