#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
    int T;
    cin >> T;
    
    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        
        vector<int> numbers(N);
        for (int i = 0; i < N; i++) {
            cin >> numbers[i];
        }
        
        auto result = minmax_element(numbers.begin(), numbers.end());
        
        cout << (*result.second - *result.first) * 2 << '\n';
    }

    return 0;
}
