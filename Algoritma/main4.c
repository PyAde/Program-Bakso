#include <stdio.h>

int main()
{
  float jr2;
  float luas;
  float keliling;

  // Meminta input jari-jari
  printf("Masukkan jari-jari: ");
  scanf("%f", &jr2);

  // Menghitung luas dan keliling lingkaran
  luas = 3.14 * jr2 * jr2;
  keliling = 2 * 3.14 * jr2;

  // Menampilkan hasil perhitungan
  printf("Luas lingkaran: %.2f\n", luas);
  printf("Keliling lingkaran: %.2f\n", keliling);

  return 0;
}
