// Ä£±¸
// https://www.acmicpc.net/problem/11657
#include <iostream>
#include <vector>

using namespace std;

void find_friend_network(int n, vector<vector<int>> &v)
{
	for (int i = 0; i < n; i++) { // round #i
		for (int j = 0; j < n; j++) {

			if (i == j)
				continue;

			for (int k = 0; k < n; k++) {

				if (j == k)
					continue;

				if (v[j][k] > v[j][i] + v[i][k])
					v[j][k] = v[j][i] + v[i][k];

			}
		}
	}
}

int main(void)
{
	int n;
	cin >> n;

	const int INF = 100;
	vector<vector<char>> friends(n, vector<char>(n));
	vector<vector<int>> two_friends(n, vector<int>(n));

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			cin >> friends[i][j];
			two_friends[i][j] = (friends[i][j] == 'Y') ? 1 : INF;
		}
	}

	find_friend_network(n, two_friends);

	int max_cnt = 0;
	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = 0; j < n; j++)
			if (two_friends[i][j] <= 2)
				cnt++;

		max_cnt = max(max_cnt, cnt);
	}

	cout << max_cnt << '\n';

	return 0;
}