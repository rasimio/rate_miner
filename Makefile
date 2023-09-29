files_to_fmt ?= app pkg # enumeration of * .py file storage or folders is required.
files_to_check ?= app  # enumeration of * .py files storage or folders is required.

ifeq (run,$(firstword $(MAKECMDGOALS)))
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  $(eval $(ARGS):;@:)
endif

## Default target
.DEFAULT_GOAL := serve

## Build api miner containers
docker_up:
	docker-compose up --build

## Start project without miner
.PHONY: run
run: install_requirements
	: # Activate venv and run flask miner
	poetry run python run.py $(ARGS)


## Rule for install dependencies
install_requirements:
	: # Activate venv and install dependencies inside
	pip install poetry && poetry install --no-dev



## Format all
fmt: format
format: remove_imports isort black docformatter add-trailing-comma


## Check code quality
chk: check
lint: check
check: flake8 black_check docformatter_check safety bandit

## Migrate repository
migrate:
	python -m scripts.migrate

## Rollback migrations in repository
migrate-rollback:
	python -m scripts.migrate --rollback

migrate-reload:
	python -m scripts.migrate --reload

## Remove unused imports
remove_imports:
	autoflake -ir --remove-unused-variables \
		--ignore-init-module-imports \
		--remove-all-unused-imports \
		${files_to_fmt}
	chmod -R 777 ./


## Sort imports
isort:
	isort ${files_to_fmt}


## Format code
black:
	black ${files_to_fmt}


## Check code formatting
black_check:
	black --check ${files_to_check}


## Format docstring PEP 257
docformatter:
	docformatter -ir ${files_to_fmt}


## Check docstring formatting
docformatter_check:
	docformatter -cr ${files_to_check}


## Check pep8
flake8:
	flake8 ${files_to_check}


## Check typing
mypy:
	mypy ${files_to_check}


## Check if all dependencies are secure and do not have any known vulnerabilities
safety:
	safety check --bare --full-report


## Check code security
bandit:
	bandit -r ${files_to_check} -x tests

## Add trailing comma works only on unix.
# an error is expected on windows.
add-trailing-comma:
	find ${files_to_fmt} -name "*.py" -exec add-trailing-comma '{}' \;
