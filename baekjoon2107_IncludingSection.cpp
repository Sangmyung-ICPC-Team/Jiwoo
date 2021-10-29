// 포함하는 구간
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void)
{
	int n;
	cin >> n;

	vector<pair<int, int>> sections(n);

	for (int i = 0; i < n; i++) {
		int s, e;
		cin >> s >> e;
		sections[i] = { s, e };
	}

	sort(sections.begin(), sections.end(), less<>());

	int max_cnt = 0;
	for (int i = 0; i < n; i++) {
		int cnt = 0;
		for (int j = i + 1; j < n; j++) {
			if (sections[i].first < sections[j].first &&
				sections[i].second > sections[j].second)
				cnt++;
		}
		max_cnt = max(max_cnt, cnt);
	}

	cout << max_cnt << '\n';
	return 0;
}