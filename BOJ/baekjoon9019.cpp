#include <iostream>
#include <queue>
#include <string>

using namespace std;

typedef pair<int, string> pis;

string convertTo4DigitNumber(int num) {
    
    string numStr = to_string(num);
    
    while (numStr.length() != 4) {
        numStr = "0" + numStr;
    }
    
    return numStr;
    
}

string toLeft(string numStr) {
    
    char temp = numStr[0];
    
    numStr[0] = numStr[1];
    numStr[1] = numStr[2];
    numStr[2] = numStr[3];
    numStr[3] = temp;
    
    return numStr;
    
}

string toRight(string numStr) {
    
    char temp = numStr[3];

    numStr[3] = numStr[2];
    numStr[2] = numStr[1];
    numStr[1] = numStr[0];
    numStr[0] = temp;
    
    return numStr;
    
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    

    int t;
    cin >> t;
    
    while(t--) {
        
        bool visited[10000] ={false, }; 
        
        int a, b;
        cin >> a >> b;
        
        queue<pis> q;
        q.push({a, ""});
        
        pis curr;
        
        while (true) {
            
            curr = q.front(); q.pop();
            
            if (curr.first == b) break;
            
            int nextNum;
            
            // D
            nextNum = curr.first << 1;
            if (nextNum > 9999) nextNum %= 10000;
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                q.push({nextNum, curr.second + "D"});
            }
            
            // S
            if (curr.first == 0) {
                nextNum = 9999;
            } else {
                nextNum = curr.first - 1;
            }
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                q.push({nextNum, curr.second + "S"});
            }
            
            // L
            nextNum = (curr.first % 1000) * 10 + (curr.first / 1000);
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                q.push({nextNum, curr.second + "L"});
            }
            
            // R
            nextNum = curr.first / 10 + (curr.first % 10) * 1000;
            if (!visited[nextNum]) {
                visited[nextNum] = true;
                q.push({nextNum, curr.second + "R"});
            }
            
        }
        
        cout << curr.second << endl;
        
    }

    return 0;
}
