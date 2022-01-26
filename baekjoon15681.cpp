// Æ®¸®¿Í Äõ¸®
// https://www.acmicpc.net/problem/15681

#include <iostream>
#include <vector>

using namespace std;

int solve(int curr, vector<vector<int>> &tree, vector<int> &size)
{
	if (size[curr] != 0)
		return size[curr];
	
	size[curr] = 1;
	for (int &child : tree[curr]) {
		if (size[child] != 0)
			continue;

		size[curr] += solve(child, tree, size);
	}

	return size[curr];
}

int main(void)
{
	cin.tie(NULL);
	cout.tie(NULL);

	int n, r, q;
	cin >> n >> r >> q;

	vector<vector<int>> tree((n+1), vector<int>());
	vector<int> size(n + 1, 0);

	for (int i = 0; i < n-1; i++) {
		int v1, v2;
		cin >> v1 >> v2;

		tree[v1].push_back(v2);
		tree[v2].push_back(v1);
	}

	//for (int i = 1; i <= n; i++) {
	//	for (int j = 0; j < tree[i].size(); j++)
	//		cout << tree[i][j] << " ";
	//	cout << "\n";
	//}

	solve(r, tree, size);

	for (int i = 0; i < q; i++) {
		int subRoot;
		cin >> subRoot;

		cout << size[subRoot] << "\n";
	}

	return 0;
}