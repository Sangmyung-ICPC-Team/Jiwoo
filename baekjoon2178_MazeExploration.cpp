// 미로 탐색
#include <iostream>
#include <algorithm>
//#include <vector>
#include <queue>
//#define INF 10000;

const int INF = 10000;
using namespace std;

int maze[101][101] = { 0, };
int dist[101][101];

int dir_x[4] = { -1, 1, 0, 0 };
int dir_y[4] = { 0, 0, -1, 1 };

int minNumOfBlock(int n, int m)
{
	queue < pair<int, int>> q;
	dist[1][1] = 1;
	
	q.push(make_pair(1, 1));

	while (!q.empty()) {
		auto curr = q.front(); q.pop();

		for (int i = 0; i < 4; i++) {
			
			int next_x = curr.first + dir_x[i];
			int next_y = curr.second + dir_y[i];

			if (next_x <= 0 || next_x > n || next_y <= 0 || next_y > m) // 범위 체크
				continue;

			if (dist[next_x][next_y] != INF) // visited 역할
				continue;

			if (maze[next_x][next_y] && (dist[next_x][next_y] > dist[curr.first][curr.second] + 1)) {
				dist[next_x][next_y] = dist[curr.first][curr.second] + 1;
				q.push(make_pair(next_x, next_y));
			}

		}
	}

	return dist[n][m];
}

int main(void)
{
	int n, m;
	cin >> n >> m;

	for (int i = 1; i <= n; i++) {
		string row;
		cin >> row;
		for (int j = 1; j <= m; j++)
			maze[i][j] = row[j-1] - '0';
	}

	for (int i = 1; i <= n; i++) {
		fill(dist[i], dist[i] + (m + 1), INF);
		//for (int j = 1; j <= m; j++)
		//	cout << dist[i][j] << ' ';
		//cout << '\n';
	}

	cout << minNumOfBlock(n, m) << "\n";

	return 0;
}