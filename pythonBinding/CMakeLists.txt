cmake_minimum_required(VERSION 3.15)

project(pythonBinding)

add_library(lib_cal SHARED lib_cal.hpp lib_cal.cpp)

# set python env to be the venv
set(Python_VIRTUALENV FIRST)

find_package(pybind11 REQUIRED)

pybind11_add_module(binding_module
    module.cpp
)

target_link_libraries(binding_module PUBLIC lib_cal)
