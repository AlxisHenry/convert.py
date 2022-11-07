run:
	python setup.py build
	pytest tests/
setup: requirements.txt
	pip install -r requirements.txt