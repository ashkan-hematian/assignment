# Define the Python interpreter and the script
PYTHON = python3
MYPY = mypy
SCRIPT = main.py

# Default target: run the script
run:
	$(PYTHON) $(SCRIPT)

# Target to install dependencies from requirements.txt
install:
	$(PYTHON) -m pip install -r requirements.txt

# Clean up any generated files (example target, modify as needed)
clean:
	rm -rf __pycache__

# Target to run type checking with mypy
linter:
	$(PYTHON) -m mypy $(SCRIPT)

# Target to run tests using pytest
test:
	$(PYTHON) -m unittest discover -s test -p 'test_*.py'

# Phony targets to prevent Makefile from confusing them with files
 .PHONY: run install linter test clean
