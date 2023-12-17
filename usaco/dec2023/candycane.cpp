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

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N, M;
    cin >> N >> M;

    vector<int> cows(N);
    vector<vector<int>> canes(M, vector<int>(2, 0));

    for (int i = 0; i < N; i++) {
        cin>>cows[i];
    }

    int height;
    for (int i = 0; i < M; i++) {
        cin >> canes[i][1];
    }


    for (long long i = 0; i < canes.size(); i ++) {
        for (long long k = 0; k < cows.size(); k ++) {
            if (cows[k] > canes[i][0]) {
                long long diff;
                
                if (cows[k] > canes[i][1]) {
                    diff = canes[i][1] - canes[i][0];
                }
                else {
                    diff = cows[k] - canes[i][0];
                }
                
                canes[i][0] += diff;
                cows[k] += diff;
            }
        }
    }

    for (long long cow:cows) {
        cout << cow << "\n";
    }
    return 0;
}