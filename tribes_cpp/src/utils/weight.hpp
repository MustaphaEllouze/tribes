#ifndef DEF_UTILS_WEIGHT
#define DEF_UTILS_WEIGHT

#include <iostream>

#include "capped_numbers/positive_float.hpp"

class Weight
{
    public:
        
        Weight();
        Weight(float value);

        float getValue() const;
        void addWeight(float const heigh_rate);
        void removeWeight(float const heigh_rate);
        
        void sendToFlux(std::ostream &flux) const;
        Weight& operator+=(float const value);
        Weight& operator-=(float const value);
        Weight& operator*=(float const value);
        Weight& operator/=(float const value);

    private:
        PositiveFloat m_value;
};

std::ostream& operator<<(std::ostream &flux, Weight const& Weight);
Weight operator+(Weight const& weight, float const value);
Weight operator-(Weight const& weight, float const value);
Weight operator*(Weight const& weight, float const value);
Weight operator/(Weight const& weight, float const value);

#endif