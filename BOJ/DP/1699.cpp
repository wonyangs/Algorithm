#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> dp(N + 1, 1e9);
    dp[0] = 0;

    for (int i = 0; i <= N; ++i) {
        for (int j = 1; j <= int(sqrt(N)); ++j) {
            int sq = j * j;
            if (i + sq <= N && dp[i] + 1 < dp[i + sq]) {
                dp[i + sq] = dp[i] + 1;
            }
        }
    }

    cout << dp[N] << endl;

    return 0;
}
