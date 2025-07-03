#include <string>
#include <math.h>
using namespace std;

class Solution {
public:
    int minMaxDifference(int num) {
        int minMapping = getMinMapping(num);
        int maxMapping = getMaxMapping(num);
        return maxMapping - minMapping;
    }

    int getMinMapping(int num) {
        string s = to_string(num);
        string minNum = to_string(num);
        
        int i = 0;
        while (s[i] == '0' && i < s.size()) {
            i++;
        }
        
        char mappingChar = s[i];
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == mappingChar) {
                minNum[j] = '0';
            }
        }
        return stoi(minNum);
    }


    int getMaxMapping(int num) {
        string s = to_string(num);
        string maxNum = to_string(num);
        
        int i = 0;
        while (s[i] == '9' && i < s.size()) {
            i++;
        }
        
        char mappingChar = s[i];
        for (int j = 0; j < s.size(); j++) {
            if (s[j] == mappingChar) {
                maxNum[j] = '9';
            }
        }
        return stoi(maxNum);
    }


};
