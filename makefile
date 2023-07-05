
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
	twine upload -r dist/*


updatepkgs:
	source .venv/bin/activate; pip install --upgrade pip wheel && pip install --upgrade -r requirements.txt && pip install --upgrade -r requirements_dev.txt

###### CLEANING #######

clean:
	rm -rf .pytest_cache

###### TESTING #######

RUNTEST?='test_'
test: clean updatepkgs
	source .venv/bin/activate; python -m pytest

