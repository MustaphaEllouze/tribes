#include <iostream>
#include <cmath>

#include "capped_numbers/positive_float.hpp"
#include "weight.hpp"

Weight::Weight(){
    m_value = PositiveFloat(0);
}

Weight::Weight(float value){
    m_value = PositiveFloat(value);
}

float Weight::getValue() const {
    return m_value.getValue();
}

void Weight::addWeight(float const weigh_rate){
    *this += weigh_rate;
}

void Weight::removeWeight(float const weight_rate){
    *this -= weight_rate;
}

void Weight::sendToFlux(std::ostream &flux) const{
    double integral_part;
    double decimal_part = modf(m_value.getValue(), &integral_part);
    flux << integral_part << "kg" << decimal_part*1000;
}

Weight& Weight::operator+=(const float value){
    m_value += value;
    return *this;
}
Weight& Weight::operator-=(const float value){
    m_value -= value;
    return *this;
}
Weight& Weight::operator*=(const float value){
    m_value *= value;
    return *this;
}
Weight& Weight::operator/=(const float value){
    m_value /= value;
    return *this;
}

std::ostream& operator<<(std::ostream &flux, Weight const& weight){
    weight.sendToFlux(flux);
    return flux;
}
Weight operator+(Weight const& weight, float const value){
    Weight result(weight.getValue()+value);
    return result;
}
Weight operator-(Weight const& weight, float const value){
    Weight result(weight.getValue()-value);
    return result;
}
Weight operator*(Weight const& weight, float const value){
    Weight result(weight.getValue()*value);
    return result;
}
Weight operator/(Weight const& weight, float const value){
    Weight result(weight.getValue()/value);
    return result;
}