#include <iostream>
using namespace std;

// GCD function
int gcd(int a, int b) {
    while (b != 0) {
        int t = a % b;
        a = b;
        b = t;
    }
    return a < 0 ? -a : a;
}

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

    // reduce fraction
    int g = gcd(num, den);
    num /= g;
    den /= g;

    if (den < 0) {
        num = -num;
        den = -den;
    }

    // equality
    int equal = (a * d == c * b) ? 1 : 0;

    cout << num << "/" << den << "\n";
    cout << equal;

    return 0;
}