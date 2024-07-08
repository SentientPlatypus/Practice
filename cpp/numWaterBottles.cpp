#include <cmath>

using namespace std;

class Solution {
public:
    int numWaterBottles(int numBottles, int numExchange) {
        return solve(0, numBottles, 0, numExchange);
    }

    int solve(int drank, int fullBottles, int empty, int numExchange) {
        if (fullBottles + empty < numExchange) return fullBottles + drank;


        //drink
        drank += fullBottles;
        empty += fullBottles;

        //exchange
        int newFullBottles = floor(empty / numExchange);
        empty -= newFullBottles * numExchange;
        fullBottles = newFullBottles;


        return solve(drank, newFullBottles, empty, numExchange);
    }
};