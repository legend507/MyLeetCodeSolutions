/*

*/

#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <queue>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <stack>
using namespace std;

/*
当检索时，
用此Class来存储两个Person之间的Path
*/
class PathNode {
public:
	int formerP;
	int thisP;
	PathNode(int x, int y) : formerP(x), thisP(y) {};
};
class FindPath {
	unordered_set<int> visited;
	unordered_set<PathNode> toVisit;
public:
	void findShortestPath(Person& p1, Person& p2) {
		for (auto oneFriend : p1.friendID) {
			toVisit.emplace(PathNode(p1.pID, oneFriend));
		}

		while (!toVisit.empty()) {
			auto itr = toVisit.begin();
			int thisP = itr->thisP;			//

			if (thisP == p2.pID) {
				// found target
			}


		}

	}
};

/*
每个Person有自己的attribute
以及自己的Friends List
*/
class Person {
public:
	int pID;
	string name;
	unordered_set<int>	friendID;

	Person(int x, string y) : pID(x), name(y) {};
};

/*
一个Machine来记录此Machine周围的Person
*/
class Machine {
public:
	int mID;
	unordered_map<int, Person&> personList;

	Machine(int x) : mID(x) {};

	// get person address by person ID
	Person& getPersonByID(int pID) {
		return personList[pID];
	}
};

/*
用一个Server来记录所有Machine
这个Server应该有
	1 一个List来对应所有machine ID和Machine实体
	2 一个List来记录所有Person，并map到那个Person所在的Machine
注意，不一定要用Machine&, 如果某个Machine是远距离的话，用Machine IP也行
*/
class Server {
public:
	int sID;
	// a map, mapping machindID with Machine address
	unordered_map<int, Machine&> machineList;
	// a map, mapping personID (unique) to Machine ID
	unordered_map<int, int> personToMachine;

	Server(int x) : sID(x) {};

	// get machine address by ID
	Machine& getMachineByID(int mID) {
		return machineList[mID];
	}

	// get machine ID by person on it
	//	person is stored in machine
	int getMachineIDByPersionID(int pID) {
		return personToMachine[pID];
	}

	// get person address by person ID
	Person& getPersonByID(int pID) {
		// 1st. find the machine
		// 2nd. fidn person
		return getMachineByID(pID).getPersonByID(pID);
	}
};

int main() {


    system("pause");
    return 0;
}

