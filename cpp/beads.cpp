/*
ID: geneust1
TASK: beads
LANG: C++
*/

#include <iostream>
#include <fstream>


using namespace std;

int main() {
    cout << "WE OUT" << endl;

    ofstream fout ("beads.out");
    ifstream fin ("beads.in");

    int len;
    fin >> len;

    string beads;
    fin >> beads;

    cout << beads << endl;
    const char* necklace = beads.c_str();
    for (char c: beads) {
        cout << c;
    }
    cout << endl;

    

}