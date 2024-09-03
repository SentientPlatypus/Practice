#include <string>
#include <vector>
#include <math.h>
using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        int converted = convert(s);

        for (int i = 1; i < k; i++) {
            converted = transform(converted);
        }
        return converted;
    }


    int convert(string s) {
        int sum = 0;
        for (char c : s) {
            int val = c - 'a' + 1;
            if (val >= 10) {
                sum += val % 10;
                val /= 10;
            }
            sum += val;
        }
        return sum;
    }

    int transform(int num) {
        if (num < 10) return num;
        return num % 10 + transform(num / 10);
    }
};