-include .env

.PHONY: all test clean deploy help install build develop lock update

develop :; maturin develop --release

build :; maturin build --release

install :; poetry install --no-root

test :; poetry run pytest tests

lock :; poetry lock

update :; poetry update

clean:
	cargo clean
	rm -rf optrush/__pycache__
	rm -f optrush/*.so
	rm -rf target
	rm -rf *.egg-info
