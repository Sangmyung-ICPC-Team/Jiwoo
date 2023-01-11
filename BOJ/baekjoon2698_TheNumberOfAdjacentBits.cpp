// 인접한 비트의 개수
#include <iostream>
#include <vector>

using namespace std;

int num_of_adjacent_bits(int n, int k)
{
	if (n == 1)
		return 0;

	vector< vector < vector<int> > > dp; // (101)*(100)*2

	dp.assign(101, vector < vector<int> >(100, vector<int>(2, 0)));
	dp[1][0][0] = 1, dp[1][0][1] = 1;

	for (int i = 2; i <= n; i++) {
		for (int j = 0; j < i; j++) {
			if (j == i - 1)
				dp[i][j][0] = 0, dp[i][j][1] = 1;
			else {
				dp[i][j][0] = dp[i - 1][j][0] + dp[i - 1][j][1];
				dp[i][j][1] = dp[i - 1][j][0];
				if (j - 1 >= 0)
					dp[i][j][1] += dp[i - 1][j - 1][1];
			}
		}
	}

	return dp[n][k][0] + dp[n][k][1];
}

int main(void)
{
	int t;
	int n, k;

	cin >> t;

	while (t) {
		cin >> n >> k;
		cout << num_of_adjacent_bits(n, k) << "\n";
		t--;
	}

	return 0;
}