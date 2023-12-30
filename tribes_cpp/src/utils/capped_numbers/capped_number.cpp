#include <algorithm>
#include <iostream>

#include "capped_number.hpp"

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

float CappedNumber::getValue() const{
    return m_value;
}

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

float CappedNumber::makeWithinBounds(
    const float value, 
    const float min_val, 
    const float max_val
){
    return std::min(std::max(min_val, value), max_val);
}

const float CappedNumber::min_value = -std::numeric_limits<float>::max();
const float CappedNumber::max_value = std::numeric_limits<float>::max();

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

