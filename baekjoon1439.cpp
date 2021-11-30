// 뒤집기
// https://www.acmicpc.net/problem/1439
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
	string s;
	cin >> s;

	int zeros = 0, ones = 0; // 연속된 0, 1 substring의 개수

	for (int i = 0; i < s.length(); i++) {
		if (s[i] != s[i + 1]) {
			if (s[i] == '0')
				zeros++;
			else
				ones++;
		}
	}

	cout << min(zeros, ones) << '\n';

	return 0;
}