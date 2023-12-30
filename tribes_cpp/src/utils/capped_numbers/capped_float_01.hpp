#ifndef DEF_UTILS_CAPPED_FLOAT01
#define DEF_UTILS_CAPPED_FLOAT01

// INCLUDE STANDARD LIBRARIES
#include "capped_number.hpp"

// CLASS DEFINITION
class CappedFloat01 : public CappedNumber
{
    public:
        // CONSTRUCTORS
        CappedFloat01();
        CappedFloat01(float value);

        // UTILITY METHODS
        CappedFloat01& operator+=(const CappedFloat01& other);
        CappedFloat01& operator+=(const float other);
        CappedFloat01& operator-=(const CappedFloat01& other);
        CappedFloat01& operator-=(const float other);
        CappedFloat01& operator*=(const CappedFloat01& other);
        CappedFloat01& operator*=(const float other);
        CappedFloat01& operator/=(const CappedFloat01& other);
        CappedFloat01& operator/=(const float other);

    private:
        // BOUNDS FOR CAPPED FLOATS
        const static float min_value;
        const static float max_value;
};

// STANDARD OPERATORS
CappedFloat01 operator+(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator-(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator*(CappedFloat01 const& a, CappedFloat01 const& b);
CappedFloat01 operator/(CappedFloat01 const& a, CappedFloat01 const& b);

#endif