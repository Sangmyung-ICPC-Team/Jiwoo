// 암호 만들기
// https://www.acmicpc.net/problem/1759
#include <iostream>
#include <algorithm>

using namespace std;

int L = 0, C = 0;
char characters[16];

void solve(string pwd, int currPos, int currLen)
{
	if (currLen == L) {
		int vowel_nums = 0;
		int consonant_nums = 0;
		for (int i = 0; i < L; i++) {
			if (pwd[i] == 'a' || pwd[i] == 'e' || pwd[i] == 'i' || pwd[i] == 'o' || pwd[i] == 'u')
				vowel_nums++;
			else
				consonant_nums++;

			if (vowel_nums >= 1 && consonant_nums >= 2) {
				cout << pwd << "\n";
				break;
			}
		}
	}
	else if (currLen > L)
		return;
	else {
		for (int i = currPos + 1; i < C; i++)
			solve(pwd + characters[i], i, currLen + 1);
	}
}

int main(void)
{
	cin.tie(NULL);
	cout.tie(NULL);
	
	cin >> L >> C;
	
	for (int i = 0; i < C; i++) {
		cin >> characters[i];
	}

	sort(characters, characters + C);

	solve("", -1, 0);

	return 0;
}