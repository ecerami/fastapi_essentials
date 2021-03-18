PROJ_SLUG = essentials
PY_VERSION = 3.8
LINTER = flake8
FORMATTER = black

check: format lint

freeze:
	pip freeze > requirements.txt

lint:
	$(LINTER) $(PROJ_SLUG)

format:
	$(FORMATTER) $(PROJ_SLUG)

