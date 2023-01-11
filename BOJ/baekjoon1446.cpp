// Áö¸§±æ
// https://www.acmicpc.net/problem/1446
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

typedef pair<int, int> pii;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);

	int n, d;
	cin >> n >> d;

	vector<int> distances(d+1);
	for (int i = 0; i <= d; i++) {
		distances[i] = i;
	}

	vector<vector<pii>> graph(d+1);

	for (int i = 0; i < n; i++) {
		int v1, v2, w;
		cin >> v1 >> v2 >> w;

		graph[v1].push_back({ v2, w });
	}

	queue<int> q;
	for (int i = 0; i <= d; i++) {
		q.push(i);

		if (i)
			distances[i] = min(distances[i], distances[i - 1] + 1);

		while (!q.empty()) {
			int curr = q.front(); q.pop();

			for (pii shortcut : graph[curr]) {
				if (shortcut.first > d)
					continue;

				if (distances[shortcut.first] > distances[curr] + shortcut.second) {
					distances[shortcut.first] = distances[curr] + shortcut.second;
					q.push(shortcut.first);
				}
			}
		}
		
	}

	cout << distances[d] << "\n";

	return 0;
}