// INCLUDE STANDARD LIBRARIES
#include <algorithm>
#include <iostream>

// INCLUDE HEADERS
#include "capped_number.hpp"

// ------------------------------ CONSTRUCTORS --------------------------------
CappedNumber::CappedNumber(){
    m_value = 0;
}

CappedNumber::CappedNumber(float value){
    m_value = makeWithinBounds(
        value, 
        CappedNumber::min_value, 
        CappedNumber::max_value
    );
}

// ------------------------------ CLASS METHODS -------------------------------
float CappedNumber::getValue() const{
    return m_value;
}

float CappedNumber::makeWithinBounds(
    const float value, 
    const float min_val, 
    const float max_val
){
    return std::min(std::max(min_val, value), max_val);
}

// --------------------------- UTILITY METHODS --------------------------------
void CappedNumber::sendToFlux(std::ostream &flux) const{
    flux << m_value;
}

CappedNumber& CappedNumber::operator+=(const CappedNumber& other){
    m_value += other.m_value;
    return *this;
}

CappedNumber& CappedNumber::operator+=(const float other){
    m_value += other;
    return *this;
}

CappedNumber& CappedNumber::operator-=(const CappedNumber& other){
    m_value -= other.m_value;
    return *this;
}

CappedNumber& CappedNumber::operator-=(const float other){
    m_value -= other;
    return *this;
}

CappedNumber& CappedNumber::operator*=(const CappedNumber& other){
    m_value *= other.m_value;
    return *this;
}

CappedNumber& CappedNumber::operator*=(const float other){
    m_value *= other;
    return *this;
}

CappedNumber& CappedNumber::operator/=(const CappedNumber& other){
    m_value /= other.m_value;
    return *this;
}

CappedNumber& CappedNumber::operator/=(const float other){
    m_value /= other;
    return *this;
}

// ----------------------- BOUNDS FOR CAPPED FLOATS ---------------------------

const float CappedNumber::min_value = -std::numeric_limits<float>::max();
const float CappedNumber::max_value = std::numeric_limits<float>::max();


// ------------------------ STANDARD OPERATORS --------------------------------
std::ostream &operator<<(std::ostream& flux, CappedNumber const& c_num){
    c_num.sendToFlux(flux);
    return flux;
}

CappedNumber operator+(CappedNumber const& a, CappedNumber const& b){
    CappedNumber result(a);
    result += b;
    return result;
}

CappedNumber operator-(CappedNumber const& a, CappedNumber const& b){
    CappedNumber result(a);
    result -= b;
    return result;
}

CappedNumber operator*(CappedNumber const& a, CappedNumber const& b){
    CappedNumber result(a);
    result *= b;
    return result;
}

CappedNumber operator/(CappedNumber const& a, CappedNumber const& b){
    CappedNumber result(a);
    result /= b;
    return result;
}

