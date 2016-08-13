#!/bin/bash


echo -e "\e[93mSimple push to git repo."
echo -e "\e[39m"

git add . 
git commit -m "update" 
git push -u origin master

