#!/bin/bash

clear

#Copy the details to a temp folder
rm -R ../package/
mkdir ../package/

# NOOOOO! don't do this!  Set ONLY the bin folder as executable 
chmod -R 755 *

cp -r ./src ../package/brisbane_ferries/ 
cd ../package/

#remove Git Files
find . -name ".DS_Store" -print0 | xargs -0 rm -rf
find . -name "._*" -print0 | xargs -0 rm -rf
find . -name "*.pyc" -print0 | xargs -0 rm -rf
find . -name "*._logo*" -print0 | xargs -0 rm -rf
find . -name "*._ap*" -print0 | xargs -0 rm -rf
 
tar -czf brisbane_ferries.tar.gz brisbane_ferries/
ls