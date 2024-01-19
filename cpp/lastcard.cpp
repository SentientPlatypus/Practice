#include <iostream>
#include <cmath>

int findLastRemainingCard(int N) {
    return 2 * (N - static_cast<int>(pow(2, floor(log2(N))))) + 1;
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <N>" << std::endl;
        return 1;
    }

    int N = std::stoi(argv[1]);

    if (N <= 0) {
        std::cerr << "N should be a positive integer." << std::endl;
        return 1;
    }

    int result = findLastRemainingCard(N);

    std::cout << "Position of the last remaining card for N = " << N << " is: " << result << std::endl;

    return 0;
}
