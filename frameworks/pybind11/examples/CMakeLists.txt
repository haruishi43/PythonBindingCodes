project(example)

#**************************************************************************************************
# General cMake settings
#**************************************************************************************************
cmake_minimum_required(VERSION 3.5)

#**************************************************************************************************
# Find Package **************************************************************************************************
find_package(OpenCV REQUIRED)
message(" *** OpenCV_INCLUDE_DIRS : " ${OpenCV_INCLUDE_DIRS})
message(" *** OpenCV_LIB_DIRS : " ${OpenCV_LIB_DIRS})
message(" *** OpenCV_LIBS : " ${OpenCV_LIBS})

find_package(PythonInterp 3 REQUIRED)
find_package(PythonLibs 3 REQUIRED)
message(" *** PYTHON_INCLUDE_DIRS : " ${PYTHON_INCLUDE_DIRS})
message(" *** PYTHON_LIBRARIES : " ${PYTHON_LIBRARIES})

# find_package(pybind11 CONFIG REQUIRED)
add_subdirectory(pybind11)
#**************************************************************************************************
# Include **************************************************************************************************
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS})
include_directories(${OpenCV_INCLUDE_DIRS}/opencv4)
include_directories(${CMAKE_CURRENT_SOURCE_DIR}/src)
include_directories(${pybind11_INCLUDE_DIR})

#**************************************************************************************************
# Set variable **************************************************************************************************
set(SOURCES
  ${CMAKE_CURRENT_SOURCE_DIR}/src/example.cc
  ${CMAKE_CURRENT_SOURCE_DIR}/src/ndarray_converter.cc
)

set(DEPENDENCIES ${OpenCV_LIBS} ${PYTHON_LIBRARIES})

set(CMAKE_CXX_STANDARD 11)
set(PYBIND11_CPP_STANDARD -std=c++11)

#**************************************************************************************************
# Make configuration
#**************************************************************************************************
pybind11_add_module(${PROJECT_NAME} ${SOURCES})
target_link_libraries(${PROJECT_NAME} PRIVATE ${DEPENDENCIES})
