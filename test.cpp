#include <stdio.h>
int string_ln(char*);
int main() {
char s[10];
int length;
printf("Nhap chuoi bat ky: ");
fgets(s, sizeof(s), stdin);
length = string_ln(s);
printf("\nDo dai chuoi %s la: %d\n", s, length);
return 0;
}
int string_ln(char *p) {
int count = 0;
while (*p != '\0' && *p != '\n') { // Thêm kiểm tra '\n'
count++;
p++;
}
return count;
}