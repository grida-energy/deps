PROTO_FILES := $(shell find ../protos -name "*.v1.proto")

deps-protos.md:
	protoc --doc_out=. --doc_opt=markdown,deps-protos.md $(PROTO_FILES) -I ../protos

clean:
	rm -f doc/deps-protos.md
