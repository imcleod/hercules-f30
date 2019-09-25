.PHONY: dasd images
all: dasd images

clean:
	make -C dasd clean
	make -C images clean

dasd:
	make -C dasd

images:
	make -C images
