#include <iostream>
#include <stack>
#include <vector>

using namespace std;


void dfs(int node, vector<int> &arr, vector<bool> &visited, vector<int> &finished) {
    
    stack<int> s;
    s.push(node);
    
    bool isCycle = false;
    int adj = 0;
    while (true) {
        int curr = s.top();
        
        visited[curr] = true;
        
        adj = arr[curr];
        
        if (curr == adj) {
            finished[curr] = 1;
            s.pop();
            break; // 스택에 남은 노드들은 전부 사이클을 이루지 못함
        }
        
        if (!visited[adj] && finished[adj] == 0) { // 아직 방문하지 않음
        
            s.push(adj);
            
        } else if (visited[adj] && finished[adj] == 0) {
            // 나와 연결된 이웃:
            // 방문됐지만 아직 탐색 중
            // == 사이클을 이룸
            
            isCycle = true;
            break;
            
        } else if (finished[adj] != 0) {
            // 이미 사이클을 이뤘거나
            // 사이클을 이루지 않는 이웃임
            // -> 현재 노드가 포함되어 사이클을 이룰 수 없음
            break;
        }
        
    }
    
    int member = 0;
    while(!s.empty()) {
        
        member = s.top(); s.pop();
        
        if (isCycle) {
            finished[member] = 1; // 사이클에 포함됨
            
            if (member == adj) {
                isCycle = false;
            }
            
        } else {
            finished[member] = 2; // 사이클에 포함안됨
        }
    }
    
}


int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    
    cin >> t;
    
    int n;
    int cnt;
    while (t--) {
        
        cin >> n;
        
        vector<int> arr(n+1);
        
        // 방문 여부
        vector<bool> visited(n+1);
        
        // 0: 아직 완료되지 않음. 1: 사이클로 완료됨, 2: 사이클이 아님
        vector<int> finished(n+1);
        
        
        // 입력
        for(int i=1; i<=n; i++) {
            cin >> arr[i];
        }
        
        
        
        for(int i=1; i<=n; i++) {
            if(finished[i] == 0) {
                dfs(i, arr, visited, finished);
            }
        }
        
        
        cnt = 0;
        for(int i=1; i<=n; i++) {
            if(finished[i] == 2) { // 사이클을 이루지 못함
                cnt++;
            }
        }
        
        cout << cnt << endl;
        
       
    }

    return 0;
}
