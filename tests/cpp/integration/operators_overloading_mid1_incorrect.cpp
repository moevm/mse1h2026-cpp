#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n), b(n);

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    cout << "SUM: ";
    for (int i = 0; i < n; i++) {
        cout << a[i] + b[i] + 1 << " ";
    }
    cout << "\n";

    cout << "COPY: ";
    for (int i = 0; i < n; i++) {
        cout << b[i] << " ";
    }

    return 0;
}