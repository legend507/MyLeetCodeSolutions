// This problem has a mathematical name, call 'Digital Root', 
// And it also has a formula, called congruence formula, as a quick solution
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    int addDigits(int num) {
        int sum = 0;
        while(num > 9) {
            sum += num%10;
            num /= 10;
        }
        sum += num;
        if(sum < 10)
            return sum;
        else {
            return addDigits(sum);            
        }
    }
    int oneLineSolution(int num) {
        return ( 1+(num-1)%9 );
    }

};

int main() {
        
        int ret = Solution().addDigits(38);
        cout << ret << endl;
    return 0;
}