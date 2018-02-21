#include    <unordered_map>
#include    <string>
#include    <iostream>
#include    <cmath>
using namespace std;


/*
    ATTENTION: this is a very good template designed to solve substring problems
        Remember, there are left boundary and right boundary to a window, I can move both boundaries!
*/
class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char,int> map;                // char is UniqueKey, int is occurance
        for(auto oneChar:t)     map[oneChar]++;     // counting all chars in t

        int windowRight     = 0;                    // a pointer to the window begin
        int windowLeft      = 0;                    // a pointer to the window end
        int counter         = t.size();             // # of all chars in string t
        int minStart        = 0;                    // start of a window
        int minLen          = INT_MAX;              // length of a window

        // move windowLeft from 0 to s.size(), to find a valid window
        while(windowLeft < s.size()) {
            // if s[windowLeft] is a correct char (a char that t has), decrease counter
            if(map[s[windowLeft]] > 0)
                counter --;

            // also decrease the corresponding value in map, map[?] can be negative
            map[s[windowLeft]]--;
            windowLeft++;

            // when counter reaches 0, we found a valid window!! now we move windowRight
            while(0 == counter) {
                // check if current window is smaller than minWindow
                if(windowLeft - windowRight < minLen) {
                    minStart    = windowRight;
                    minLen      = windowLeft - windowRight;
                }
                // increase the corresponding value in map, 
                map[s[windowRight]]++;

                // if s[windowRight] is a correct char, increase counter, this will break the while loop
                if(map[s[windowRight]] > 0) 
                    counter ++;
                
                windowRight++;
            }
        }

        return minLen==INT_MAX? "":s.substr(minStart, minLen);
    }
};

int main() {
    Solution so;
    string s = "ADOBECODEBANC";
    string t = "ABC";

    cout << so.minWindow(s, t) << endl;

    return 0;
}
