.PHONY: all proto prepare-publish manually-publish clean

all: proto

proto:
	./gradlew build

prepare-publish:
	# need SIGNING_KEY environment variable to be set
	./gradlew publishToMavenLocal

manually-publish:
	./gradlew publishAllPublicationsToMavenCentralRepository --no-configuration-cache

clean:
	./gradlew clean
