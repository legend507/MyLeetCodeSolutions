#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    bool isMatch(string s, string p) {
        // S is original string (it only contains characters), 
        //  p can contain characters, ?s and *s

        // scan from 0
        int s_ptr = 0;
        int p_ptr = 0;
        int star_pos = -1;
        int s_ptr_copy = -1;

        // iterate until reach the end of s (end of s is NULL 0x00)
        while(s[s_ptr]) {
            // 1st, if s and p have a same char or p has a ?, then check next
            if(p[p_ptr] == '?' || s[s_ptr] == p[p_ptr]) {s_ptr++; p_ptr++; continue;}

            // 2nd, if p has a *, things get complicated...
            /// if p has a *, record star position, p_ptr += 1, record s_ptr position
            if(p[p_ptr] == '*') {star_pos = p_ptr++; s_ptr_copy = s_ptr; continue;}

            // 3rd, if encountered a star before,
            /// move p_ptr behind *, move s_ptr 1 step
            if(star_pos != -1) {p_ptr = star_pos + 1; s_ptr = ++s_ptr_copy; continue;}

            // if 1st, 2nd and 3rd conditions are not meet
            return false;
        }

        // reached the end of s
        /// check p, if p only contains * from this point on, then return true
        while(p[p_ptr] == '*') {p_ptr++;}
        return (p_ptr == p.size());
    }
};

int main() {

// string in C++ also ended with a '\0', here is a proof
/*
    string str={"abcd"};
    cout << hex << int(str[0]) << endl;
    cout << hex << int(str[1]) << endl;
    cout << hex << int(str[2]) << endl;
    cout << hex << int(str[3]) << endl;
    cout << hex << int(str[4]) << endl;
    cout << hex << int(str[5]) << endl;
*/    
    

    return 0;
}
