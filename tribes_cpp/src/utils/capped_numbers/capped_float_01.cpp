// INCLUDE HEADERS
#include "capped_float_01.hpp"

// ------------------------------ CONSTRUCTORS --------------------------------
CappedFloat01::CappedFloat01(){
    m_value = 0;
}

CappedFloat01::CappedFloat01(float value){
    m_value = CappedNumber::makeWithinBounds(
        value, 
        CappedFloat01::min_value, 
        CappedFloat01::max_value
    );
}

// ----------------------- BOUNDS FOR CAPPED FLOATS ---------------------------
const float CappedFloat01::min_value = 0;
const float CappedFloat01::max_value = 1;

// ----------------------- UTILITY METHODS ------------------------------------
CappedFloat01& CappedFloat01::operator+=(const CappedFloat01& other){
    m_value = makeWithinBounds(m_value+other.m_value, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator+=(const float other){
    m_value = makeWithinBounds(m_value+other, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator-=(const CappedFloat01& other){
    m_value = makeWithinBounds(m_value-other.m_value, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator-=(const float other){
    m_value = makeWithinBounds(m_value-other, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator*=(const CappedFloat01& other){
    m_value = makeWithinBounds(m_value*other.m_value, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator*=(const float other){
    m_value = makeWithinBounds(m_value*other, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator/=(const CappedFloat01& other){
    m_value = makeWithinBounds(m_value/other.m_value, min_value, max_value);
    return *this;
}
CappedFloat01& CappedFloat01::operator/=(const float other){
    m_value = makeWithinBounds(m_value/other, min_value, max_value);
    return *this;
}

// ------------------------ STANDARD OPERATORS --------------------------------
CappedFloat01 operator+(CappedFloat01 const& a, CappedFloat01 const& b){
    CappedFloat01 result(a);
    result += b;
    return result;
}
CappedFloat01 operator-(CappedFloat01 const& a, CappedFloat01 const& b){
    CappedFloat01 result(a);
    result -= b;
    return result;
}
CappedFloat01 operator*(CappedFloat01 const& a, CappedFloat01 const& b){
    CappedFloat01 result(a);
    result *= b;
    return result;
}
CappedFloat01 operator/(CappedFloat01 const& a, CappedFloat01 const& b){
    CappedFloat01 result(a);
    result /= b;
    return result;
}
