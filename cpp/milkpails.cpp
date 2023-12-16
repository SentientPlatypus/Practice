/*
ID: geneust1
TASK: gift1
LANG: C++                 
*/

#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

bool dp[1005];

int main() {
    // Input and Output file streams for reading input from "pails.in" and writing output to "pails.out"
    ifstream cin("pails.in");
    ofstream cout("pails.out");

    // Read input values x, y, and m
    int x, y, m;
    cin >> x >> y >> m;

    // mx will store the maximum measurement
    int mx = 0;

    // dp array is used for dynamic programming to store whether a particular measurement is possible or not
    dp[0] = true;

    // Loop through measurements from 1 to m
    for (int i = 1; i <= m; i++)
    {
        // Check if it's possible to get the current measurement using pail with capacity x
        if (i - x >= 0 && dp[i - x])
        {
            dp[i] = true;  // Set dp[i] to true, indicating that measurement i is possible
            mx = i;        // Update mx to the current measurement i
            continue;      // Continue to the next iteration
        }

        // Check if it's possible to get the current measurement using pail with capacity y
        if (i - y >= 0 && dp[i - y])
        {
            dp[i] = true;  // Set dp[i] to true, indicating that measurement i is possible
            mx = i;        // Update mx to the current measurement i
            continue;      // Continue to the next iteration
        }
    }

    // Output the maximum measurement that can be obtained
    cout << mx;
}