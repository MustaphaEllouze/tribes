#include <tuple>
#include <iostream>

#include "capped_numbers/positive_float.hpp"
#include "time.hpp"

const int Time::YEARS_TO_DAYS = 365;

Time::Time(){
    m_days = 0;
}

Time::Time(int days){
    m_days = days;
}

Time::Time(int years, int days){
    m_days = YEARS_TO_DAYS*years + days;
}

int Time::getYears() const{
    return m_days/YEARS_TO_DAYS;
}

int Time::getValue() const{
    return m_days;
}

std::tuple<int,int> Time::getYearsAndDays() const{
    std::tuple<int,int> resultat(
        m_days/YEARS_TO_DAYS,
        m_days%YEARS_TO_DAYS
    );
    return resultat;
}

void Time::sendToFlux(std::ostream& flux){
    std::tuple<int,int> years_and_days = this->getYearsAndDays();
    flux 
        << std::get<0>(years_and_days) 
        << " years " 
        << std::get<1>(years_and_days)
        << " days";
}

Time& Time::operator+=(Time time){
    m_days += time.m_days;
    return *this;
}

Time& Time::operator+=(int value){
    m_days += value;
    return *this;
}

Time& Time::operator-=(Time time){
    m_days -= time.m_days;
    return *this;
}

Time& Time::operator-=(int value){
    m_days -= value;
    return *this;
}

std::ostream& operator<<(std::ostream& flux, Time time){
    time.sendToFlux(flux);
    return flux;
}

Time operator+(Time const& a, Time const& b){
    Time result(a);
    result += b;
    return result;
}
Time operator-(Time const& a, Time const& b){
    Time result(a);
    result -= b;
    return result;
}