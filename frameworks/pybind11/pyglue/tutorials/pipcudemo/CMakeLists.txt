cmake_minimum_required(VERSION 3.0)
project(pipcudemo)

file(GLOB SOURCES "*.cu")

find_package(CUDA REQUIRED)
set(CUDA_NVCC_FLAGS ${CUDA_NVCC_FLAGS} -arch=sm_30)

cuda_add_library(mylib SHARED ${SOURCES})

cuda_add_executable(test_mylib testDriver.cpp)
target_link_libraries(test_mylib mylib)
