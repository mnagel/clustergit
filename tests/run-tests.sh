#! /bin/bash

DIR=$(dirname "$0")

rm -r cover .coverage
nosetests --with-coverage --cover-html
pylint --rcfile .pylintrc src > pylint.html

rm -r apidoc
sphinx-apidoc . --full -H clustergit -A mn -V 1 -R 1 -o apidoc
cd apidoc
vim -c ":%s/#sys.path.insert(0, os.path.abspath('.'))/sys.path.insert(0, os.path.abspath('..'))/" -c 'x' conf.py
make html > output.log 2> errors.log
echo "output saved to output.log and errors.log to stop spam"
cd ..

if [ $# == 0 ]; then
	echo $# parameters, going interactive
	echo "opening coverage report in browser"
	echo "opening lint report in browser"
	xdg-open "cover/index.html"
	xdg-open "pylint.html"
	xdg-open "apidoc/_build/html/index.html"
else
	echo $# parameters, going non-interactive
fi
