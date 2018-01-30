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
    m.insert(0);

    cout << *(m.end()) << endl;

    vector<int> v;

    v.push_back(0);
    v.push_back(1);
    v.push_back(7);
    v.push_back(9);
    v.push_back(3);
    v.push_back(0);

    cout << *(v.end()) << endl;

    return 0;
}

