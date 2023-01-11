// 30
// https://www.acmicpc.net/problem/10610
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	string str;
	cin >> str;

	sort(str.begin(), str.end(), greater<>());

	if (str[str.length() -1] != '0')
		cout << -1 << endl;
	else {
		long long total = 0;
		for (auto ch : str) {
			total += (long long)(ch - '0');
		}

		if (total % 3 == 0)
			cout << str << endl;
		else
			cout << -1 << endl;
	}
	return 0;
}