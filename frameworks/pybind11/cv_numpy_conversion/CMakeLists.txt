cmake_minimum_required(VERSION 2.8)
project(process_in_cpp C CXX)

# set(CMAKE_MACOSX_RPATH ON)
# set(CMAKE_DISABLE_IN_SOURCE_BUILD ON)
# set(CMAKE_DISABLE_SOURCE_CHANGES  ON)

# if(NOT CMAKE_BUILD_TYPE)
#   set(CMAKE_BUILD_TYPE Release)
# endif()
# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -fPIC")
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -fPIC -std=c++11")

# Find dependencies
find_package(Eigen3 REQUIRED)
find_package(OpenCV REQUIRED)
include_directories(${EIGEN3_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})
set( DEPENDENCIES ${OpenCV_LIBS} ${EIGEN3_LIBS} )

# set(PYBIND11_CPP_STANDARD -std=c++11)
add_subdirectory("${process_in_cpp_SOURCE_DIR}/../pybind11" "${process_in_cpp_SOURCE_DIR}/../pybind11/build")

pybind11_add_module(process_in_cpp process_in_cpp.cc)
set_target_properties(process_in_cpp PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${process_in_cpp_SOURCE_DIR}/.")
target_link_libraries(process_in_cpp PRIVATE ${DEPENDENCIES})