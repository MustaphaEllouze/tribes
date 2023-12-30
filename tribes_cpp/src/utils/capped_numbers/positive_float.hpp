#ifndef DEF_UTILS_POSITIVE_FLOAT
#define DEF_UTILS_POSITIVE_FLOAT

#include "capped_number.hpp"

class PositiveFloat : public CappedNumber
{
    public:
        PositiveFloat();
        PositiveFloat(float value);
    private:
        const static float min_value;
        const static float max_value;
};

PositiveFloat operator+(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator-(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator*(PositiveFloat const& a, PositiveFloat const& b);
PositiveFloat operator/(PositiveFloat const& a, PositiveFloat const& b);

#endif