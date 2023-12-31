#ifndef DEF_PERSONS_RACE
#define DEF_PERSONS_RACE

#include "../utils/height.hpp"
#include "../utils/weight.hpp"
#include "../utils/time.hpp"

#include "../utils/capped_numbers/positive_float.hpp"
#include "../utils/capped_numbers/capped_float_01.hpp"

class Race
{
    public:
    protected:
    private:    
        Height m_male_height;
        Height m_female_height;

        Weight m_male_weight;
        Weight m_female_weight;

        Time m_male_lifespan;
        Time m_female_lifespan;
        
        Time m_male_sex_mature_age;
        Time m_female_sex_mature_age;
        
        Time m_male_mature_age;
        Time m_female_mature_age;
        
        Time m_gestation_time;

        PositiveFloat m_number_of_children;

        
};

#endif