init:
	pip install . -r requirements.txt

test:
	pytest tests

remo:
	pip uninstall spacex_api
