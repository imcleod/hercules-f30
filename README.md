## Intro

These are some very simple but specific helper scripts and configurations to install F30 for s390x inside the hercules emulator.

How simple?  **The instructions below should give you a running F30 s390x instance with 6 commands.**

I am by no means expert in mainframe or hecules.  Corrections and improvements welcome.

This was inspired by Daniel Horak's earlier work with F20 which he documented here:

https://sharkcz.livejournal.com/12268.html

More recent Fedora releases make use of newer s390x features that are not properly emulated by the 3.x series of hercules.

As a result, to use these scripts and instructions, you'll need to install the in-progress 4.x rpm-ification from here:

https://copr.fedorainfracloud.org/coprs/imcleod/hercules4/


## Instructions

Do several preparation steps:

`make all`

This downloads the install kernel and ramdisk, appends the kickstart file to the ramdisk, creates the hercules DASD image file and sets up a NAT rule and forwarding to allow the virtual QETH device inside of the hercules guest to route to the outside world.  Look in the Makefiles for details.

Now start hercules with our config.  Note that for this setup, you must be root, as hercules will create a tap networking device as it runs:

`sudo hercules -f ./fedora.cnf`

Within the hercules console, start the install.  In the mainframe world this is known as an Initial Program Load.  The details of the boot environment are described in the "ks.ins" file:

`herc =====> ipl ks.ins`

Now wait and watch for 2 to 3 hours.  You'll see occasional console output from Anaconda, combined with status output from the emulator itself.

If you are bored, press [esc] to toggle back and forth between a more device/CPU centric view of the emulator status, and the actual console/command-line.

If you end up in an emergency shell, you can interact with linux by prepending a "!" to console commands.  e.g.:

`herc =====> !ps xa`

For some reason, the emulator doesn't fully shut down for me when the install is finished.  However, the final Anaconda log messages appear, and the MIPS value goes way down.  At this point, you can quit and then restart the emulator.  e.g.:

`herc =====> quit`

and then:

`# sudo hercules -f ./fedora.cnf`

At this point you can IPL from the disk device we have just installed to, rather than into the install environment defined by ks.ins file.  In our configuration, this is device 130 and the command to IPL from it is the following:

`herc =====> ipl 130`

After a brief boot up, you should be able to "ssh root@192.168.200.3".  The root password is "fedora"
