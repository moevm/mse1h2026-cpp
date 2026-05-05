#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (b + d == 0) {
        cout << "undefined\n0";
        return 0;
    }

    cout << a + c << "/" << b + d << "\n";

    cout << (a == c);

    return 0;
}