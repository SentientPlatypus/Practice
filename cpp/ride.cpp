/*
ID: geneust1
TASK: ride
LANG: C++                 
*/

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int getval(const string& name) {
    int result = 1;
    for (char ch : name) {
        cout << ch << endl;
        result *= (ch - 'A' + 1);
    }
    return result;
}

int main() {
    ofstream fout ("ride.out");
    ifstream fin ("ride.in");


    string comet;
    string group;

    getline(fin, comet);
    getline(fin, group);

    int cometval = getval(comet);
    int groupval = getval(group);

    if (cometval % 47 == groupval % 47) {
        fout << "GO"<< endl;
    }
    else {
        fout << "STAY" << endl;
    }

    return 0;
}