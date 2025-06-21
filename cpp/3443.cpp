class Solution {
public:
    int maxDistance(string s, int k) {
        int x = 0, y = 0;
        int res = 0;
        for (int i = 0; i < s.size(); i++) {
            switch (s[i]) {
                case 'N': {y++; break;}
                case 'S': {y--; break;}
                case 'E': {x++; break;}
                case 'W': {x--; break;}
            }


            int md = abs(x) + abs(y);
            res = max(res, md + min(2 * k, i + 1 - md));
        }

        return res;
    }
};