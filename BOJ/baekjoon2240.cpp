#include <iostream>
#include <vector>

using namespace std;

int t, w;
int plumPos[1001];

int getNumberOfPlums()
{
    vector<vector<int>> dp(1001, vector<int>(31, 0));
    int maxPlums = 0;
    for(int currTime=1; currTime<=t; currTime++) {
        for(int cnt=0; cnt<=w; cnt++) {
            if (plumPos[currTime] == cnt%2) {// cnt%2 == 0: 1번 위치, cnt%2 == 1: 2번 위치
                dp[currTime][cnt] = max(dp[currTime-1][cnt], dp[currTime-1][cnt-1]) + 1;
            } else {
                dp[currTime][cnt] = max(dp[currTime-1][cnt], dp[currTime-1][cnt-1]);
            }
            
            maxPlums = max(maxPlums, dp[currTime][cnt]);
        }
    }
    
    return maxPlums;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> t >> w;

    for(int i=1; i<=t; i++) {
        cin >> plumPos[i];
        plumPos[i]--;
    }


    cout << getNumberOfPlums() << endl;

    return 0;
}