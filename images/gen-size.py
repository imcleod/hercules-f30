#!/usr/bin/python

import os
import struct

'''
createaddrsize INITRD_ADDRESS INITRD ADDRSIZE
  Create the initrd.addrsize file required in LPAR boot process.

  Examples:
    createaddrsize ${INITRD_ADDRESS} ${outroot}/${BOOTDIR}/initrd.img ${outroot}/${BOOTDIR}/initrd.addrsize
'''

dest="initrd.addrsize"
src="initrd.img"

addrsize = open(dest, "wb")
addrsize_data = struct.pack(">iiii", 0, int("0x02000000", 16), 0, os.stat(src).st_size)
addrsize.write(addrsize_data)
addrsize.close()


