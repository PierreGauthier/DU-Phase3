Indawo : Indawo.o nfc.o wiringPiSPI.o wiringPi.o piHiPri.o piThread.o
	@gcc Indawo.o nfc.o wiringPiSPI.o wiringPi.o piHiPri.o piThread.o -o Indawo -lpthread -g
Indawo.o : Indawo.c nfc.h wiringPiSPI.h
	@gcc -c Indawo.c -g
nfc.o : nfc.c nfc.h wiringPiSPI.h
	@gcc -c nfc.c -g
wiringPiSPI.o : wiringPiSPI.c wiringPiSPI.h
	@gcc -c wiringPiSPI.c -g
wiringPi.o : wiringPi.c wiringPi.h
	@gcc -c wiringPi.c -g
piHiPri.o : piHiPri.c
	@gcc -c piHiPri.c -g
piThread.o : piThread.c
	@gcc -c piThread.c -g
clean :
	@rm *.o readID
install : 
	@cc -shared -fpic -o libNFC.so nfc.c wiringPiSPI.c wiringPi.c piHiPri.c piThread.c -lpthread
	@sudo mv libNFC.so /usr/lib
