#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<int> a(n), b(n);

    for (int i = 0; i < n; i++) cin >> a[i];
    for (int i = 0; i < n; i++) cin >> b[i];

    // WRONG
    vector<int>& copy_arr = a;

    // WRONG
    if (n > 0) {
        a[0] += 1000;
    }

    // WRONG
    cout << "SUM: ";
    for (int i = 0; i < n; i++) {
        if (i) cout << " ";
        cout << a[i] + b[i];
    }
    cout << "\n";

    // WRONG
    cout << "COPY: ";
    for (int i = 0; i < (int)copy_arr.size(); i++) {
        if (i) cout << " ";
        cout << copy_arr[i];
    }

    return 0;
}