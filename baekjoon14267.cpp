#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m;
    cin >> n >> m;
    
    vector<vector<int>> henchman(n+1, vector<int>());
    for(int i=1; i<=n; i++) {
        int boss;
        cin >> boss;
        
        if (boss == -1) continue;
        
        henchman[boss].push_back(i);
    }
    
    vector<int> compliment(n+1, 0);
    for(int i=0; i<m; i++) {
        int h, c;
        cin >> h >> c;
        compliment[h] += c;
    }
    
    
    stack<int> s;
    s.push(1);
    
    while (!s.empty()) {
        
        int boss = s.top(); s.pop();
        
        for (int h : henchman[boss]) {
            compliment[h] += compliment[boss];
            s.push(h);
        }
        
    }
    
    for(int i=1; i<=n; i++) {
        cout << compliment[i] << " ";
    }
    cout << endl;
    

    return 0;
}
