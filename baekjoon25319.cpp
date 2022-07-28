#include <iostream>
#include <vector>
#include <string>
#include <limits.h>

using namespace std;

typedef pair<int, int> pii;

const int NUMBER_OF_ALPHABET = 26;

char field[51][51];

int N, M;
string command = "";


void goToDest(pii curr, pii dest) {

    // 행 위치 맞추기
    if (curr.first < dest.first) { // 목적지보다 위쪽에 있음
        for (int i=0; i< dest.first - curr.first; i++) {
            command += "D";
        }
    } else { // 목적지보다 아래쪽에 있음
        for (int i=0; i< curr.first - dest.first; i++) {
            command += "U";
        }
    }

    // 열 위치 맞추기
    if (curr.second < dest.second) { // 목적지보다 왼쪽에 있음
        for (int i=0; i< dest.second - curr.second; i++) {
            command += "R";
        }
    } else { // 목적지보다 오른쪽에 있음
        for (int i=0; i< curr.second - dest.second; i++) {
            command += "L";
        }
    }

}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    // 아이디에 등장하는 알파벳 i의 개수 -> X(i)
    vector<int> idAlphabet(NUMBER_OF_ALPHABET, 0);

    // 필드에 등장하는 알파벳 i의 개수 -> Y(i)
    vector<vector<pii>> fieldAlphabet(NUMBER_OF_ALPHABET, vector<pii>());

    int S;
    cin >> N >> M >> S;


    // 필드 입력 및 필드에서의 각 알파벳 개수(Y) 카운트
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> field[i][j];
            fieldAlphabet[field[i][j] - 'a'].push_back({i, j});
        }
    }

    // 아이디 입력
    string uid;
    cin >> uid;


    // 아이디에서의 각 알파벳 개수(X) 카운트
    for (int i = 0; i < S; i++) {
        idAlphabet[uid[i] - 'a']++;
    }


    // 최대 강화 횟수(C) 구하기
    long unsigned int C = INT_MAX;
    for (int i = 0; i < NUMBER_OF_ALPHABET; i++) {
        if (idAlphabet[i] == 0) {
            continue;
        }

        C = min(C, fieldAlphabet[i].size() / idAlphabet[i]);
    }


    // 초기 위치 (0, 0)
    pii curr = { 0, 0 };


    // S * C 길이만큼 알파벳을 주워야 함
    for (int i = 0; i < S * C; i++) {
        char ch = uid[i % S];
        pii dest = fieldAlphabet[ch - 'a'].back(); fieldAlphabet[ch - 'a'].pop_back();

        goToDest(curr, dest);
        curr = dest;


        command += "P";
    }

    goToDest(curr, {N-1, M-1});
    cout << C << " " << command.size() << endl;
    cout << command << endl;

    return 0;
}
