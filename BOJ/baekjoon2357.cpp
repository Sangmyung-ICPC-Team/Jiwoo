// ÃÖ¼Ú°ª°ú ÃÖ´ñ°ª
// https://www.acmicpc.net/problem/2357
#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

pii init(int start, int end, int node, vector<double> &tree, vector<pii> &seg_tree)
{
	if (start == end) {
		seg_tree[node] = { tree[start], tree[start] };
		return seg_tree[node];
	}
	else {
		int mid = (start + end) / 2;

		pii left_node = init(start, mid, node << 1, tree, seg_tree);
		pii right_node = init(mid + 1, end, (node << 1) + 1, tree, seg_tree);
		seg_tree[node].first = min(left_node.first, right_node.first);
		seg_tree[node].second = max(left_node.second, right_node.second);

		return seg_tree[node];
	}
}

pii getPartialMinMax(int start, int end, int node, int left, int right, vector<double>& tree, vector<pii>& seg_tree)
{
	if (end < left || start > right) 
		return { 2147483647, 0 };
	else if (start >= left && end <= right) {
		return seg_tree[node];
	}
	else {
		int mid = (start + end) / 2;

		pii left_node = getPartialMinMax(start, mid, node << 1, left, right, tree, seg_tree);
		pii right_node = getPartialMinMax(mid + 1, end, (node << 1) + 1, left, right, tree, seg_tree);

		return { min(left_node.first, right_node.first), max(left_node.second, right_node.second) };
	}
}

int main(void)
{
	cin.tie(NULL);
	cout.tie(NULL);

	int n, m;
	cin >> n >> m;

	vector<double> tree(n + 1);
	vector<pii> seg_tree(n << 2);

	for (int i = 1; i <= n; i++)
		cin >> tree[i];

	init(1, n, 1, tree, seg_tree);

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;

		pii result = getPartialMinMax(1, n, 1, a, b, tree, seg_tree);

		cout << result.first << " " << result.second << "\n";
	}

	return 0;
}