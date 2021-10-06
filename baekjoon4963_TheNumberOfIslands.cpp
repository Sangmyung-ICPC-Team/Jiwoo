// ¼¶ÀÇ °³¼ö
#include <iostream>
#include <algorithm>
#include <stack>
#include <cstring>

using namespace std;

int gragh[51][51] = { 0 };
bool visited[51][51] = { false };

int dir_x[8] = { -1, 1, 0, 0, -1, 1, -1, 1 };
int dir_y[8] = { 0, 0 , -1, 1, -1, 1, 1, -1 };

void numOfIslands(int x, int y, int n, int m)
{
	stack<pair<int, int>> s;

	s.push(make_pair(x, y));

	while (!s.empty()) {
		auto curr = s.top(); s.pop();
		visited[curr.first][curr.second] = true;

		for (int i = 0; i < 8; i++) {
			int next_x = curr.first + dir_x[i];
			int next_y = curr.second+ dir_y[i];
		
			if (next_x < 0 || next_x >= n || next_y < 0 || next_y >= m)
				continue;

			if (gragh[next_x][next_y] && !visited[next_x][next_y])
				s.push(make_pair(next_x, next_y));
		}
	}
}

int main()
{
	int w, h;
	int cnt;

	while (true) {
		cnt = 0;
		cin >> w >> h;

		if (w == 0 && h == 0) break;

		for (int i = 0; i < h; i++)
			for (int j = 0; j < w; j++)
				cin >> gragh[i][j];

		for (int i = 0; i < h; i++)
			for(int j=0; j<w; j++)
				if (gragh[i][j] && !visited[i][j]) {
					cnt++;
					numOfIslands(i, j, h, w);
				}

		cout << cnt << '\n';

		memset(visited, false, sizeof(visited));
		memset(gragh, 0, sizeof(gragh));

	}
	return 0;
}