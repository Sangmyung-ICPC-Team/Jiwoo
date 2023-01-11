#include <iostream>
#include <queue>
#include <vector>

using namespace std;

typedef pair<int, int> pii;


int dx[4] = {0, 0, 1, -1};
int dy[4] = {1, -1, 0, 0};


int n;

void bfs(int x, int y, vector<vector<char>> &field, vector<vector<bool>> &visited) {
    queue<pii> q;
    q.push({x, y});
    
    while(!q.empty()) {
        pii curr = q.front(); q.pop();
        
        for(int i=0; i<4; i++) {
            int nx = curr.first + dx[i];
            int ny = curr.second + dy[i];
            
            if(nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
            
            if(!visited[nx][ny] && field[curr.first][curr.second] == field[nx][ny]) {
                visited[nx][ny] = true;
                q.push({nx, ny});
            }
        }
    }
}

int solve(vector<vector<char>> &field) {
    
    vector<vector<bool>> visited(n, vector<bool>(n));
    
    int cnt = 0;
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            if(!visited[i][j]){
                cnt++;
                bfs(i, j, field, visited);
            }
        }
    }
    
    return cnt;
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    
    
    vector<vector<char>> field(n, vector<char>(n));
    vector<vector<char>> rgbField(n, vector<char>(n));
    // input
    for(int i=0; i<n; i++) {
        for(int j=0; j<n; j++) {
            cin >> field[i][j];
            
            rgbField[i][j] = field[i][j];
            if (rgbField[i][j] == 'G') {
                rgbField[i][j] = 'R';
            }
        }
    }
    
    
    int cnt = solve(field);
    int rgbCnt = solve(rgbField);
    
    cout << cnt << " " << rgbCnt << endl;

    return 0;
}