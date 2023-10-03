#include <pybind11/pybind11.h>

#include "multiply.hpp"
#include "pybind11/numpy.h"
namespace py = pybind11;

py::array_t<float> multiply_cpp(py::array_t<float> a, py::array_t<float> b) {
    py::buffer_info a_buf = a.request();
    py::buffer_info b_buf = b.request();
    uint32_t a_rows = a_buf.shape[0], a_cols = a_buf.shape[1];
    uint32_t b_rows = b_buf.shape[0], b_cols = b_buf.shape[1];
    if (a_buf.ndim != 2 || b_buf.ndim != 2) {
        throw std::runtime_error("Number of dimensions must be two");
    }
    if (a_cols != b_rows) {
        throw std::runtime_error("Matrix inner dimensions must agree");
    }
    std::vector<std::vector<float>> a_vec(a_rows, std::vector<float>(a_cols));
    float *a_ptr = (float *)a_buf.ptr;
    for (std::size_t i = 0; i < a_rows; ++i) {
        for (std::size_t j = 0; j < a_cols; ++j) {
            a_vec[i][j] = *(a_ptr + i * a_cols + j);
        }
    }
    std::vector<std::vector<float>> b_vec(b_rows, std::vector<float>(b_cols));
    float *b_ptr = (float *)b_buf.ptr;
    for (std::size_t i = 0; i < b_rows; ++i) {
        for (std::size_t j = 0; j < b_cols; ++j) {
            b_vec[i][j] = *(b_ptr + i * b_cols + j);
        }
    }
    auto c_vec = multiply_cpp_cpu(a_vec, b_vec);
    std::vector<py::ssize_t> c_shape = {a_rows, b_cols};
    py::array_t<float> c = py::array_t<float>(c_shape);
    py::buffer_info c_buf = c.request();
    float *c_ptr = (float *)c_buf.ptr;
    for (std::size_t i = 0; i < a_rows; ++i) {
        for (std::size_t j = 0; j < b_cols; ++j) {
            *(c_ptr + i * b_cols + j) = c_vec[i][j];
        }
    }
    return c;
}

PYBIND11_MODULE(multiply_cpp_impl, m) {
    m.doc() = "Python bindings for Multiply Module.";
    m.def("multiply_cpp", &multiply_cpp, "Multiply two matrices.");
}