.PHONY: all proto prepare-publish copy-bundle rename make-bundle prints clean publish-manually

all: make-bundle

proto:
	./gradlew build

prepare-publish:
	# need SIGNING_KEY environment variable to be set
	./gradlew publishToMavenLocal

BUNDLE_DIR := lib/build/distributions/io/github/grida-energy/deps/1.0.1

copy-bundle:
	mkdir -p $(BUNDLE_DIR)
	cp lib/build/libs/* $(BUNDLE_DIR)/
	cp lib/build/publications/mavenJava/pom-default.xml $(BUNDLE_DIR)/deps-1.0.1.pom
	cp lib/build/publications/mavenJava/pom-default.xml.asc $(BUNDLE_DIR)/deps-1.0.1.pom.asc

rename:
	make -f makefile.rename

make-bundle: proto prepare-publish copy-bundle rename
	make -f makefile.bundle

prints:
	echo '${MD5_FILES}'
	echo '${SHA1_FILES}'
	echo '${TO_HASH_FILES}'

clean:
	./gradlew clean

publish-manually:
	curl \
		--request POST \
		--verbose \
		--header "Authorization: Bearer ${SONATYPE_TOKEN}" \
		--form bundle=@lib/build/distributions/central-bundle.zip \
		https://central.sonatype.com/api/v1/publisher/upload