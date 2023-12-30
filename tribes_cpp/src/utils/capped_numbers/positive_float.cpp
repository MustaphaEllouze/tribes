#include <limits>

#include "positive_float.hpp"

PositiveFloat::PositiveFloat(){
    m_value = 0;
}

PositiveFloat::PositiveFloat(float value){
    m_value = CappedNumber::makeWithinBounds(
        value, 
        PositiveFloat::min_value, 
        PositiveFloat::max_value
    );
}

const float PositiveFloat::min_value = 0;
const float PositiveFloat::max_value = std::numeric_limits<float>::max();

PositiveFloat operator+(PositiveFloat const& a, PositiveFloat const& b){
    PositiveFloat result(a);
    result += b;
    return result;
}
PositiveFloat operator-(PositiveFloat const& a, PositiveFloat const& b){
    PositiveFloat result(a);
    result -= b;
    return result;
}
PositiveFloat operator*(PositiveFloat const& a, PositiveFloat const& b){
    PositiveFloat result(a);
    result *= b;
    return result;
}
PositiveFloat operator/(PositiveFloat const& a, PositiveFloat const& b){
    PositiveFloat result(a);
    result /= b;
    return result;
}

