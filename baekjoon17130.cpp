// 토끼가 정보섬에 올라온 이유
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

bool visited[1001][1001];
char island[1001][1001];
int dp[1001][1001];
int dx[3] = { -1, 0, 1 };
int dy = 1;

int n, m;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	int rx, ry; // 토끼 초기 위치

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			cin >> island[i][j];
			dp[i][j] = 0;
			visited[i][j] = false;

			if (island[i][j] == 'R') {
				rx = i;
				ry = j;
			}
		}
	}

	bool canEscape = false;
	int maxCarrots = 0;

	queue<pii> q;
	q.push({ rx, ry });

	while (!q.empty()) {
		pii curr = q.front(); q.pop();
		int x = curr.first;
		int y = curr.second;

		if (visited[x][y])
			continue;
		visited[x][y] = true;

		if (island[x][y] == 'C') {
			dp[x][y]++;
		}
		else if (island[x][y] == 'O') {
			maxCarrots = max(maxCarrots, dp[x][y]);
			canEscape = true;
		}
		for (int i = 0; i < 3; i++) {
			int nx = x + dx[i];
			int ny = y + dy;

			if (nx < 1 || nx > n || ny < 1 || ny > m)
				continue;

			if (!visited[nx][ny] && island[nx][ny] != '#') {
				q.push({ nx, ny });
				dp[nx][ny] = max(dp[nx][ny], dp[x][y]);
			}
		}
	}

	if (canEscape)
		cout << maxCarrots << "\n";
	else
		cout << "-1\n";

	return 0;
}