#include <string>
#include <iostream>
#include <climits>
using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        int ret = 0;
        int plusORminus = 1;
        int i = 0;
        while(str[i] == ' ') {i++;}                     // skip all blackspace ' '

        if(str[i] == '+' && str[i+1] == '-') return 0;  // shit..., this is meaningless...
        if(str[i] == '+') {plusORminus = +1;    i++;}   // if '+'
        if(str[i] == '-') {plusORminus = -1;    i++;}   // if '-'

        // read digit by digit
        while ( (str[i] >= '0') && (str[i] <= '9')) {
            if (ret >  INT_MAX / 10 || (ret == INT_MAX / 10 && str[i] - '0' > 7)) {
                if (plusORminus == 1) return INT_MAX;
                else return INT_MIN;
            }
            ret = ret * 10 + str[i++] - '0';
        }
        return (ret * plusORminus);
    }
};

int main() {
    Solution s;
    cout << s.myAtoi("123456");

    return 0;
}