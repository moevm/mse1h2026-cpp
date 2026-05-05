#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    // WRONG
    if (b == 0 || d == 0) {
        cout << "undefined\n0";
        return 0;
    }

    // WRONG
    int num = a + c;
    int den = b + d;

    cout << num << "/" << den << "\n";

    // WRONG
    cout << (a == c);

    return 0;
}