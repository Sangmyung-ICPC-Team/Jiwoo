// 소트인사이드
#include <iostream>
#include <algorithm>
//#include <string>

using namespace std;

int main()
{
	string s;
	cin >> s;
	//sort(s.begin(), s.end(), greater<char>());
	sort(s.rbegin(), s.rend());
	cout << s;
	return 0;
}