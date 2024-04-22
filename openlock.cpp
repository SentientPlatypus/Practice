#include <vector>
#include <queue>
#include <unordered_set>
#include <string>
using namespace std;

class Solution {
public:
    int openLock(vector<string>& deadends, string target) {
        unordered_set<string> v(deadends.begin(), deadends.end());
        if (v.count("0000")) return -1; 

        queue<string> q;
        q.push("0000");
        v.insert("0000");
        int level = 0;

        while (!q.empty()) {
            int levelSize = q.size();
            for (int i = 0; i < levelSize; ++i) {
                string c = q.front();
                q.pop();
                
                if (c == target) return level; 
                
                for (int j = 0; j < 4; ++j) {
                    for (int k = -1; k <= 1; k += 2) {
                        string n = c;
                        n[j] = (n[j] - '0' + k + 10) % 10 + '0'; 
                        if (!v.count(n)) {
                            q.push(n);
                            v.insert(n);
                        }
                    }
                }
            }
            ++level;
        }
        return -1; 
    }
};
