// ½ºÆ¼Ä¿
// https://www.acmicpc.net/problem/9465

#include <iostream>
#include <vector>

using namespace std;

int main(void)
{
	cin.tie(NULL);
	cout.tie(NULL);

	int t;
	cin >> t;

	while (t--) {
		int n;
		cin >> n;

		vector<vector<int>> arr(2, vector<int>(n + 1, 0));
		vector<vector<int>> dp(2, vector<int>(n + 1, 0));

		for (int i = 1; i <= n; i++)
			cin >> arr[0][i];

		for (int i = 1; i <= n; i++)
			cin >> arr[1][i];


		dp[0][1] = arr[0][1];
		dp[1][1] = arr[1][1];
	
		for (int i = 2; i <= n; i++) {
			dp[0][i] = arr[0][i] + max(dp[1][i - 1], dp[1][i - 2]);
			dp[1][i] = arr[1][i] + max(dp[0][i - 1], dp[0][i - 2]);
		}

		cout << max(dp[0][n], dp[1][n]) << "\n";
	}
	return 0;
}