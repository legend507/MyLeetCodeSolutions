#include    <iostream>
#include    <vector>
#include    <string>
using namespace std;


/*
The idea here is brute force.
To check all possible combinations
*/
class Solution {
private:

	void dfs(vector<string> &ret, 
			const string num,
			const int target,
			int curPos,
			string equationSoFar, 
			long cv,
			const char preOp,
			const int preNum
		) {
		
//		cout << equationSoFar << endl;

		/* reach end of num, and cv = target */
		if (curPos == num.size() && cv == target) {
			ret.push_back(equationSoFar);
		}
		else {
			for (int i = 1; i <= num.size()-curPos; i++) {
				long curNum = stol(num.substr(curPos, i));

				if (to_string(curNum).size() != num.substr(curPos, i).size()) continue;

				// try +
				dfs(
					ret, num, target,
					curPos + i,					/*curPos*/
					equationSoFar + '+' + num.substr(curPos, i),
					cv + curNum,
					'+',
					curNum
				);

				// try -
				dfs(
					ret, num, target,
					curPos + i,					/*curPos*/
					equationSoFar + '-' + num.substr(curPos, i),
					cv - curNum,
					'-',
					curNum
				);

				// try *
				//	if previous is ?*preNum, add *curNum
				if (preOp == '*' || preOp == '!') {
					dfs(
						ret, num, target,
						curPos + i,					/*curPos*/
						equationSoFar + '*' + num.substr(curPos, i),
						cv * curNum,
						'*',
						curNum
					);
				}
				//	if previous is ?+preNum, add -preNum+preNum*curNum
				else if(preOp == '+'){
					dfs(
						ret, num, target,
						curPos + i,					/*curPos*/
						equationSoFar + '*' + num.substr(curPos, i),
						cv - preNum + preNum*curNum,
						'+',
						preNum*curNum
					);
				}
				//	if previous is ?-preNum, add +preNum-preNum*curNum
				else {
					dfs(
						ret, num, target,
						curPos + i,					/*curPos*/
						equationSoFar + '*' + num.substr(curPos, i),
						cv + preNum - preNum * curNum,
						'-',
						preNum*curNum
					);
				}

				
			}
		}
	}

public:
	vector<string> addOperators(string num, int target) {
		vector<string> ret;

		if (num.empty())	return ret;

		for (int i = 1; i <= num.size(); i++) {
			long curNum = stol(num.substr(0, i));

			cout << curNum << endl;
			if (to_string(curNum).size() != num.substr(0, i).size()) continue;
			dfs(
				ret, num, target,
				i,						/*curPos*/
				num.substr(0, i),		/*equationSoFar*/
				stol(num.substr(0, i)),	/*cv*/
				'!',
				stol(num.substr(0, i))	/*preNum*/
			);
		}

		return ret;
	}
};

int main() {
	string str = { "2147483647" };
	//cout << str.substr(0, 1);	// output is 1
	Solution s;
	vector<string> ret;

	ret = s.addOperators(str, 2147483647);

	cout << "------------------" << endl;
	for (auto itr : ret) {
		cout << itr << endl;
	}

	system("pause");
	return 0;
}
