#ifndef DEF_UTILS_HEIGHT
#define DEF_UTILS_HEIGHT

#include <iostream>

#include "capped_numbers/positive_float.hpp"

class Height
{
    public:
        
        Height();
        Height(float value);

        float getValue() const;
        void addHeight(float const heigh_rate);
        void removeHeight(float const heigh_rate);
        
        void sendToFlux(std::ostream &flux) const;
        Height& operator+=(float const value);
        Height& operator-=(float const value);
        Height& operator*=(float const value);
        Height& operator/=(float const value);

    private:
        PositiveFloat m_value;
};

std::ostream& operator<<(std::ostream &flux, Height const& height);
Height operator+(Height const& height, float const value);
Height operator-(Height const& height, float const value);
Height operator*(Height const& height, float const value);
Height operator/(Height const& height, float const value);

#endif