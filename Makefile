.PHONY: test

setup:
	pip install -U pip
	pip install -r requirements.txt

setup-dev: setup
	python setup.py develop
	pip install -r requirements-dev.txt

test:
	PYTHONPATH=NathanJamesToolbox py.test
