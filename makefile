
.PHONY: all package startdb create-network clean deepclean tests test testauto testapp

include .env
export

all: test clean run start

CONTAINERS=$$(sudo docker ps -a -q)

package: clean
	python -m build
	python -m pip install --upgrade twine wheel setuptools
	twine check dist/*
	twine upload dist/*

updatepkgs:
	pip install --upgrade pip wheel && pip install --upgrade -r requirements.txt && pip install --upgrade -r requirements_dev.txt
	

###### CLEANING #######

clean:
	rm -rf .pytest_cache .coverage dist

###### TESTING #######

testinit: clean updatepkgs
	pip install -e .

RUNTEST='test_'
test:
	pip install -e .
	python -m pytest -k $(RUNTEST)

tests:
	python -m pytest

testfull:testinit tests



