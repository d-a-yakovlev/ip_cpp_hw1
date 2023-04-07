project(app)

set(
    APP_SRC_FILES src/app.cpp
)

add_executable(app ${APP_SRC_FILES})
target_link_libraries(app PRIVATE string_holder_lib)
set_target_properties(app PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin
)


add_executable(app_for_integrate ${APP_SRC_FILES})
target_compile_definitions(app_for_integrate PRIVATE INTEGRATE)
target_link_libraries(app_for_integrate PRIVATE string_holder_lib)
set_target_properties(app_for_integrate PROPERTIES 
    RUNTIME_OUTPUT_DIRECTORY ${CMAKE_SOURCE_DIR}/bin
)