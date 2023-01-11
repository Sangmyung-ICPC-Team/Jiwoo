#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

char field[500][500];

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int r, c;
    cin >> r >> c;

    vector<pii> wp = vector<pii>();


    for(int i=0; i<r; i++) {
        for(int j=0; j<c; j++) {
            cin >> field[i][j];

            if (field[i][j] == '.') {
                field[i][j] = 'D';
            } else if (field[i][j] == 'W') {
                wp.push_back({i, j});
            }
        }
    }

    int sheepIsSafe = 1;
    for(pii w : wp) {
        for(int i=0; i<4; i++) {
            int nx = w.first + dx[i];
            int ny = w.second + dy[i];
            if (nx < 0
                        || nx >= r
                        || ny < 0
                        || ny >= c)
                continue;

            if (field[nx][ny] == 'S') {
               sheepIsSafe = 0;
               break;
            }
        }

        if (!sheepIsSafe) break;

    }


    if(!sheepIsSafe) cout << 0 << endl;
    else {
        cout << 1 << endl;

        for(int i=0; i<r; i++) {
            for(int j=0; j<c; j++) {
                cout << field[i][j];
            }

            cout << endl;
        }
    }

    return 0;
}
