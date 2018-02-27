#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    // think s = 11111 <- This is a fucking Fibonaci, with ret = 8
    // think s = 11119 <- This is also a Fibonaci, with ret = 8
    // think s = 111191 <- same as 11119, ret = 8
    int numDecodings(string s) {
        // if size = 0 or first element is 0
        if( !s.size() || s.front() == '0') return 0;

        // ret          : decode ways of s[i]
        // ret_former   : decode ways of s[i-1]
        int ret = 1, ret_former = 1;

        // traverse from s[1], because already made sure s[0] != 0
        for(int i = 1; i < s.size(); i++) {
            // check if is 0
            if(s[i] == '0') {
                ret = 0;
            }

            // then check if former digit is 1 or 2
            // 10 ~ 16, 20~26
            if(s[i-1] == '1' || s[i-1] == '2' && s[i] <= '6') {
                ret = ret + ret_former;
                ret_former = ret - ret_former;
            } 
            // 17, 18, 19
            else {

                // 11001, when reach another valid number after consecutive 0s, ret and ret_former are both 0
                ret_former = ret;
            }
        }
        return ret;
    }
};

int main() {

    string str = {"10"};

    Solution s;

    cout << s.numDecodings(str);

    return 0;
}
