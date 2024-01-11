#include <iostream>
#include <fstream>
#include <string>

int main() {
    std::ifstream fin ("pfs.in");
    std::ofstream fout ("pfs.out");

    int N;
    fin >> N;

    for (int t = 0; t < N; t++) {
        std::string s;
        fin >> s;
        std::cout << s << "\n";

        bool pass = true;
        int counter = 0;
        for (char &c : s) {
            if (c == '(') {
                counter += 1;
            }
            else {
                counter -= 1;
            }
            if (counter < 0) {
                pass = false;
                fout << "NO" << "\n";
                break;
            }
        }

        if (counter == 0) {
            fout << "YES" << "\n";
        }
        else {
            fout << "NO" << "\n";
        }
    }

}