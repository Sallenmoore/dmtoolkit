
.PHONY: all package startdb create-network clean deepclean tests test testauto testapp

include .env
export

all: test clean run start

CONTAINERS=$$(sudo docker ps -a -q)

package:
	rm -rf dist
	python -m build
	python -m pip install --upgrade twine
	twine check dist/*
	twine upload -r testpypi dist/*


###### CLEANING #######

clean:
	rm -rf .pytest_cache

###### TESTING #######

RUNTEST?='test_'
test: clean
	python -m pytest $(RUNTEST)

tests: clean 
	pip install --no-cache-dir --upgrade pip wheel
	pip install -r ./requirements.txt
	python -m pytest

