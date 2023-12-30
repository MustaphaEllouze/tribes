#include "utils/capped_numbers/capped_number.hpp"
#include "utils/capped_numbers/capped_float_01.hpp"
#include "utils/capped_numbers/positive_float.hpp"
#include <iostream>

int main(){
    PositiveFloat i(1);
    PositiveFloat j(-1);

    std::cout << i+j << std::endl;
    std::cout << i-j << std::endl;
    std::cout << i*j << std::endl;
    std::cout << i/j << std::endl;
    return 0;
}