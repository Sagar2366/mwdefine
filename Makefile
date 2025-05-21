.PHONY: all build test artifact clean

all: build test

build:
	python3 -m pip install --upgrade pip
	pip install .

test:
	pytest

artifact:
	python3 -m build

clean:
	rm -rf dist/ build/ *.egg-info
