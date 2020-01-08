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
	read -p "Are you sure want to delete it?[y/n]" confirm
	if [ "$confirm" = "n" ] || [ "$confirm" = "N" ]; then
		return
	fi
	cd ~/Documents/Projects
	rm -rf ~/Documents/Projects/$1
	python ~/deleteProject.py $1
}
