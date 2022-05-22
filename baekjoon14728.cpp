// ����ġ��
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
		
		// for���� �ں��� ����
		// �ߺ��� ���� �����ؼ� �����ִ� ������ ���ϱ� ����
		for (int j = t; j >= k; j--) {
			dp[j] = max(dp[j], dp[j - k] + s);
		}
	}
	
	cout << dp[t];

	return 0;
}