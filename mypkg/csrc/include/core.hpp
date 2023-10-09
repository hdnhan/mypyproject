#pragma once

#include <cstdint>    // uint32_t, uint64_t
#include <stdexcept>  // std::invalid_argument
#include <vector>

std::uint64_t fib(std::uint64_t n);
std::vector<std::vector<float>> matmul_cpu(std::vector<std::vector<float>> const& a,
                                           std::vector<std::vector<float>> const& b);