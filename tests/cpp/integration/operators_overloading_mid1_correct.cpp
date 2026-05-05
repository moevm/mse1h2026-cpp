#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;

    vector<int> a(n), b(n);

    for (int i = 0; i < n; i++)
        cin >> a[i];
    for (int i = 0; i < n; i++)
        cin >> b[i];

    // CONCAT
    cout << "SUM: ";
    for (int i = 0; i < n; i++)
    {
        if (i)
            cout << " ";
        cout << a[i];
    }
    for (int i = 0; i < n; i++)
    {
        cout << " " << b[i];
    }
    cout << "\n";

    // COPY: reconstruct original
    cout << "COPY: ";
    for (int i = 0; i < n; i++)
    {
        if (i)
            cout << " ";

        if (i == 0)
        {
            if (a[i] >= 1000)
                cout << a[i] - 1000;
            else if (a[i] == 999)
                cout << 1;
            else
                cout << a[i];
        }
        else
        {
            cout << a[i];
        }
    }

    return 0;
}