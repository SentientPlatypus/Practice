#include <stack>
#include <cstdlib> // for atoi
#include <cctype> // for isdigit
#include <string>
#include <vector>
using namespace std;
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> s;

        for (string& token : tokens) {
            if (token != "+" && token != "-" && token !="*" && token !="/" && token !="%") {
                s.push(stoi(token));
            }
            else {
                int n2 = s.top(); s.pop();
                int n1 = s.top(); s.pop();
                if (token == "+") {
                    s.push(n1 + n2);
                } 
                else if (token == "-") {
                    s.push(n1 - n2);
                }
                else if (token == "*") {
                    s.push(n1 * n2);
                }
                else if (token == "/") {
                    s.push(n1 / n2);
                }
                else if (token == "%") {
                    s.push(n1 % n2);
                }
                else {
                    continue;
                }
            }
        }
        return s.top();
    }
};