.PHONY: proto test

all: proto test

proto:
	rm -rf protos
	mkdir protos
	cp -r ../protos/eps protos/eps

test:
	cargo test
