#include <stdlib.h>
#include <sys/types.h>
#include <fcntl.h>
#include <openssl/ssl.h>
#include <unistd.h>

char buf[8192];

main()
{
        int const fd=open("/proc/self/maps", O_RDONLY);
        SSL_library_init(); /* dummy call */
        for (;;) {
                size_t len=read(fd, buf, sizeof(buf));
                if (-1==len) {
                        perror("read"); exit(1);
                }
                if (0==len)
                        break;
                write(1, buf, len);
        }
        return 0;
}
