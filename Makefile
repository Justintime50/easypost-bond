VIRTUALENV := python3 -m venv

## help - Display help about make targets for this Makefile
help:
	@cat Makefile | grep '^## ' --color=never | cut -c4- | sed -e "`printf 's/ - /\t- /;'`" | column -s "`printf '\t'`" -t

## venv - Install the virtual environment
venv:
	$(VIRTUALENV) ~/.venv/withbond/
	ln -snf ~/.venv/withbond/ venv
	venv/bin/pip install -e ."[dev]"

## install - Install the complete service locally
install: | venv
	cp .env.example .env

## clean - Remove the virtual environment and clear out .pyc files
clean:
	rm -rf ~/.venv/withbond/ venv
	find . -name '*.pyc' -delete
	find . -name '.env' -delete

## run - Run the service locally
run:
	venv/bin/python app.py

## docker - Run the service in a docker container (always builds)
docker:
	docker-compose up -d --build

## lint - Lint the project
lint:
	venv/bin/pylint withbond/*.py

## test - Test the project
test:
	venv/bin/python -m unittest

.PHONY: help install clean run docker lint test 
