#include <vector>
#include <deque>
#include <algorithm>

using namespace std;
class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        deque<int> dq;
        sort(deck.begin(), deck.end());

        for (auto it = deck.rbegin(); it != deck.rend(); ++it) {
            if (!dq.empty()) {
                int last = dq.back();
                dq.pop_back();
                dq.push_front(last);
            }
            dq.push_front(*it);
        }

        return vector<int>(dq.begin(), dq.end());
    }
};