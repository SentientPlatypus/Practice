#include <iostream>
#include <algorithm>
#include <vector>

bool isVowel(char letter) {
    return (letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u');
}

void generatePasscodes(int l, std::vector<char>& letters, std::string currentPasscode, int index) {
    if (currentPasscode.length() == l) {
        int vowelsCount = std::count_if(currentPasscode.begin(), currentPasscode.end(), isVowel);
        int nonVowelsCount = l - vowelsCount;

        if (vowelsCount >= 1 && nonVowelsCount >= 2) {
            std::cout << currentPasscode << "\n";
        }
        return;
    }

    if (index >= letters.size()) {
        return;
    }

    generatePasscodes(l, letters, currentPasscode + letters[index], index + 1);

    generatePasscodes(l, letters, currentPasscode, index + 1);
}

int main() {
    int l, c;
    std::cin >> l >> c;

    std::vector<char> letters(c);

    for (int i = 0; i < c; ++i) {
        std::cin >> letters[i];
    }

    std::sort(letters.begin(), letters.end());

    generatePasscodes(l, letters, "", 0);

    return 0;
}
