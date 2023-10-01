#include <iostream>
#include <cmath>

using namespace std;

bool isPerfect(int n) {
    int root = sqrt(n);
    return root * root == n;
}

int main(void) {
    int N, M;

    cin >> N;
    cin >> M;
    
    int min = 0;
    int sum = 0;
    for (int i = N; i <= M; i++) {
        if (isPerfect(i)) {
            sum += i;
            if (min == 0)
                min = i;
        }
    }
    if (sum == 0) {
        cout << -1 << endl;
    } else {
        cout << sum << endl;
        cout << min << endl;
    }

    return 0;
}
