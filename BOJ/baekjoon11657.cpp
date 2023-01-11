// 타임 머신
// https://www.acmicpc.net/problem/11657
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

int main(void)
{
	const int INF = 987654321;
	
	int n, m;
	cin >> n >> m;

	vector<pair<pii, int>> edge_list;

	for (int i = 0; i < m; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		edge_list.push_back(make_pair(make_pair(a, b), c));
	}
	
	vector<long long> distances((n + 1), INF);
	distances[1] = 0;

	for (int i = 1; i < n; i++) { // n - 1번 반복
		for (int j = 0; j < m; j++) { // edge relaxation
			int s, e, cost;

			s = edge_list[j].first.first;
			e = edge_list[j].first.second;
			cost = edge_list[j].second;

			if (distances[s] == INF) continue;

			if (distances[s] + cost < distances[e])
				distances[e] = distances[s] + cost;

		}
	}

	// 모든 edge에 대하여 edge relaxation 한번 더 수행하여 음수 사이클 여부 판별
	bool isOddCycle = false;
	for (int j = 0; j < m; j++) { // edge relaxation
		int s, e, cost;

		s = edge_list[j].first.first;
		e = edge_list[j].first.second;
		cost = edge_list[j].second;

		if (distances[s] == INF) continue;

		if (distances[s] + cost < distances[e]) {
			isOddCycle = true; break;
		}
	}

	if (isOddCycle)
		cout << -1 << "\n";
	else {
		for (int i = 2; i <= n; i++) {// 2~n번째 도시까지의 거리 출력
			if (distances[i] == INF)
				cout << -1 << "\n";
			else
				cout << distances[i] << "\n";
		}
	}

	return 0;
}