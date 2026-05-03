#include <array>
#include <initializer_list>
#include <iostream>
#include <stdexcept>

class Matrix3x3 {
private:
    std::array<std::array<int, 3>, 3> data{};

public:
    Matrix3x3() = default;

    Matrix3x3(std::initializer_list<int> values) {
        if (values.size() != 9) {
            throw std::invalid_argument("Need exactly 9 elements");
        }
        auto it = values.begin();
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                data[i][j] = *it++;
            }
        }
    }

    Matrix3x3 operator*(const Matrix3x3& other) const {
        Matrix3x3 result;
        for (int i = 0; i < 3; ++i) {
            for (int j = 0; j < 3; ++j) {
                int sum = 0;
                for (int k = 0; k < 3; ++k) {
                    sum += data[i][k] * other.data[k][j];
                }
                result.data[i][j] = sum;
            }
        }
        return result;
    }

    int& operator()(int row, int col) {
        if (row < 0 || row > 2 || col < 0 || col > 2) {
            throw std::out_of_range("index");
        }
        return data[row][col];
    }

    const int& operator()(int row, int col) const {
        if (row < 0 || row > 2 || col < 0 || col > 2) {
            throw std::out_of_range("index");
        }
        return data[row][col];
    }

    static Matrix3x3 Identity() {
        Matrix3x3 id;
        for (int i = 0; i < 3; ++i) {
            id.data[i][i] = 1;
        }
        return id;
    }

    friend std::ostream& operator<<(std::ostream& os, const Matrix3x3& m) {
        for (int i = 0; i < 3; ++i) {
            os << "[ " << m.data[i][0] << " " << m.data[i][1] << " " << m.data[i][2] << " ]";
            if (i != 2) {
                os << "\n";
            }
        }
        return os;
    }
};

int main() {
    int valuesA[9];
    int valuesB[9];
    for (int i = 0; i < 9; ++i) {
        if (!(std::cin >> valuesA[i])) {
            return 0;
        }
    }
    for (int i = 0; i < 9; ++i) {
        std::cin >> valuesB[i];
    }

    Matrix3x3 a{valuesA[0], valuesA[1], valuesA[2],
                valuesA[3], valuesA[4], valuesA[5],
                valuesA[6], valuesA[7], valuesA[8]};
    Matrix3x3 b{valuesB[0], valuesB[1], valuesB[2],
                valuesB[3], valuesB[4], valuesB[5],
                valuesB[6], valuesB[7], valuesB[8]};

    int rMod = 0;
    int cMod = 0;
    int newVal = 0;
    std::cin >> rMod >> cMod >> newVal;
    a(rMod, cMod) = newVal;

    int rRead = 0;
    int cRead = 0;
    std::cin >> rRead >> cRead;

    int rBad = 0;
    int cBad = 0;
    std::cin >> rBad >> cBad;

    Matrix3x3 product = a * b;
    std::cout << product << "\n";
    std::cout << a(rRead, cRead) << "\n";
    try {
        (void)a(rBad, cBad);
    } catch (const std::out_of_range&) {
        std::cout << "out_of_range\n";
    }
    std::cout << Matrix3x3::Identity() << "\n";
}
