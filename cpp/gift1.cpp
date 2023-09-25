/*
ID: geneust1
TASK: gift1
LANG: C++                 
*/

#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <vector>


using namespace std;


int main() {
    cout << "we out"<< endl;
    ofstream fout ("gift1.out");
    ifstream fin ("gift1.in");

    int np;
    map<string, int> table;
    vector<string> names;
    fin >> np;

    for (int i = 0; i < np; i++ ) {
        string name;
        fin >> name;

        table[name] = 0;
        names.push_back(name);
    }

    while (!fin.eof()) {
        string giver;
        fin >> giver;

        int amount;
        int nshare;
        fin >> amount >> nshare;

        if (nshare == 0) {
            break;
        }

        int foreach = amount / nshare;
        int remainder = amount % nshare;

        table[giver] -= (amount - remainder);

        for (int i = 0; i < nshare; i ++) {
            string reciever;
            fin >> reciever;

            table[reciever] += foreach;
        }
    }


    for (const string& name : names) {
        cout << name << " " << table[name] << endl;
        fout << name << " " << table[name] << endl;
    }
    

    return 0;
}