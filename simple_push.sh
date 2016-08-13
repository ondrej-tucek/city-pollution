#!/bin/bash

# Usage
# ./simple_push fix

echo -e "\e[93mSimple push to git repo."
echo -e "\e[39m"

git add . 
git commit -m "$@" 
git push -u origin master

