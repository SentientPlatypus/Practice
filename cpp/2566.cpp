#include <string>
#include <math.h>
using namespace std;

class Solution {
public:
    int minMaxDifference(int num) {
        string s = to_string(num);
        char maxDigit = '0';
        char minDigit = '9';

        int i = 0;
        while (s[i] == '9') {
            i++;
        }

        s[i] = '9';

        int maxn = stoi(s);
        
        string mins = to_string(num);
        mins[0] = '0';
        int minn = stoi(mins);

        return abs(maxn - minn);
    }



};