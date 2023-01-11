// 내일 할거야
// https://www.acmicpc.net/problem/7983
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

bool cmp(pii a, pii b) {
    return a.second > b.second;
}

int main(void)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<pii> arr;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        arr.push_back({ a, b });

    }

    sort(arr.begin(), arr.end(), cmp);

    int start = arr[0].second;
    for (auto schedule : arr) {
        if (start > schedule.second) {
            start = schedule.second;
        }

        start -= schedule.first;
    }

    cout << start << endl;

    return 0;
}