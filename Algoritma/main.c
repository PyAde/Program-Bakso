#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
int jumlahpesan, total, uang, total_kupon, data_int, point;
char tukarkan[6]; 

printf("Masukan jumlah porsi yang ingin di pesan: ");
scanf("%d", &jumlahpesan);
total = jumlahpesan * 10000;

printf("Masukan uang pembayaran: ");
scanf("%d", &uang);
if (uang > total) {
printf("kembalian Rp. %d\n", uang - total);
printf("Jumlah point kamu %d\n", jumlahpesan * 10000);
} else if (uang == total) {
printf("Hore uang kamu ternyata pas Rp %d\n", uang);
printf("Jumlah point kamu %d\n", jumlahpesan * 10000);
} else {
printf("uang kamu kurang Rp. %d\n", total - uang);
return 0;
}

total_kupon = jumlahpesan / 10;
data_int = (int) total_kupon;
printf("Apakan anda yakin untuk menukarkan point [iya/tidak]: ");
scanf("%s", tukarkan); 
if (strcmp(tukarkan, "iya") == 0) { 
point = jumlahpesan * 10000;
if (point >= 100000) {
printf("SELAMAT ANDA MENDAPATKAN %d KUPON BAKSO GRATIS!!!\n", data_int);
} else {
printf("MAAF POINT KAMU KURANG %d\n", 100000 - point);
}
} else if (strcmp(tukarkan, "tidak") == 0) {
printf("Anda tidak menukarkan point. Point anda tetap %d\n",jumlahpesan * 10000);
} else {
printf("Input yang Anda masukkan salah. Mohon masukkan 'iya' atau 'tidak'\n");
}
}