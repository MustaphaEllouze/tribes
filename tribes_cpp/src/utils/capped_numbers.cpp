#include <algorithm>
#include <iostream>

#include "capped_numbers.hpp"

CappedNumber::CappedNumber(
    float value, 
    bool minimum_value, 
    bool maximum_value
){
    float result = value;
    if(minimum_value){
        result = std::max(CappedNumber::min_value, result);
    }
    if(maximum_value){
        result = std::min(CappedNumber::max_value, result);
    }
    m_value = result;
}

float CappedNumber::getValue() const {
    return m_value;
}

void CappedNumber::sendToFlux(std::ostream &flux) const {
    flux << m_value;
}

std::ostream& operator<<(std::ostream &flux, CappedNumber const &c_num){
    c_num.sendToFlux(flux);
    return flux;
}

float CappedNumber::min_value = 2;
float CappedNumber::max_value = 5;