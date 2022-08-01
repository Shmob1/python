#!/usr/bin/env bash

VERSION=$(cat ../.python-version)

# ANSI escape codes 
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # no colour
ORANGE='\033[0;33m'
GREEN='\033[0;32m'  

function yn () {
    if [ -z "$1" ]; then
        echo "incorrect usage of yn ()"
        exit
    fi
    echo -en $1
    read -p " (y/n) " yn
    while true; do
        case $yn in 
            [yY] ) return 0;;
            [nN] ) return 1;;
            * ) read -p "Invalid response (y/n) " yn;;
        esac
    done
}

function add_to_bashrc {
    case "$SHELL" in
        *"bash" ) 
            rc=~/.bashrc
            touch $rc;;
        *"zsh" ) 
            rc=~/.zshrc
            touch $rc;;
        *"fish")
            echo "${RED} fish is currently not supported :("
            return 2;;
        * )
            echo "${RED} your shell is unsupported"
            return 3;;
    esac

    echo "\n###########################" >> $rc
    echo '# pyenv configruation' >> $rc
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> $rc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> $rc
    echo 'eval "$(pyenv init -)"' >> $rc
    echo '# pyenv-virtualenv configruation' >> $rc
    echo 'eval "$(pyenv virtualenv-init -)"' >> $rc
    echo '###########################' >> $rc
}

if yn "Do you want to wipe & reinstall pyenv?\n${ORANGE}This will delete all python environments${NC}"; then
    rm -rf ~/.pyenv
    curl https://pyenv.run | bash

    add_to_bashrc

    source ~/.bashrc
    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    pyenv install $VERSION
fi