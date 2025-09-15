.PHONY: proto test

all: proto test

proto:
	rm -rf protos
	mkdir protos
	cp -r ../protos/deps protos/deps

test:
	cargo test

clean:
	rm -rf protos
	cargo clean