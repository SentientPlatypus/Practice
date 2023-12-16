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

int main() {
    ifstream fin("diamonds.in");
    ofstream fout("diamonds.out");

    int N, K;
    fin >> N >> K;

    vector<int> d(N);

    for (int i = 0; i < N; i ++) {
        fin >> d[i];
    }

    int mx = 0;
    int temp = 1;
    sort(d.begin(), d.end());

    for (int i = 1; i < N; i ++) {
        if (abs(d[i] - d[i-1]) <= K) {
            temp += 1;
        } 
        else {
            mx = max(mx, temp);
            temp = 1;
        }
    }

    mx = max(mx, temp);

    fout << temp << "\n";
    return 0;
}