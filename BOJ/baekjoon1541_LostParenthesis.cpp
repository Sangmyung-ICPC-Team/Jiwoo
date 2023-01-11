// ÀÒ¾î¹ö¸° °ıÈ£
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string input;
	cin >> input;

	string num = "";
	int result = 0;
	bool minus = false;

	for (int i = 0; i <= input.size(); i++) {
		if (input[i] == '-' || input[i] == '+' || input[i] == '\0') {
			if (minus)
				result -= stoi(num);
			else
				result += stoi(num);
			num = "";
		}else
			num += input[i];

		if (input[i] == '-')
			minus = true;
	}

	cout << result << '\n';

	return 0;
}