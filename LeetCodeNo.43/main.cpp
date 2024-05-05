#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Solution {
private:
    void multiplyDigits(string& num1,string& num2, vector<int>& product) {
        for(int i = num1.size() - 1; i >= 0; i--) {

            for(int j = num2.size() - 1; j >= 0; j--) {

                int digit1 = num1[i] - '0';
                int digit2 = num2[j] - '0';
                int multiply = digit1 * digit2;

                int sum = multiply + product[i + j + 1];
                product[i + j + 1] = sum % 10;
                product[i + j] += sum / 10;
            }
        }
    }

    string convertToString(const vector<int>& product) {
        string result = "";
        for(int digit : product) {
            result += to_string(digit);
        }
        return result;
    }

    string removeLeadingZeros(const string& str) {
        int idx = 0;
        while(str[idx] == '0') {
            idx++;
        }
        return (idx == 0) ? str : str.substr(idx);
    }

public:
    string multiply(string num1, string num2) {
        if(num1 == "0" || num2 == "0")
            return "0";

        vector<int> product(num1.size() + num2.size(), 0);

        multiplyDigits(num1, num2, product);

        string result = convertToString(product);

        return removeLeadingZeros(result);
    }
};

int main() {
  string num1 = "123";
  string num2 = "456";

  Solution s;

  std::cout << s.multiply(num1, num2);

  return 0;
}
