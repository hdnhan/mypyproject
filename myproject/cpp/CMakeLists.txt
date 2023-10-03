cmake_minimum_required(VERSION 3.15)
project(PyBinding_Mutiply_Module)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra") # Optional
set(CMAKE_BUILD_TYPE Release)

find_package(Python 3.6 REQUIRED COMPONENTS Interpreter Development) 
execute_process(
    COMMAND ${Python_EXECUTABLE} -m pybind11 --cmakedir
    OUTPUT_VARIABLE pybind11_DIR
    OUTPUT_STRIP_TRAILING_WHITESPACE
)
find_package(pybind11 CONFIG REQUIRED)
set(MODULE_NAME multiply_cpp_impl)
pybind11_add_module(${MODULE_NAME} src/bindings.cpp)

set(MULTIPLY_EXT multiply_ext)
add_library(${MULTIPLY_EXT} src/multiply.cpp)
target_include_directories(${MULTIPLY_EXT} PUBLIC include)
set_target_properties(${MULTIPLY_EXT} PROPERTIES POSITION_INDEPENDENT_CODE ON)

target_link_libraries(
    ${MODULE_NAME}
    PRIVATE
    ${MULTIPLY_EXT}
)