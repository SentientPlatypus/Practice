#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:

    int removeSubstring(char first, char second, int points, std::string& s) {
        vector<char> vec;
        int localPoints = 0;

        for (char c : s) {
            if (!vec.empty() && vec.back() == first && c == second) {
                vec.pop_back();
                localPoints += points;
            } else {
                vec.push_back(c);
            }
        }

        // Reconstruct the string s from the vector
        s.assign(vec.begin(), vec.end());

        return localPoints;
    }

    int maximumGain(string s, int x, int y) {
        int points = 0;

        if (x > y) {
            points += removeSubstring('a', 'b', x, s);
            points += removeSubstring('b', 'a', y, s);
        } else {
            points += removeSubstring('b', 'a', y, s);
            points += removeSubstring('a', 'b', x, s);
        }

        return points;
    }
};
