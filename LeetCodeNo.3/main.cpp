#include <vector>
#include <string>
#include <iostream>
using namespace std;

class solution {
public:
    int lengthOfLongestSubstrings(string s) {
        vector<string>  substrings;
        vector<int>     length;
        string          sub;
        int             ret = 0;

        for(int i = 0; i < s.length(); i++) {

            if(string::npos == sub.find(s[i])) {
                // current character is not in sub
                
            } else {
                // current charactor in sub
                sub.erase(sub.begin(), sub.begin() + sub.find(s[i])+1);
            }
            sub += s[i];

            ret = (ret < sub.length())? sub.length():ret;
            cout << sub << endl;
        }
        return ret;
    }
};

int main() {
    solution s;
    string input = "pwwkew";
    input = "abcdefb";

    cout << s.lengthOfLongestSubstrings(input) << endl;

    return 0;
}