#include <pybind11/pybind11.h>
#include "lib_cal.hpp"

PYBIND11_MODULE(binding_module, m) {
    m.def("cmult", &lib_cal::cmult);
}