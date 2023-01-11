#include <iostream>

using namespace std;

typedef pair<int, int> pii;


int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};


int field[51][51];
int newField[51][51];

int R, C;

int airPurifierRoWPos[2];


void spread() {
    for(int i=1; i<=R; i++) {
        for(int j=1; j<=C; j++) {
            if (field[i][j] != 0) {

                int subValue = field[i][j] / 5;

                for (int p=0; p<4; p++) {

                    int nx = i + dx[p];
                    int ny = j + dy[p];

                    if (nx < 1 || nx > R || ny < 1 || ny > C) {
                        continue;
                    }

                    if (field[nx][ny] == -1) {
                        continue;
                    }

                    newField[nx][ny] += subValue;
                    field[i][j] -= subValue;
                }

            }
        }
    }
}

void afterSpread() {
    for(int i=1; i<=R; i++) {
        for(int j=1; j<=C; j++) {
            field[i][j] += newField[i][j];
            newField[i][j] = 0;
        }
    }
}

void clean() {

    for(int i=airPurifierRoWPos[0]-1; i>1; i--) {
        field[i][1] = field[i-1][1];
    }

    for(int i=1; i<C; i++) {
        field[1][i] = field[1][i+1];
    }

    for(int i=1; i<airPurifierRoWPos[0]; i++) {
        field[i][C] = field[i+1][C];
    }

    for(int i=C; i>2; i--) {
        field[airPurifierRoWPos[0]][i] = field[airPurifierRoWPos[0]][i-1];
    }

    field[airPurifierRoWPos[0]][2] = 0;



    for(int i=airPurifierRoWPos[1]+1; i<R; i++) {
        field[i][1] = field[i+1][1];
    }

    for(int i=1; i<C; i++) {
        field[R][i] = field[R][i+1];
    }

    for(int i=R; i>airPurifierRoWPos[1]; i--) {
        field[i][C] = field[i-1][C];
    }

    for(int i=C; i>2; i--) {
        field[airPurifierRoWPos[1]][i] = field[airPurifierRoWPos[1]][i-1];
    }


    field[airPurifierRoWPos[1]][2] = 0;

}

int totalFindDust() {
    int total = 0;

    for(int i=1; i<=R; i++) {
        for(int j=1; j<=C; j++) {

            // 공기정청기 위치
            if (field[i][j] == -1) {
                continue;
            }

            total += field[i][j];
        }
    }

    return total;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int T;

    cin >> R >> C >> T;
    for(int i=1; i<=R; i++) {
        for(int j=1; j<=C; j++) {
            cin >> field[i][j];
        }

        if (field[i][1] == -1 && airPurifierRoWPos[0] == 0) {
                airPurifierRoWPos[0] = i;
                airPurifierRoWPos[1] = i+1;
            }
    }


    while(T--) {
        spread();
        afterSpread();
        clean();
    }


    cout << totalFindDust() << endl;

    return 0;
}