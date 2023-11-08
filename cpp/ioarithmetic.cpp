#include <iostream>
#include <fstream>
#include <string>


using namespace std;

int main() {
    ifstream fin ("file.in");
    ofstream fout ("file.out");


    int firstnum;
    int secondnum;

    fin >> firstnum;
    fin >> secondnum;

    cout << firstnum + secondnum << endl;
    fout << firstnum + secondnum << endl;
    return 0;
}