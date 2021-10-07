class Solution {
public:
    bool canVisitAllRooms(vector<vector<int>>& rooms) {
        vector<int> gragh(1000, 0);
        vector<bool> visited(1000, false);

        stack<int> s;
        s.push(0);

        while (!s.empty()) {
            auto curr = s.top(); s.pop();
            visited[curr] = true;

            for (auto next : rooms[curr])
                if (!visited[next])
                    s.push(next);
        }

        for (int i = 0; i < rooms.size(); i++)
            if (!visited[i])
                return false;

        return true;
    }
};