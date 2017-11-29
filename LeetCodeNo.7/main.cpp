#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long long ret = 0;
        while(x != 0) {
            try {
                ret = (ret*10) + (x%10);
                if(ret > INT_MAX || ret < INT_MIN) {
                    throw "exceed";
                }
            } catch(const char* e) {
                return 0;
            }

            x   = x / 10;
        }

        return ret;
    }
};

int main() {
    Solution s;

    cout << s.reverse(-123) << endl;
    cout << s.reverse(123) << endl;
    cout << s.reverse(120) << endl;
    cout << s.reverse(-120) << endl;
 
    cout << s.reverse(1534236469) << endl;

    return 0;
}
