#include <iostream>
#include <vector>
#include <string>

using namespace std;

void reverseEngineerProgram(const vector<vector<string>>& testCases) {
    for (const auto& testCase : testCases) {
        int N, M;
        sscanf(testCase[0].c_str(), "%d %d", &N, &M);

        // Initialize a vector to store the conditions of the program
        vector<int> conditions(N, -1);

        // Iterate through each input-output pair
        for (int i = 1; i <= M; ++i) {
            const string& inputString = testCase[i];
            string inputValues = inputString.substr(0, N);
            int output = inputString.back() - '0';

            // Check each condition in the input
            for (int j = 0; j < N; ++j) {
                if (conditions[j] == -1) {
                    // If the condition is not set, set it based on the input
                    conditions[j] = inputValues[j] - '0';
                } else if (conditions[j] != (inputValues[j] - '0')) {
                    // If the condition is inconsistent, Elsie is lying
                    cout << "LIE" << endl;
                    goto end_of_test_case;
                }
            }

            // All conditions are consistent with the input-output pair
            if (count(conditions.begin(), conditions.end(), -1) == 0) {
                cout << "OK" << endl;
            } else {
                cout << "LIE" << endl;
            }

            end_of_test_case:
            continue;
        }
    }
}

int main() {
    int T;
    cin >> T;

    vector<vector<string>> testCases;
    for (int t = 0; t < T; ++t) {
        int N, M;
        cin >> N >> M;

        vector<string> testCase;
        testCase.push_back(to_string(N) + " " + to_string(M));

        for (int m = 0; m < M; ++m) {
            string input;
            cin >> input;
            testCase.push_back(input);
        }

        testCases.push_back(testCase);
    }

    // Call the function to check if Elsie is lying or not
    reverseEngineerProgram(testCases);

    return 0;
}
