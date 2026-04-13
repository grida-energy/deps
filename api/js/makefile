.PHONY: requirements proto

all: requirements proto

requirements:
	bun install

proto:
	bun x buf generate

clean:
	rm -rf ./deps
