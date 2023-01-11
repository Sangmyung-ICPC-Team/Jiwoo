// Ÿ�� �ӽ�
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

	for (int i = 1; i < n; i++) { // n - 1�� �ݺ�
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

	// ��� edge�� ���Ͽ� edge relaxation �ѹ� �� �����Ͽ� ���� ����Ŭ ���� �Ǻ�
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
		for (int i = 2; i <= n; i++) {// 2~n��° ���ñ����� �Ÿ� ���
			if (distances[i] == INF)
				cout << -1 << "\n";
			else
				cout << distances[i] << "\n";
		}
	}

	return 0;
}