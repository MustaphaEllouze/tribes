#include <iostream>
#include <cmath>

#include "capped_numbers/positive_float.hpp"
#include "height.hpp"

Height::Height(){
    m_value = PositiveFloat(0);
}

Height::Height(float value){
    m_value = PositiveFloat(value);
}

float Height::getValue() const {
    return m_value.getValue();
}

void Height::addHeight(float const heigh_rate){
    *this += heigh_rate;
}

void Height::removeHeight(float const height_rate){
    *this -= height_rate;
}

void Height::sendToFlux(std::ostream &flux) const{
    double integral_part;
    double decimal_part = modf(m_value.getValue(), &integral_part);
    flux << integral_part << "m" << decimal_part*1000;
}

Height& Height::operator+=(const float value){
    m_value += value;
    return *this;
}
Height& Height::operator-=(const float value){
    m_value -= value;
    return *this;
}
Height& Height::operator*=(const float value){
    m_value *= value;
    return *this;
}
Height& Height::operator/=(const float value){
    m_value /= value;
    return *this;
}

std::ostream& operator<<(std::ostream &flux, Height const& height){
    height.sendToFlux(flux);
    return flux;
}
Height operator+(Height const& height, float const value){
    Height result(height.getValue()+value);
    return result;
}
Height operator-(Height const& height, float const value){
    Height result(height.getValue()-value);
    return result;
}
Height operator*(Height const& height, float const value){
    Height result(height.getValue()*value);
    return result;
}
Height operator/(Height const& height, float const value){
    Height result(height.getValue()/value);
    return result;
}