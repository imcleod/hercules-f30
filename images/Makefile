help:
	@echo "Targets:"
	@echo "- all:             Execute all build targets"
	@echo "- clean:           clean up"
	@echo "- kernel.img:      Download the kernel image from Fedora"
	@echo "- initrd.img.in:   Download the initrd.img.in file from Fedora"
	@echo "- initrd.img:      Generate the initrd.img"
	@echo "- initrd.addrsize: Execute the gen-size script"

all: kernel.img initrd.img initrd.addrsize

clean:
	rm -f kernel.img initrd.img.in initrd.img initrd.addrsize

kernel.img:
	wget https://dl.fedoraproject.org/pub/fedora-secondary/releases/30/Server/s390x/os/images/kernel.img

initrd.img.in:
	wget -O initrd.img.in https://dl.fedoraproject.org/pub/fedora-secondary/releases/30/Server/s390x/os/images/initrd.img

initrd.img: initrd.img.in ks.cfg
	rm -f initrd.img
	cp initrd.img.in initrd.img
	echo ks.cfg | cpio -c -o >> initrd.img

initrd.addrsize: initrd.img
	./gen-size.py
