#include <string>
#include <unordered_set>
#include <utility> 

using namespace std;

struct pair_hash {
    template <class T1, class T2>
    std::size_t operator () (const std::pair<T1, T2>& p) const {
        auto hash1 = std::hash<T1>{}(p.first);
        auto hash2 = std::hash<T2>{}(p.second);
        return hash1 ^ hash2;
    }
};

class Solution {
public:
    bool isPathCrossing(string path) {
        int sx = 0, sy = 0;
        unordered_set<pair<int, int>, pair_hash> s;
        s.insert({0, 0});
        
        for (char c : path) {
            if (c == 'N')
                sy += 1;
            else if (c == 'E')
                sx += 1;
            else if (c == 'S')
                sy -= 1;
            else if (c == 'W')
                sx -= 1;
            
            pair<int, int> p = {sx, sy};
            
            if (s.find(p) == s.end())
                s.insert(p);
            else
                return true;
        }
        
        return false;
    }
};