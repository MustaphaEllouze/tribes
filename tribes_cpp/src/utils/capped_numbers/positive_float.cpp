// INCLUDE STANDARD LIBRARIES
#include <limits>

// INCLUDE HEADERS
#include "positive_float.hpp"

// ------------------------------ CONSTRUCTORS --------------------------------
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

// ----------------------- BOUNDS FOR CAPPED FLOATS ---------------------------
const float PositiveFloat::min_value = 0;
const float PositiveFloat::max_value = std::numeric_limits<float>::max();

// ------------------------ STANDARD OPERATORS --------------------------------
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

