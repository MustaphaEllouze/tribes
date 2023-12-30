#include "utils/height.hpp"
#include <iostream>

int main(){
    Height result(1.5);
    result  = result *1.5;
    std::cout << result << std::endl;
    return 0;
}