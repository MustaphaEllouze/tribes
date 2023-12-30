#ifndef DEF_UTILS_CAPPED
#define DEF_UTILS_CAPPED

// INCLUDE STANDARD LIBRARIES
#include <iostream>
#include <limits>

// CLASS DEFINITION
class CappedNumber
{
    public :
        // CONSTRUCTORS
        CappedNumber();
        CappedNumber(float value);

        // CLASS METHODS
        float getValue() const;
        static float makeWithinBounds(
            const float value, 
            const float min_val, 
            const float max_val
        );

        // UTILITY METHODS
        void sendToFlux(std::ostream &flux) const;
        CappedNumber& operator+=(const CappedNumber& other);
        CappedNumber& operator+=(const float other);
        CappedNumber& operator-=(const CappedNumber& other);
        CappedNumber& operator-=(const float other);
        CappedNumber& operator*=(const CappedNumber& other);
        CappedNumber& operator*=(const float other);
        CappedNumber& operator/=(const CappedNumber& other);
        CappedNumber& operator/=(const float other);
        
    private:
        // BOUNDS FOR CAPPED FLOATS
        const static float min_value;
        const static float max_value;

    protected:
        // VALUE ENCAPSULATION
        float m_value;
};

// STANDARD OPERATORS
std::ostream &operator<<(std::ostream& flux, CappedNumber const& c_num);
CappedNumber operator+(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator-(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator*(CappedNumber const& a, CappedNumber const& b);
CappedNumber operator/(CappedNumber const& a, CappedNumber const& b);

#endif