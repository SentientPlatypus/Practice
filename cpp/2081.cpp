#include <string>
#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long kMirror(int k, int n) {
        int count = 0;
        long long ans = 0;
        int left = 1;
        while (count < n) {
            int right = left * 10;
            // op = 0: odd-length palindromes, op = 1: even-length palindromes
            for (int op = 0; op < 2; ++op) {
                for (int i = left; i < right && count < n; ++i) {
                    long long combined = i;
                    int x = (op == 0 ? i / 10 : i);
                    while (x) {
                        combined = combined * 10 + x % 10;
                        x /= 10;
                    }
                    string basek = baseTenToBaseK(combined, k);
                    if (isPalindrome(basek)) {
                        ++count;
                        ans += combined;
                    }
                }
            }
            left = right;
        }
        return ans;
    }
    
    string baseTenToBaseK(long long i, long long k) {
        if (i == 0) return "0";  // Base case should return "0"
        
        string result = "";
        while (i > 0) {
            result = to_string(i % k) + result;
            i /= k;
        }
        return result;
    }
    
    bool isPalindrome(string k) {
        int i = 0;
        int j = k.size() - 1;
        
        while (i <= j) {
            if (k[i] != k[j]) return false;
            i++;
            j--;
        }
        return true;
    }


};