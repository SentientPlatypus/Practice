#include <vector>

using namespace std;

class Solution {
public:
    int numTeams(vector<int>& rating) {
        int n = rating.size();
        int teams = 0;

        vector<vector<int>> increasingTeams(n, vector<int>(4, 0));
        vector<vector<int>> decreasingTeams(n, vector<int>(4, 0));

        for (int i = 0; i < n; i++) {
            increasingTeams[i][1] = 1;
            decreasingTeams[i][1] = 1;
        }

        for (int c = 2; c <= 3; c++) {
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    if (rating[j] > rating[i]) increasingTeams[j][c] += increasingTeams[i][c - 1];
                    if (rating[j] < rating[i]) decreasingTeams[j][c] += decreasingTeams[i][c - 1];
                }
            }
        }

        for (int i = 0; i < n; i++) {
            teams += increasingTeams[i][3] + decreasingTeams[i][3];
        }

        return teams;
    }
};