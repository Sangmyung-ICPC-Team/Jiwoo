// 바닥 장식
// https://www.acmicpc.net/problem/1388
#include <iostream>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

const int MAX_LEN = 50;

int dx[2] = { 0, 1 };
int dy[2] = { 1, 0 };

int n, m;
char floors[MAX_LEN][MAX_LEN] = { " ", };
bool visited[MAX_LEN][MAX_LEN] = { false, };

void bfs(int x, int y, int mode) // mode == 0: 가로, mode == 1: 세로
{
	queue<pii> q;

	visited[x][y] = true;
	q.push({ x, y });

	while (!q.empty()) {

		pii curr = q.front(); q.pop();

		int nx = curr.first + dx[mode];
		int ny = curr.second + dy[mode];

		if (nx >= n || ny >= m)
			continue;
	
		if (!visited[nx][ny] && floors[x][y] == floors[nx][ny]) {
			visited[nx][ny] = true;
			q.push({ nx, ny });
		}
	}
}

int main()
{
	cin >> n >> m;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			cin >> floors[i][j];

	int cnt = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!visited[i][j]) {
				cnt++;
				if (floors[i][j] == '-')
					bfs(i, j, 0);
				else
					bfs(i, j, 1);
			}
		}
	}

	cout << cnt << "\n";
	
	return 0;
}