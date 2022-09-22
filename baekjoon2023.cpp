#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int n;
int sdp[4] = {2, 3, 5, 7};
int pd[4] = {1, 3, 7, 9}; 

bool isPrimary(int number) {
    for(int i=2; i<sqrt(number); i++) {
        if(number % i == 0) {
            return false;
        }
    }
    return true;
}

void backtracking(string number)
{
    if(number.length() == n) {
        cout << number << endl;
    } else {
        if(number.length() == 0) {
            for(int i=0; i<4; i++) {
                backtracking(number + to_string(sdp[i]));
            }
        }else {
            for(int i=0; i<4; i++) {
                if(isPrimary(stoi(number + to_string(pd[i])))) {
                    backtracking(number + to_string(pd[i]));
                }
            }
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;

    backtracking("");

    return 0;
}
