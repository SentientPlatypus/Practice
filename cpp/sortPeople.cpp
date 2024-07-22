#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        int i, key, j;
        string keyName;
        

        for (int i = 1; i < names.size(); i++) {
            key = heights[i];
            keyName = names[i];
            j = i - 1;


            while (j >= 0 && heights[j] < key) {
                heights[j + 1] = heights[j];
                names[j + 1] = names[j];
                j--;
            }
            heights[j + 1] = key;
            names[j + 1] = keyName;
        }


        for (int h : heights) cout << h;

        return names;
    }
};