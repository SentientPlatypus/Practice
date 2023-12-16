class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.length() > haystack.length()) {
            return -1;
        }

        for (int i = 0; i < haystack.length(); i ++) {
            for (int k = 0; k < needle.length(); k++) {
                if (k + i >= haystack.length() || haystack[i + k] != needle[k]) break;
                if (k == needle.length() - 1) return i;
            }
        }
        return -1;
    }
};