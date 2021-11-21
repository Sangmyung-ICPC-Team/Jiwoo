// 제 2회 IUPC는 잘 개최될 수 있을까?
// https://www.acmicpc.net/problem/12788
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void)
{
	int n, m, k;
	cin >> n;
	cin >> m >> k;

	vector<int> arr(n, 0);
	for (int i = 0; i < n; i++)
		cin >> arr[i];

	sort(arr.rbegin(), arr.rend());

	int ans = 0, total = 0;
	bool isEnough = false;
	for (int i = 0; i < n; i++) {
		total += arr[i];
		ans++;
		if (total >= m * k) {
			isEnough = true;
			break;
		}
	}

	if (isEnough)
		cout << ans << '\n';
	else
		cout << "STRESS\n";

	return 0;
}