#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        int i = 0;
        int j = people.size() - 1;
        int b = 0;

        sort(people.begin(), people.end());

        while (i <= j) {
            if (people[i] + people[j] <= limit) {
                i++;
                j--;
            }
            else j--;
            b++;
        }
        return b;
    }
};