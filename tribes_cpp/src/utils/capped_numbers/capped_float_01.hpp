#ifndef DEF_UTILS_CAPPED_FLOAT01
#define DEF_UTILS_CAPPED_FLOAT01

#include "capped_number.hpp"

class CappedFloat01 : public CappedNumber
{
    public:
        CappedFloat01();
        CappedFloat01(float value);
    private:
        const static float min_value;
        const static float max_value;
};

CappedFloat01 operator+(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator-(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator*(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator/(CappedFloat01 const& a, CappedFloat01 const& b);

#endif