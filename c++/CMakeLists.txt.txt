cmake_minimum_required(VERSION 3.12)
project(ResizeImages)

find_package(OpenCV REQUIRED)

set(CMAKE_CXX_STANDARD 11)

add_executable(resize_images main.cpp)

target_link_libraries(resize_images ${OpenCV_LIBS})
