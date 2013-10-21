stuff64:
	rm -f *.o
	gcc -pie -fPIE -o where where.c -lssl
