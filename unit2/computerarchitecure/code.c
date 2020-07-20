#include <stdio.h>
#include <stdlib.h>

// int main(void)
// {
//     int x = 100;   // value is 100 decimal
//     int h = 0x100; // value is 256 decimal
//     int b = 0b100; // value is 4 decimal

//     int y = 0x47F;

//     if (b == 0x04){
//         // TRUE
//     }
//     return 0;
// }

// int main(void)
// {
//     int x = 0b11000101

//     printf("%d decimal\n", x);
//     printf("%x hex\n", x);
//     printf("%X hex\n", x)
//     return 0;
// }
// int main(void)
// {
//     int y = 255;
//     char s[20];
//     sprintf(s, "%X", y);
//     printf("%s\n", s);
//     return 0;
// }

int main(void)
{
    char *s = "110011";
    long v = strtol(s, NULL, 2);
    printf('%ld\n', v);
    return 0;

}