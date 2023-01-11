// ��� ����
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

		// �������� ������ ���� ���� ����
		// ��ü ���� ���� - ���� ���� ���� = �����ؾ� �� ���� ����
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