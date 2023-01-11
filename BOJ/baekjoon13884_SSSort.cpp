// 삭삽 정렬
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int p;
	cin >> p;

	while (p--) {
		int k, n;
		cin >> k >> n;

		vector<int> arr(n, 0);
		vector<int> sortedArr(n, 0);
		for (int i = 0; i < n; i++) {
			cin >> arr[i];
			sortedArr[i] = arr[i];
		}

		sort(sortedArr.begin(), sortedArr.end());

		// 원래부터 정순인 원소 개수 세기
		// 전체 원소 개수 - 정순 원소 개수 = 정렬해야 할 원소 개수
		int answer = 0;
		int j = 0;

		for(int i=0;i<n;i++)
			if (sortedArr[j] == arr[i]) {
				answer++;
				j++;
			}

		cout << k << ' ' << n - answer << '\n';

	}
	return 0;
}