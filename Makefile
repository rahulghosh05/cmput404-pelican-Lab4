PYTHON ?= .venv/bin/python
PELICAN = $(PYTHON) -m pelican
GITHUB_PAGES_BRANCH = pages
.PHONY: html devserver publish github
html:
	$(PELICAN) content -s pelicanconf.py
devserver:
	$(PELICAN) content -s pelicanconf.py --autoreload --listen
publish:
	$(PELICAN) content -s publishconf.py
github: publish
	$(PYTHON) -m ghp_import output -b $(GITHUB_PAGES_BRANCH) -n
	git push origin $(GITHUB_PAGES_BRANCH)
