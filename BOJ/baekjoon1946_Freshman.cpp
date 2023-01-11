// 신입사원
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

void solve() {
	int n;
	cin >> n;
	
	vector<pair<int, int>> people;

	for (int i = 0; i < n; i++) {
		int g1, g2;
		cin >> g1 >> g2;

		people.push_back({ g1, g2 });
	}

	sort(people.begin(), people.end()); // 내림차순 정렬

	int answer = 0;
	int min_grade = n + 1;
	for (int i = 0; i < n; i++) {
		if (people[i].second < min_grade) {
			min_grade = people[i].second;
			answer++;
		}
	}

	cout << answer << '\n';
}

int main(void)
{
	int t;
	cin >> t;

	while (t--) {
		solve();
	}
	return 0;
}