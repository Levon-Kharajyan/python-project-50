install:
	poetry install

gendiff:
	poetry run gendiff

build:
	poetry build

check:
	poetry check

package-install:
	python3 -m pip install --user dist/*.whl

package-reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest

test-cov:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: install build check lint test test-cov