help:
	@echo 'make test:         Test everything'

test:
	echo "Running tests..."
	#python3 -m unittest -v tests/test_countlinescommand.py
	python3 -m unittest discover tests -v
