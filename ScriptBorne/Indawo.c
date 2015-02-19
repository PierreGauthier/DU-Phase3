#ifdef HAVE_CONFIG_H
#  include "config.h"
#endif // HAVE_CONFIG_H

#include <errno.h>
#include <signal.h>
#include <stdlib.h>

#include <nfc/nfc.h>
#include <nfc/nfc-emulation.h>

#include "utils/nfc-utils.h"

static nfc_device *pnd;
static nfc_context *context;

static void stop_emulation(int sig) {
  (void)sig;
  if (pnd != NULL) {
    nfc_abort_command(pnd);
  } else {
    nfc_exit(context);
    exit(EXIT_FAILURE);
  }
}

static uint8_t __nfcforum_tag2_memory_area[] = {
  0x00, 0x00, 0x00, 0x00,  // Block 0
  0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0xFF, 0xFF,  // Block 2 (Static lock bytes: CC area and data area are read-only locked)
  0xE1, 0x10, 0x06, 0x0F,  // Block 3 (CC - NFC-Forum Tag Type 2 version 1.0, Data area (from block 4 to the end) is 48 bytes, Read-only mode)

  0x03, 0x21, 0xd1, 0x02,  // Block 4 (NDEF)
  0x1c, 0x53, 0x70, 0x91,
  0x01, 0x09, 0x54, 0x02,
  0x65, 0x6e, 0x4c, 0x69,

  0x62, 0x6e, 0x62, 0x63,
  0x51, 0x01, 0x0b, 0x55,
  0x03, 0x6c, 0x69, 0x62,
  0x6e, 0x66, 0x63, 0x2e,

  0x6f, 0x72, 0x67, 0x00,
  0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x00, 0x00,
};

static uint8_t __nfcforum_tag2_memory_header[] = {
  0x00, 0x00, 0x00, 0x00,  // Block 0
  0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0xFF, 0xFF,  // Block 2 (Static lock bytes: CC area and data area are read-only locked)
  0xE1, 0x10, 0x06, 0x0F,  // Block 3 (CC - NFC-Forum Tag Type 2 version 1.0, Data area (from block 4 to the end) is 48 bytes, Read-only mode)
 
  0x03, 0x21, 0xd1, 0x02,  // Block 4 (NDEF)
  0x1c, 0x53, 0x70, 0x91,
  0x01, 0x09, 0x54, 0x02,
  0x65, 0x6e, 0x4c, 0x69,

  0x62, 0x6e, 0x62, 0x63,
  0x51, 0x01, 0x0b, 0x55,
  0x04,
};

#define READ 		0x30
#define WRITE 		0xA2
#define SECTOR_SELECT 	0xC2

#define HALT 		0x50
static int
nfcforum_tag2_io(struct nfc_emulator *emulator, const uint8_t *data_in, const size_t data_in_len, uint8_t *data_out, const size_t data_out_len)
{
  int res = 0;

  uint8_t *nfcforum_tag2_memory_area = (uint8_t *)(emulator->user_data);

  printf("    In: ");
  print_hex(data_in, data_in_len);

  switch (data_in[0]) {
    case READ:
      if (data_out_len >= 16) {
        memcpy(data_out, nfcforum_tag2_memory_area + (data_in[1] * 4), 16);
        res = 16;
      } else {
        res = -ENOSPC;
      }
      break;
    case HALT:
      printf("HALT sent\n");
      res = -ECONNABORTED;
      break;
    default:
      printf("Unknown command: 0x%02x\n", data_in[0]);
      res = -ENOTSUP;
  }

  if (res < 0) {
    ERR("%s (%d)", strerror(-res), -res);
  } else {
    printf("    Out: ");
    print_hex(data_out, res);
  }

  return res;
}

int main(int argc, char *argv[]) {
	
	
	printf("\n");
	printf("\n");
	
	int i,j,k, n = sizeof(__nfcforum_tag2_memory_area);
	for(i=0; i<n/16; i++) {
		for(k=16*i; k<(16*i)+16; k++) {
			printf("%02X ",__nfcforum_tag2_memory_area[k]);
		}
		printf("   |   ");
		for(k=16*i; k<(16*i)+16; k++) {
			if(__nfcforum_tag2_memory_area[k] != 0x0B) printf("%c",__nfcforum_tag2_memory_area[k]);
			else printf("?");
		}
		printf("\n");
	}	
	
	char msg[] = "du-phase3-pierregauthier-1.c9.io";
	int msgsize = sizeof(msg), headersize = sizeof(__nfcforum_tag2_memory_header), ndefsize = (((msgsize+headersize)/16)+1)*16;
	uint8_t __nfcforum_tag2_memory_area2[ndefsize];
	
	printf("\n\n-------------------(%d-%d-%d)\n\n",headersize,msgsize,ndefsize);
	
	for (i=0; i<headersize; i++) {
		__nfcforum_tag2_memory_area2[i] = __nfcforum_tag2_memory_header[i];
	}
	for (i=0; i<msgsize; i++) {
		__nfcforum_tag2_memory_area2[i+headersize] = msg[i];
	}
	for (i=msgsize+headersize; i<ndefsize; i++) {
		__nfcforum_tag2_memory_area2[i] = 0x00;
	}
	__nfcforum_tag2_memory_area2[38] = 0x0B;
	
	
	n = sizeof(__nfcforum_tag2_memory_area2);	
	for(i=0; i<ndefsize/16; i++) {
		for(k=16*i; k<16*i+16; k++) {
			printf("%02X ",__nfcforum_tag2_memory_area2[k]);
		}
		printf("   |   ");
		for(k=16*i; k<16*i+16; k++) {
			if(__nfcforum_tag2_memory_area2[k] != 0x0B) printf("%c",__nfcforum_tag2_memory_area2[k]);
			else printf("?");
		}
		printf("\n");
	}
	
	printf("\n");

  nfc_target nt = {
    .nm = {
      .nmt = NMT_ISO14443A,
      .nbr = NBR_UNDEFINED, // Will be updated by nfc_target_init()
    },
    .nti = {
      .nai = {
        .abtAtqa = { 0x00, 0x04 },
        .abtUid = { 0x08, 0x00, 0xb0, 0x0b },
        .szUidLen = 4,
        .btSak = 0x00,
        .szAtsLen = 0,
      },
    }
  };

  struct nfc_emulation_state_machine state_machine = {
    .io = nfcforum_tag2_io
  };

  struct nfc_emulator emulator = {
    .target = &nt,
    .state_machine = &state_machine,
    .user_data = __nfcforum_tag2_memory_area2,
  };

  signal(SIGINT, stop_emulation);

  nfc_init(&context);
  if (context == NULL) {
    ERR("Unable to init libnfc (malloc)");
    exit(EXIT_FAILURE);
  }
  pnd = nfc_open(context, NULL);

  if (pnd == NULL) {
    ERR("Unable to open NFC device");
    nfc_exit(context);
    exit(EXIT_FAILURE);
  }

  printf("NFC device: %s opened\n", nfc_device_get_name(pnd));
  printf("Emulating NDEF tag now, please touch it with a second NFC device\n");

  if (nfc_emulate_target(pnd, &emulator, 0) < 0) {
    nfc_perror(pnd, argv[0]);
    nfc_close(pnd);
    nfc_exit(context);
    exit(EXIT_FAILURE);
  }

  nfc_close(pnd);
  nfc_exit(context);
  exit(EXIT_SUCCESS);
}
