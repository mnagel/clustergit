#! /bin/bash

cd $(dirname "$0")
touch demo
rm -rf demo
mkdir demo
cd demo

mkdir repo1
cd repo1
git init
cd ..

mkdir repo2
cd repo2
git init
git checkout --orphan otherbranch
cd ..

mkdir repo3
cd repo3
git init
touch a b c
git add .
git commit -a -m "nevermind"
cd ..

mkdir arepo
cd arepo
git init
touch a b c
git add .
git commit -a -m "nevermind"
cd ..

mkdir norepo

git clone git@github.com:mnagel/clustergit
cd clustergit
touch a b c
git add .
git commit -a -m "nevermind"
cd ..

git clone git@github.com:mnagel/clustergit clustergit-clean

## now run
# cd demo
# clustergit --warn-unversioned
# clustergit --pull
