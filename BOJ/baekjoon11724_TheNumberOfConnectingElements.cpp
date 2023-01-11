// 연결 요소의 개수
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>

const int MAX = 1000 + 1;
using namespace std;

bool visited[MAX] = { false };
vector<int> gragh[MAX];

void dfs(int node)
{
	stack<int> s;
	s.push(node);
	while (!s.empty()) {
		auto curr = s.top(); s.pop();
		visited[curr] = true;

		for (auto adj : gragh[curr])
			if (!visited[adj])
				s.push(adj);
	}
}

int main(void)
{
	int cnt = 0;
	int n, m;
	cin >> n >> m;
	
	for (int i = 0; i < m; i++) {
		int n1, n2;
		cin >> n1 >> n2;

		gragh[n1].push_back(n2);
		gragh[n2].push_back(n1);
	}

	for (int i = 1; i <= n; i++)
		if (!visited[i]) {
			cnt++;
			dfs(i);
		}

	cout << cnt << "\n";

	return 0;
}