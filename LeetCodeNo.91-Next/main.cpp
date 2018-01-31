#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int numDecodings(string s) {
        int multi = 1;
        
        // if less than 2 elements in string
        if(2 > s.size()) {
            return 1;
        }

        for(int i = 0; i < s.size(); i++) {
            if((s[i] == '1' || s[i] == '2') && s[i+1] != '0') {
                multi += (numDecodings(s.substr(i+2, s.size())) + numDecodings(s.substr(i+1, s.size())));
            }
        }
        return (0==s.size()?0:multi);
        
    }
};

int main() {

    string str = {"999219"};

    Solution s;

    cout << s.numDecodings(str);

    return 0;
}
