
#include <vector>

class Solution {
public:
    int findSpecialInteger(std::vector<int>& arr) {
        int maxcount = 0;
        int maxnum = arr[0];

        int current = arr[0];
        int timesappeared = 0;

        for (int i = 0; i < arr.size(); i ++) {
            if (arr[i] == current) timesappeared ++;
            else {
                if (timesappeared > maxcount) {
                    maxcount = timesappeared;
                    maxnum = current;
                }
                timesappeared = 1;
                current = arr[i];
            }
        }
        if (timesappeared > maxcount) {
            maxnum = current;
        }

        return maxnum;

    }
};