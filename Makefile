.PHONY: install format lint test sec

install:
	@poetry install
format:
	@isort .
	@black .
lint:
	@black . --check
	@isort . --check
	@prospector --with-tool pep257 --doc-warning
test: 	
	@pytest -v
sec: 
	@pip-audit