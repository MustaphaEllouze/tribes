#ifndef DEF_UTILS_CAPPED
#define DEF_UTILS_CAPPED

#include <iostream>
#include <limits>

class CappedNumber
{
    public :
        CappedNumber();
        CappedNumber(float value);
        float getValue() const;
        void sendToFlux(std::ostream &flux) const;

        CappedNumber& operator+=(const CappedNumber& other);
        CappedNumber& operator+=(const float other);
        CappedNumber& operator-=(const CappedNumber& other);
        CappedNumber& operator-=(const float other);
        CappedNumber& operator*=(const CappedNumber& other);
        CappedNumber& operator*=(const float other);
        CappedNumber& operator/=(const CappedNumber& other);
        CappedNumber& operator/=(const float other);
        
        static float makeWithinBounds(const float value, const float min_val, const float max_val);
    private:
        const static float min_value;
        const static float max_value;
    protected:
        float m_value;
};

std::ostream &operator<<(std::ostream& flux, CappedNumber const& c_num);
CappedNumber operator+(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator-(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator*(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator/(CappedNumber const& a, CappedNumber const& b);

#endif