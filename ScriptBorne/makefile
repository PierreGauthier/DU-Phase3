Indawo : Indawo.o utils/nfc-utils.o
	@gcc Indawo.o utils/nfc-utils.o -o Indawo -lnfc -g
Indawo.o : Indawo.c
	@gcc -c Indawo.c -g
clean :
	@rm *.o Indawo
install : 
	@cc -shared -fpic -o libNFC.so nfc.c wiringPiSPI.c wiringPi.c piHiPri.c piThread.c -lpthread
	@sudo mv libNFC.so /usr/lib
