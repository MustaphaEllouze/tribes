#ifndef DEF_UTILS_CAPPED
#define DEF_UTILS_CAPPED

#include <iostream>

class CappedNumber
{
public:
    CappedNumber(float value, bool minimum_value, bool maximum_value);
    float getValue() const;
    void sendToFlux(std::ostream &flux) const;

private:
    static float min_value;
    static float max_value;
    float m_value;
};

std::ostream &operator<<(std::ostream& flux, CappedNumber const& c_num);

#endif