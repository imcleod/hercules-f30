#include <stdio.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>

/* taken from https://bugzilla.redhat.com/show_bug.cgi?id=197773#c27 */

int main(int argc,char **argv)
{
        unsigned int zero = 0;
        int fd;
        unsigned int size;


        size = htonl(atoi(argv[1]));

        fd = open("initrd.addrsize", O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);
        write(fd, &zero, sizeof(int));
        write(fd, &size, sizeof(int));
        close(fd);
        return 0;
}
