#!bin/bash

# function to automate project
function create() {
    if command -v python2.7 &>/dev/null; then
        if [ ! -d ~/Documents/Projects ]; then
            read -p "Project directory not exist. Do you want to create it?[Y/n]" confirm
            if [ "$confirm" = "n" ] || [ "$confirm" = "N" ]; then
                "You must create directory to continue. Bye!"
                return
            fi
            mkdir ~/Documents/Projects
        fi
        cd ~/Documents/Projects
        python ~/createProject.py $PWD $@
        
        IFS=' '
        INPUT=$@
        i=0
        for field in ${INPUT}; do
            if [ "$field" = "-p" ]; then
                j=$((i+1))
            fi
            dir=$field
            if [ "$i" = "$j" ]; then
                break
            fi
            i=$((i+1))
        done

        cd $dir
        unset j
	unset dir
    else
        echo "Python 2.7 is not installed, you can get python 2.7.x from here : https://www.python.org/downloads/"
    fi
}

function open() {
    cd ~/Documents/Projects/$1
}

function delete() {
    if [ "$1" = "" ]; then
        echo "Must include directory name, ex: delete demo"
        return
    fi
	  
    if [ ! -d ~/Documents/Projects/$1 ]; then
        echo "Directory doesn't exist"
        return
    fi

    read -p "Are you sure you want to delete this directory? [y/n] " confirm
    if [ "$confirm" = "n" ] || [ "$confirm" = "N" ]; then
        "Canceling..."
        return
    fi

    rm -rf ~/Documents/Projects/$1
    echo "Project folder deleted successfully"

    unset confirm
    read -p "Do you want to delete your github repository? [y/n] " confirm
    if [ "$confirm" = "n" ] || [ "$confirm" = "N" ]; then
        "Canceling..."
        return
    fi
    python ~/deleteProject.py  $1
}
