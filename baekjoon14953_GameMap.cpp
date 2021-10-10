// ICPC Regionals Asia Pacific Korea Asia Regional - Daejeon 2017 C¹ø
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int dfs(vector<vector<int>>& g, vector<int>& degree, vector<int>& dp, int start_node)
{
	if (dp[start_node])
		return dp[start_node];
	dp[start_node]++;

	for (auto adj : g[start_node])
		if (degree[adj] > degree[start_node])
			dp[start_node] = max(dp[start_node], dfs(g, degree, dp, adj) + 1);

	return dp[start_node];
}

int main(void)
{
	int n, m;
	cin >> n >> m;

	vector<vector<int>> gragh(n);
	vector<int> degree(n, 0);
	vector<int> dp(n, 0);

	for (int i = 0; i < m; i++) {
		int c1, c2;
		cin >> c1 >> c2;

		gragh[c1].push_back(c2);
		gragh[c2].push_back(c1);

		degree[c1]++;
		degree[c2]++;
	}

	int answer = 0;
	for (int i = 0; i < n; i++)
		answer = max(answer, dfs(gragh, degree, dp, i));

	cout << answer << '\n';

	return 0;
}