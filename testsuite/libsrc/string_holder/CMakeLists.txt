project(string_holder_lib_test)

set(STRING_HOLDER_LIB_TEST_SRC_FILES
    src/unit_tests.cpp
)

add_executable(string_holder_lib_test
 ${STRING_HOLDER_LIB_TEST_SRC_FILES} 
 ${CMAKE_SOURCE_DIR}/third-party/Catch2/extras/catch_amalgamated.cpp
)

target_link_libraries(string_holder_lib_test PRIVATE string_holder_lib)
target_include_directories(string_holder_lib_test PRIVATE ${CMAKE_SOURCE_DIR}/third-party/Catch2/src)

set_target_properties(string_holder_lib_test PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin
)