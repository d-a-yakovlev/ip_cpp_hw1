project(string_holder)

set(STRING_HOLDER_SRC_FILES
    src/string_holder.cpp
)

add_library(string_holder_lib STATIC ${STRING_HOLDER_SRC_FILES})
