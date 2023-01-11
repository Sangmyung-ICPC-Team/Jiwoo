// ICPC Seoul Nationalwide Internet Competition 2021 I¹ø
#include <iostream>
#include <queue>

using namespace std;

struct Node {
	int n1, n2, n3;

	Node(int a, int b, int c) {
		n1 = a; n2 = b; n3 = c;
	}

	bool operator<(const Node& b) const
	{
		if (n1 == b.n1) {
			if (n2 == b.n2)
				return n3 > b.n3;
			else
				return n2 > b.n2;
		}
		else
			return n1 > b.n1;
	}
};

int main()
{
	int n;
	cin >> n;

	priority_queue<Node> pq;

	for (int i = 0, num, r1, r2, r3; i < n; i++) {
		cin >> num >> r1 >> r2 >> r3;

		pq.push(Node(r1 * r2 * r3, r1 + r2 + r3, num));
	}

	for (int i = 0; i < 3; i++) {
		cout << pq.top().n3 << ' '; pq.pop();
	}

	cout << '\n';
	return 0;
}