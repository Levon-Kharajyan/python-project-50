install:
		poetry install

gendiff:
		poetry run gendiff

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

package-reinstall:
		python3 -m pip install --user --force-reinstall dist/*.whl

lint:
		poetry run flake8 gendiff

test:
		poetry run pytest

test-cov:
		poetry run pytest --cov=gendiff

.PHONY: install gendiff build publish package-install package-reinstall lint test test-cov
