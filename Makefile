help:
	@sed -ne '/@sed/!s/## //p' $(MAKEFILE_LIST)

install: ## Install the complete service locally
	pip3 install -e ."[dev]"
	cp .env.example .env

run: ## Run the service locally
	python3 app.py

docker: ## Run the service in a docker container (always builds)
	docker-compose up -d --build

lint: ## Lint the entire project
	pylint withbond/*.py	
