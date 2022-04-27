// °ÅÁþ¸»
// https://www.acmicpc.net/problem/1043
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
const int MAX_VALUE = 51;

vector<vector<int>> attendeeList(MAX_VALUE);
vector<vector<int>> partyList(MAX_VALUE);
bool alreadyKnow[51];
bool visited[51];

int getNumberOfPossibleParties(queue<int> &knowers)
{
	int cnt = 0;

	while (!knowers.empty()) {
		auto knower = knowers.front(); knowers.pop();

		for (auto party : partyList[knower]) {
			if (!visited[party]) {
				cnt++;
				visited[party] = true;

				for (auto& attendee : attendeeList[party]) {
					if (!alreadyKnow[attendee]) {
						alreadyKnow[knower] = true;
						knowers.push(attendee);
					}
				}
			}
		}
	}

	return cnt;
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	int k;
	cin >> k;

	if (k == 0)
		cout << m << "\n";
	else {
		queue<int> knowers;

		for (int i = 0; i < k; i++) {
			int knower;
			cin >> knower;

			knowers.push(knower);
			alreadyKnow[knower] = true;
		}

		for (int i = 1; i <= m; i++) {
			int attendeeNum;
			cin >> attendeeNum;

			for (int j = 0; j < attendeeNum; j++) {
				int attendee;
				cin >> attendee;

				attendeeList[i].push_back(attendee);
				partyList[attendee].push_back(i);
			}
		}

		cout << m - getNumberOfPossibleParties(knowers) << "\n";
	}

	return 0;
}