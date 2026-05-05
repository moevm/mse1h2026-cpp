#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    if (b == 0 || d == 0) {
        cout << "undefined\n0";
        return 0;
    }

    // sum
    int num = a * d + c * b;
    int den = b * d;

    // equality
    int equal = (a * d == c * b) ? 1 : 0;

    cout << num << "/" << den << "\n";
    cout << equal;

    return 0;
}