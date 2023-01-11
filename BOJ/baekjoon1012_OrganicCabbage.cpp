// 유기농 배추
#include <iostream>
#include <vector>
#include <stack>
#include <cstring>

using namespace std;

bool visited[51][51] = { false, };
int gragh[51][51] = { 0, };
int adj_pos[4][2] = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };

void dfs(int x, int y, int n, int m)
{
	stack <pair<int, int >> s;
	s.push({ x, y });

	while (!s.empty()) {
		auto curr = s.top(); s.pop();
		visited[curr.first][curr.second] = true;

		for (auto adj : adj_pos) {
			int curr_x = curr.first + adj[0];
			int curr_y = curr.second + adj[1];

			if (curr_x < 0 || curr_x >= n || curr_y < 0 || curr_y >= m)
				continue;

			if (gragh[curr_x][curr_y] && !visited[curr_x][curr_y])
				s.push({ curr_x, curr_y });
		}
	}
	return;
}

int min_num_of_worm(int n, int m)
{
	int cnt = 0;

	for (int i = 0; i < n; i++)
		for (int j = 0; j < m; j++)
			if (gragh[i][j] && !visited[i][j]) {
				dfs(i, j, n, m);
				cnt++;
			}

	return cnt;
}

int main(void)
{
	int t;
	int m, n, k;
	int x, y;

	cin >> t;

	while (t) {
		
		cin >> m >> n >> k;

		for (int i = 0; i < k; i++) {
			cin >> x >> y; // x: 열 정보, y: 행 정보
			gragh[y][x] = 1;
		}
		cout << min_num_of_worm(n, m) << "\n";

		memset(visited, false, sizeof(visited));
		memset(gragh, 0, sizeof(gragh));
		t--;
	}
	return 0;
}