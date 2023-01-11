// д╥гн
// https://www.acmicpc.net/problem/4796
#include <iostream>

using namespace std;

int main(void)
{
	int P = -1, L = -1, V = -1;
	int i = 1;
	int days = 0;

	while (true) {
		cin >> P >> L >> V;

		if (P + L + V == 0)
			break;

		int days = 0, rest = 0;
		days += (V / L) * P;
		rest = V % L;

		if (rest <= P)
			days += rest;
		else
			days += P;

		printf("Case %d: %d\n", i++, days);
	}

	return 0;
}