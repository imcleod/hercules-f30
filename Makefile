.PHONY: dasd images network
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
