#include <string>
#include <vector>
using namespace std;


class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        vector<int> v(26,-1);
        int curr = 0 ;
        int ans = -1;
        for(int i =0;i<s.size();i++){
            char x = s[i];
            if (v[x-'a']==-1){
                v[x-'a'] = i;
            }
            else{
                curr = i-v[x-'a']-1;
                ans = max(curr,ans);
            }
        }
        return ans;
    }
}; 