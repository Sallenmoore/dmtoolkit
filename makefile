
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

RUNTEST='test_dndnpc_complete'
test: clean updatepkgs
	pip install -e .
	python -m pytest -k $(RUNTEST)

RUNTEST?='test_'
tests: clean updatepkgs
	pip install -e .
	python -m pytest -s -v

