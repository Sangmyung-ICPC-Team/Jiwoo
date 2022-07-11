#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool compare(vector<int>& a, vector<int>& b)
{
	return a[0] - a[1] > b[0] - b[1];
}

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n, x;

	cin >> n >> x;

	vector<vector<int>> menu(n, vector<int>(2));

	for (int i = 0; i < n; i++) {
		cin >> menu[i][0] >> menu[i][1];
	}

	sort(menu.begin(), menu.end(), compare);

	int result = 0;
	int cost = 1000 * n;
	for (int today = 0; today < n; today++) {
		if ((x >= cost + 4000) && (menu[today][0] > menu[today][1])) {
			cost += 4000;
			result += menu[today][0];
		}
		else {
			result += menu[today][1];
		}
	}

	cout << result << endl;

	return 0;
}