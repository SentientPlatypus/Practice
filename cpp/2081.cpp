#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    long long kMirror(int k, int n) {
        long long ans = 0;
        
        string curp = "0";  // Start with 0
        int counter = 0;
        
        while (counter < n) {
            curp = nextPalindromeEfficient(curp);
            
            long long curpdec = stoll(curp);
            string basek = baseTenToBaseK(curpdec, k);
            if (isPalindrome(basek)) {
                counter++;
                ans += curpdec;
            }
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

    bool isAllNines(const string& s) {
        for (char c : s) {
            if (c != '9') return false;
        }
        return true;
    }
    
    string nextPalindromeEfficient(const string& palindrome) {
        int n = palindrome.length();

        if (n == 1) {
            int digit = palindrome[0] - '0';
            return (digit == 9) ? "11" : to_string(digit + 1);
        }
        

        if (palindrome[0] == '9' && palindrome.find_first_not_of('9') == string::npos) {
            return "1" + string(n - 1, '0') + "1";
        }
        
        // Extract the first half (and middle digit if odd length)
        int halfLen = n / 2;
        string firstHalf = palindrome.substr(0, halfLen);
        char middleDigit = (n % 2 == 1) ? palindrome[halfLen] : '\0';
        
        // Convert first half (with middle digit if odd) to number and increment
        string incrementBase = firstHalf;
        if (n % 2 == 1) incrementBase += middleDigit;
        
        long long incrementedNum = stoll(incrementBase) + 1;
        string incremented = to_string(incrementedNum);
        
        // Handle carry that changes the length
        if (incremented.length() > incrementBase.length()) {
            // For even length palindromes like "99", the next is "101"
            if (n % 2 == 0) {
                return "1" + string(n-1, '0') + "1";
            } else {
                // Odd length becomes even
                string result = incremented;
                for (int i = incremented.length() - 2; i >= 0; i--) {
                    result += incremented[i];
                }
                return result;
            }
        }
        
        // Normal case - extract new first half and middle digit
        string newFirstHalf;
        if (n % 2 == 1) {
            newFirstHalf = incremented.substr(0, halfLen);
            middleDigit = incremented[halfLen];
        } else {
            newFirstHalf = incremented;
        }
        
        // Construct the result
        string result = newFirstHalf;
        if (n % 2 == 1) result += middleDigit;
        
        // Add the reversed first half
        for (int i = newFirstHalf.length() - 1; i >= 0; i--) {
            result += newFirstHalf[i];
        }
        
        return result;
    }

};