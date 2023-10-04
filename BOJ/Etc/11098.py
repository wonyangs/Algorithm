#include <iostream>

using namespace std;

void highestPlayer(void) {
    int p;
    
    cin >> p;
    
    int maxPrice = -1;
    string maxName;
    for (int i = 0; i < p; i++) {
        int price;
        string name;
        
        cin >> price >> name;

        if (maxPrice < price) {
            maxPrice = price;
            maxName = name;
        }
    }
    cout << maxName << "\n";
}

int main()
{
    int n;
    
    cin >> n;
    
    for (int i = 0; i < n; i++) {
        highestPlayer();
    }

    return 0;
}
