# ifndef DEF_UTILS_TIME
#define DEF_UTILS_TIME

#include <tuple>
#include <iostream>

#include "capped_numbers/positive_float.hpp"

class Time {
    public:
        Time();
        Time(int days);
        Time(int years, int days);
        int getYears() const;
        int getValue() const;
        std::tuple<int,int> getYearsAndDays() const;
        void sendToFlux(std::ostream& flux);
        Time& operator+=(Time time);
        Time& operator+=(int value);
        Time& operator-=(Time time);
        Time& operator-=(int value);
    protected:
        int m_days;
    private:
        static const int YEARS_TO_DAYS;
};

std::ostream& operator<<(std::ostream& flux, Time time);
Time operator+(Time const& a, Time const& b);
Time operator-(Time const& a, Time const& b);

#endif