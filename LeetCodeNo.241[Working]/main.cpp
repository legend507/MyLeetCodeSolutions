#include <iostream>
#include <string>
#include <vector>
#include <cassert>
using namespace std;

class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> ret;
        return ret;
    }
};

string stringToString(string input) {
    assert(input.length() >= 2);
    string result;
    for (int i = 1; i < input.length() -1; i++) {
        char currentChar = input[i];
        if (input[i] == '\\') {
            char nextChar = input[i+1];
            switch (nextChar) {
                case '\"': result.push_back('\"'); break;
                case '/' : result.push_back('/'); break;
                case '\\': result.push_back('\\'); break;
                case 'b' : result.push_back('\b'); break;
                case 'f' : result.push_back('\f'); break;
                case 'r' : result.push_back('\r'); break;
                case 'n' : result.push_back('\n'); break;
                case 't' : result.push_back('\t'); break;
                default: break;
            }
            i++;
        } else {
          result.push_back(currentChar);
        }
    }
    return result;
}

string integerVectorToString(vector<int> list, int length = -1) {
    if (length == -1) {
        length = list.size();
    }

    string result;
    if (length == 0) {
        return result;
    }

    for(int index = 0; index < length; index++) {
        int number = list[index];
        result += to_string(number) + ", ";
    }
    return result.substr(0, result.length() - 2);
}

int main() {
    cout << "Nameless shit" << endl;
    string line;
    while (getline(cin, line)) {
        string input = stringToString(line);
        
        vector<int> ret = Solution().diffWaysToCompute(input);

        string out = integerVectorToString(ret);
        cout << out << endl;
    }
    return 0;
}