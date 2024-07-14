#include <stack>
#include <string>
#include <unordered_map>
#include <map>
#include <cctype>

using namespace std;

class Solution {
public:
    string countOfAtoms(string formula) {
        stack<unordered_map<string, int>> st;
        unordered_map<string, int> mp;
        int n = formula.size();
        
        for (int i = 0; i < n; ) {
            if (formula[i] == '(') {
                // Push the current map onto the stack and start a new one for the inner formula
                st.push(mp);
                mp.clear();
                i++;
            } else if (formula[i] == ')') {
                // Pop the top map from the stack
                unordered_map<string, int> top = mp;
                mp = st.top();
                st.pop();
                i++;
                
                // Parse the multiplier
                int start = i;
                while (i < n && isdigit(formula[i])) i++;
                int multiplier = (start < i) ? stoi(formula.substr(start, i - start)) : 1;
                
                // Apply the multiplier to the popped map and add to the current map
                for (const auto& p : top) {
                    mp[p.first] += p.second * multiplier;
                }
            } else {
                // Parse the element
                int start = i;
                i++;
                while (i < n && islower(formula[i])) i++;
                string element = formula.substr(start, i - start);
                
                // Parse the count
                start = i;
                while (i < n && isdigit(formula[i])) i++;
                int count = (start < i) ? stoi(formula.substr(start, i - start)) : 1;
                
                mp[element] += count;
            }
        }
        
        map<string, int> sorted_mp(mp.begin(), mp.end());
        string result;
        for (const auto& p : sorted_mp) {
            result += p.first;
            if (p.second > 1) result += to_string(p.second);
        }
        
        return result;
    }
};
