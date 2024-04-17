
.PHONY: all package clean deepclean tests

include .env
export

all: test clean run start

CONTAINERS=$$(sudo docker ps -a -q)

package: clean
	python -m build
	python -m pip install --upgrade twine wheel setuptools
	twine check dist/*
	twine upload dist/*

###### CLEANING #######

clean:
	rm -rf .pytest_cache .coverage dist

###### TESTING #######
updatepkgs:
	pip install --upgrade pip wheel && pip install --upgrade -r requirements.txt && pip install --upgrade -r requirements_dev.txt
	pip install -e .

tests: clean updatepkgs
	python -m pytest




