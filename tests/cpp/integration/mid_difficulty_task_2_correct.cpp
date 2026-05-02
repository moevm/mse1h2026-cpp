#include <iostream>
using namespace std;

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;

    int num = a * d + c * b;
    int den = b * d;

    if (den == 0) {
        cout << "undefined";
    } else {
        cout << num << "/" << den;
    }

    return 0;
}