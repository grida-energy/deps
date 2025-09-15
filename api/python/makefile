.PHONY: proto

PROTO_FILES := $(shell find ../protos -name "*.v1.proto")

proto:
	protoc --python_out=src --pyi_out=src ${PROTO_FILES} -I ../protos

clean:
	rm -rf src/deps