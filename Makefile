.PHONY: dasd images network help

help:
	@echo "Targets:"
	@echo "- all:     Execute all build targets"
	@echo "- clean:   Clean up"
	@echo "- network: Execute network creation script"
	@echo "- dasd:    Create the dasd"
	@echo "- network: Create the images"

all: dasd images network

clean:
	make -C dasd clean
	make -C images clean

network:
	sudo ./setup_network.sh

dasd:
	make -C dasd

images:
	make -C images
