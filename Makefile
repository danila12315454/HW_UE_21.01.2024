CODE_FOLDERS := src
TEST_FOLDERS := test_circular_doubly_linked_list.py

.PHONY: test lint install format

install:
	poetry install --no-root

format:
	black .
	isort .

lint:
	isort --check .
	black --check .
	flake8 $(CODE_FOLDERS) $(TEST_FOLDERS)
	pylint $(CODE_FOLDERS) $(TEST_FOLDERS)
	mypy $(CODE_FOLDERS) $(TEST_FOLDERS)

test:
	poetry run pytest --cov=$(CODE_FOLDERS) --cov-fail-under=100