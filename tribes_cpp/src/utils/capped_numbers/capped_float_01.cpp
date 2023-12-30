#include "capped_float_01.hpp"

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

const float CappedFloat01::min_value = 0;
const float CappedFloat01::max_value = 1;

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
