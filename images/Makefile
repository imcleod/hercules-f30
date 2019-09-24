all: kernel.img initrd.img initrd.addrsize

# See source for BZ link with details
# s390x boot process needs to know the size of the initrd in this way
gen-size: gen-size.c
	gcc -o gen-size gen-size.c

kernel.img:
	wget https://dl.fedoraproject.org/pub/fedora-secondary/releases/30/Server/s390x/os/images/kernel.img

initrd.img.in:
	wget -o initrd.img.in https://dl.fedoraproject.org/pub/fedora-secondary/releases/30/Server/s390x/os/images/initrd.img

initrd.img: initrd.img.in ks.cfg
	rm -f initrd.img
	cp initrd.img.in initrd.img
	echo ks.cfg | cpio -c -o >> initrd.img

initrd.addrsize: initrd.img gen-size
	gen-size `du initrd.img | cut -f 1`
