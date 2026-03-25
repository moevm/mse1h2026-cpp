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
    Matrix3x3 id = Matrix3x3::Identity();
    Matrix3x3 b{1, 2, 3, 4, 5, 6, 7, 8, 9};
    Matrix3x3 c = id * b;

    std::cout << c(2, 1) << "\n";
    try {
        (void)c(3, 0);
    } catch (const std::out_of_range&) {
        std::cout << "oor\n";
    }
    std::cout << Matrix3x3::Identity() << "\n";
}
