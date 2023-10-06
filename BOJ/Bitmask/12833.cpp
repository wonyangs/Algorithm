#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    
    cin >> a >> b >> c;
    
    if (c & 1)
        cout << (a ^ b);
    else
        cout << a;

    return 0;
}
