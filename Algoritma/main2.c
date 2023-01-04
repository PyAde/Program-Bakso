#include <stdio.h>

int main() {
int jumlahpesan, total, uang, point;

printf("Masukan jumlah porsi yang ingin di pesan: ");
scanf("%d", &jumlahpesan);
total = jumlahpesan * 10000;

printf("Masukan uang pembayaran: ");
scanf("%d", &uang);
if (uang > total) {
printf("kembalian Rp. %d\n", uang - total);
} else if (uang == total) {
printf("Hore uang kamu ternyata pas Rp %d\n", uang);
} else {
printf("uang kamu kurang Rp. %d\n", total - uang);
return 0;
}
}