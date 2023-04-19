cmake_minimum_required(VERSION 3.24)

project("hw1_stringHolder")

set(
    CMAKE_CXX_STANDARD 20
    CMAKE_CXX_STANDARD_REQUIRED On
    CMAKE_CXX_EXTENSIONS Off
)

add_compile_options(-Wall -Wpedantic -Werror)

include_directories(${CMAKE_SOURCE_DIR}/include)

add_subdirectory(libsrc/string_holder)
add_subdirectory(projects/app)
add_subdirectory(testsuite/libsrc/string_holder)