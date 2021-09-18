#! /bin/bash

cd $(dirname "$0")
touch demo
rm -rf demo
mkdir demo
pushd demo

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

popd

##
# Demo multi-directory support
##
cd $(dirname "$0")
touch demo2
rm -rf demo2
mkdir demo2
pushd demo2

mkdir repo1_in_demo2
cd repo1_in_demo2
git init
cd ..

mkdir repo2_in_demo2
cd repo2_in_demo2
git init
git checkout --orphan otherbranch
cd ..

mkdir repo3_in_demo2
cd repo3_in_demo2
git init
touch a b c
git add .
git commit -a -m "nevermind"
cd ..

popd

## now run
# clustergit -d demo -d demo2 --warn-unversioned
# clustergit -d demo -d demo2 --pull
