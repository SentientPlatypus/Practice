/*
ID: geneust1
TASK: friday
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>



using namespace std;


int main() {
    cout << "WE OUT" << endl;
    ofstream fout ("friday.out");
    ifstream fin ("friday.in");

    int nyears;
    fin >> nyears;

    int arr[7] = {0,0,0,0,0,0,0};

    int thirtydaymonths[4] = {9, 4, 6, 11};
    int currentday = 2;
    

    int totaldays = 0;
    for (int i = 1900; i <= 1900 + nyears - 1; i++) {
        
        for (int month = 1; month <=12; month++) {
            int days;
            
            if (find(begin(thirtydaymonths), end(thirtydaymonths), month) != end(thirtydaymonths)) {
                days = 30;
            }
            else {
                days = 31;
                if (month == 2) {
                    days = 28;
                    if ((i % 4 == 0 && i % 100 != 0) || (i % 400 == 0)) {
                        days = 29;
                    }
                }
            }

            for (int day = 1; day <= days; day ++) {
                if (day == 13) {
                    arr[currentday] +=1;
                }
                currentday += 1;
                currentday %= 7;

            }
        }
    }

    for (int i = 0; i < 7; i++) {
        fout << arr[i];
        cout << arr[i];
        if (i < 6) {
            fout << " ";
            cout << " ";
        }
    }
    fout << endl;
    cout << endl;
}