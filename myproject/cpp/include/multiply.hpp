#pragma once

#include <vector>
#include <cstdint> // uint32_t
#include <stdexcept> // std::invalid_argument

std::vector<std::vector<float>> multiply_cpp_cpu(std::vector<std::vector<float>> const& a,
                                             std::vector<std::vector<float>> const& b);