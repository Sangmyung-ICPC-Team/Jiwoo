// ÀÛ¾÷
// https://www.acmicpc.net/problem/2056
#include <iostream>
#include <vector>

using namespace std;
const int INF = 100001;

int getMinTime(int n, vector<vector<int>> &pre, vector<int> &time) {
	vector<int> dp(n + 1, 0);
	dp[1] = time[1];

	int total_time = 0;
	for (int i = 2; i <= n; i++) {
		for (int p : pre[i]) {
			dp[i] = max(dp[i], dp[p]);
		}
		dp[i] += time[i];
		total_time = max(total_time, dp[i]);
	}

	return total_time;
}

int main()
{
	int n;
	cin >> n;

	vector<vector<int>> pre(n + 1, vector<int>());
	vector<int> time(n + 1, 0);

	for (int i = 1; i <= n; i++) {
		cin >> time[i];

		int p_nums;
		cin >> p_nums;

		for (int j = 0; j < p_nums; j++) {
			int p; cin >> p;
			pre[i].push_back(p);
		}
	}

	cout << getMinTime(n, pre, time) << "\n";

	return 0;
}