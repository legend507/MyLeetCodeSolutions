#include <iostream>
#include <vector>
#include <set>
using namespace std;

int main() {

    multiset<int> m;

    m.insert(0);
    m.insert(1);
    m.insert(7);
    m.insert(9);
    m.insert(3);
    m.insert(5);

    multiset<int>::iterator itr1 = m.end();    
    cout << *(--itr1) << endl;
    cout << "-----------------" << endl;

    for(multiset<int>::iterator itr2 = m.begin(); itr2 != m.end(); itr2++) {
        cout << *(itr2) << " ";
    }
    cout << endl;

    return 0;
}

