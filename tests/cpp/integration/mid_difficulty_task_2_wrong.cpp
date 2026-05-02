#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (b + d == 0) {
        cout << "undefined";
    } else {
        cout << a + c << "/" << b + d; // WRONG
    }

    return 0;
}