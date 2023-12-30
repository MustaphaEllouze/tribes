#ifndef DEF_UTILS_POSITIVE_FLOAT
#define DEF_UTILS_POSITIVE_FLOAT

// INCLUDE STANDARD LIBRARIES
#include "capped_number.hpp"

// CLASS DEFINITION
class PositiveFloat : public CappedNumber
{
    public:
        // CONSTRUCTORS
        PositiveFloat();
        PositiveFloat(float value);

        // UTILITY METHODS
        PositiveFloat& operator+=(const PositiveFloat& other);
        PositiveFloat& operator+=(const float other);
        PositiveFloat& operator-=(const PositiveFloat& other);
        PositiveFloat& operator-=(const float other);
        PositiveFloat& operator*=(const PositiveFloat& other);
        PositiveFloat& operator*=(const float other);
        PositiveFloat& operator/=(const PositiveFloat& other);
        PositiveFloat& operator/=(const float other);

    private:
        // BOUNDS FOR CAPPED FLOATS
        const static float min_value;
        const static float max_value;
};

// STANDARD OPERATORS
PositiveFloat operator+(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator-(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator*(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator/(PositiveFloat const& a, PositiveFloat const& b);

#endif