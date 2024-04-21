#include <iostream>
#include <cmath>
#include <unistd.h>
#include <cstring>

const int kScreenWidth = 80;
const int kScreenHeight = 22;
const int kTotalPixels = kScreenWidth * kScreenHeight;

void gotoxy(int x, int y) {
    std::cout << "\x1b[" << y + 1 << ";" << x + 1 << "H";
}

int main() {
    float A = 0, B = 0;
    float i, j;
    int k;
    float z[kTotalPixels];
    char b[kTotalPixels];

    std::cout << "\x1b[2J"; // Clear screen
    while (true) {
        memset(b, 32, kTotalPixels);
        memset(z, 0, kTotalPixels * sizeof(float));
        for (j = 0; j < 6.28; j += 0.07) {
            for (i = 0; i < 6.28; i += 0.02) {
                float c = sin(i);
                float d = cos(j);
                float e = sin(A);
                float f = sin(j);
                float g = cos(A);
                float h = d + 2;
                float D = 1 / (c * h * e + f * g + 5);
                float l = cos(i);
                float m = cos(B);
                float n = sin(B);
                float t = c * h * g - f * e;
                // Center the donut in the terminal window
                int x = kScreenWidth / 2 + static_cast<int>(30 * D * (l * h * m - t * n));
                int y = kScreenHeight / 2 + static_cast<int>(15 * D * (l * h * n + t * m));
                int o = x + kScreenWidth * y;
                int N = 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n);
                if (kScreenHeight > y && y > 0 && kScreenWidth > x && x > 0 && D > z[o]) {
                    z[o] = D;
                    b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
                }
            }
        }
        gotoxy(0, 0);
        for (k = 0; k < kTotalPixels; k++)
            putchar(k % kScreenWidth ? b[k] : 10);
        A += 0.03; // Increase the increment for A
        B += 0.01; // Increase the increment for B
        usleep(10000); // Delay in microseconds (10 ms)
    }
    return 0;
}
