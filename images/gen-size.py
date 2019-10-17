#!/usr/bin/env python3
"""
createaddrsize INITRD_ADDRESS INITRD ADDRSIZE
  Create the initrd.addrsize file required in LPAR boot process.

  Examples:
    createaddrsize ${INITRD_ADDRESS} ${outroot}/${BOOTDIR}/initrd.img ${outroot}/${BOOTDIR}/initrd.addrsize
"""

import argparse
import os
import struct


#: DEST is the destination
DEST = 'initrd.addrsize'
#: SRC is the source to read in
SRC = 'initrd.img'


def main():
    """
    Main entry point.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s', '--src', help='The source to read in', default=SRC)
    parser.add_argument(
        '-d', '--dest', help='The destination', default=DEST)
    args = parser.parse_args()

    with open(args.dest, "wb") as addrsize:
        addrsize_data = struct.pack(
            ">iiii", 0, int("0x02000000", 16), 0, os.stat(args.src).st_size)
        addrsize.write(addrsize_data)


if __name__ == '__main__':
    main()
