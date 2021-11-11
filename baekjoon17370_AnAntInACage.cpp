// 육각형 우리 속의 개미
// https://www.acmicpc.net/problem/17370

#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

const int dir[2][3][2] = {
	{ { -1, 0 }, { 1, -1 }, { 1, 1 } },
	{ { 1, 0 }, { -1, 1 }, { -1, -1 } }
};

int n, answer = 0;
bool visited[1'000][1'000];

void dfs(int prev, pii curr, int type, int cnt) {
	if (cnt > n)
		return;

	if (visited[curr.first][curr.second]) {
		if (cnt == n)
			answer++;
	}
	else {
		visited[curr.first][curr.second] = true;

		for (int i = 0; i < 3; i++) {
			if (i == prev)
				continue;

			pii next = {
				curr.first + dir[type][i][0],
				curr.second + dir[type][i][1]
			};

			dfs(i, next, !type, cnt + 1);
		}

		visited[curr.first][curr.second] = false;
	}
}

int main(void)
{
	cin >> n;

	visited[100][100] = true;
	dfs(0, { 101, 100 }, 0, 0);

	cout << answer << '\n';

	return 0;
}
