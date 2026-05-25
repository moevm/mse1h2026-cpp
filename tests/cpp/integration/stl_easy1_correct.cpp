#include <iostream>
#include <vector>

void printVectorInfo(const std::vector<int>& vec) {
    std::cout << "Size: " << vec.size() << '\n';
    std::cout << "Capacity: " << vec.capacity() << '\n';
    std::cout << "Empty: " << (vec.empty() ? "yes" : "no") << '\n';
}

int main() {
    std::vector<int> v1;
    std::vector<int> v2 = {1, 2, 3, 4, 5};

    printVectorInfo(v1);
    printVectorInfo(v2);

    return 0;
}
