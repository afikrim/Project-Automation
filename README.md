```

     ( A       ( U      ( U  ( T T T T T    ( O O O 
    ( A A      ( U      ( U      ( T      ( O    ( O 
   ( A ( A     ( U      ( U      ( T      ( O    ( O 
  ( A   ( A    ( U      ( U      ( T      ( O    ( O       ( P P ( Y   Y
 ( A A A A A    ( U     ( U      ( T      ( O    ( O       ( P  P ( Y Y
( A       ( A     ( U U U        ( T        ( O O O  ( O)  ( P P   ( Y
                                                           ( P    ( Y
                                                           ( P   ( Y


Usage :
  auto [option] [argument]

Options :
  -p|--project-name    Your new project name(required)
  -l|--language        Your project language(required). Available language: PHP (php), JavaScript (js)
  -t|--text-editor     Your command to open your favorite text editor. Ex: code, subl, etc.(required)
  -c|--php-framework   Framework that you will use. All php framework that use composer are available. Usage: -c [composer dir] or --php-framework [composer dir], ex: -c laravel/laravel
  --npm|--node-modules Framework that you will use. All node modules are available. Usage: --npm [node modules] or --node-modules [node modules], ex --npm express socket.io
  -g|--github          To confirm this project upload to github repos or not.

```
# Project-Automation
Custom command to automate you create your project

# About
This is a shell application that help you make your project really easy. This project run well on linux machine but i don't know this project also work on other OS or not.

# How?
## Requirement
Before you start using this project please install python 2.7 first. After you guys install it, please install this python modules, termcolor and pygithub. You can install it by type this in your shell
```
pip install termcolor
pip install PyGithub
```
After you guys install it, you can go to root directory by run this command
```
cd
```
Then give permission to this shell program to execute by run this command
```
chmod +x /path/to/file.sh

# example, chmod +x ~/Project-Automation/.my_custom_commands.sh
```
Also move the python script to your root by run this command
```
mv /path/to/file ~/

# example, mv ~/Project-Automation/createProject.py ~/
```
Then don't forget to add this to your .bashrc file
```
source /path/to/file

# example, source ~/Project-Automation/.my_custom_commands.sh
```
Finally you can write ```auto``` in your shell to use this automation.
