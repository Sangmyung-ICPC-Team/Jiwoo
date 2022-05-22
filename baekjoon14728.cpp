// 벼락치기
// https://acmicpc.net/problem/14728
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, t;
	cin >> n >> t;

	vector<int> dp(t + 1, 0);

	for (int i = 0; i < n; i++) {
		int k, s;
		cin >> k >> s;
		
		// for문을 뒤부터 실행
		// 중복된 값을 누적해서 더해주는 현상을 피하기 위함
		for (int j = t; j >= k; j--) {
			dp[j] = max(dp[j], dp[j - k] + s);
		}
	}
	
	cout << dp[t];

	return 0;
}