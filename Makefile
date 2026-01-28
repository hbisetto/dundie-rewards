.PHONY: install virtualenv ipython clean test watch## Para não criar arquivos extras desnecessários

install:
	@echo "Installing for dev environment"
	@.venv/bin/python3 -m pip install -e ".[dev]"

virtualenv:
	@echo "Creating a virtualenv"
	@.venv/bin/python -m pip -m venv .venv

ipython:
	@echo "Openning the ipython usign the .venv"
	@.venv/bin/ipython 

test:
	@.venv/bin/pytest -vv -s tests/

watch:
	@.venv/bin/ptw -- -vv tests/

clean: ## Clean unused files
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./ -name '__pycache__' -exec rm -rf {} \;
	@find ./ -name 'Thumbs.db' -exec rm -f {} \;
	@find ./ -name '*~' -exec rm -f {} \;
	@rm -rf .cache
	@rm -rf .pytest_cache
	@rm -rf .mypy_cache
	@rm -rf build
	@rm -rf dist
	@rm -rf *.egg-info
	@rm -rf htmlcov
	@rm -rf .tox/
	@rm -rf docs/_build
