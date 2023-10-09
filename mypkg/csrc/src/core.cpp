#include "core.hpp"

std::uint64_t fib(std::uint64_t n) {
    if (n <= 1) {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

std::vector<std::vector<float>> matmul_cpu(std::vector<std::vector<float>> const& a,
                                           std::vector<std::vector<float>> const& b) {
    uint32_t a_rows = a.size(), a_cols = a[0].size();
    uint32_t b_rows = b.size(), b_cols = b[0].size();
    if (a_rows == 0 || a_cols == 0 || b_rows == 0 || b_cols == 0) {
        throw std::invalid_argument("a or b is empty");
    }
    if (a_cols != b_rows) {
        throw std::invalid_argument("a_cols != b_rows");
    }

    std::vector<std::vector<float>> c(a_rows, std::vector<float>(b_cols, 0.0));
    for (std::size_t i = 0; i < a_rows; ++i) {
        for (std::size_t j = 0; j < b_cols; ++j) {
            for (std::size_t k = 0; k < a_cols; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return c;
}
