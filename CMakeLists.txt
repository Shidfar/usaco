cmake_minimum_required(VERSION 3.10)
project(USACO)

set(CMAKE_CXX_STANDARD 11)

SET(FILES main.cpp ride/ride.cpp gift1/gift1.cpp)
add_executable(USACO ${FILES})
