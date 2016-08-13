#!/bin/bash


echo -e "\e[93mSimple push to git repo."
echo 1st argument: ${args[0]}
echo "you passed me" ""$*""
echo "you passed me" $@
echo -e "\e[39m"

git add . 
git commit -m "$@" 
git push -u origin master

