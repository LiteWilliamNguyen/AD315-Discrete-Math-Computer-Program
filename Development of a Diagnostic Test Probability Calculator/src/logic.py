
# Bayes' Theorem
# P(A|B) = P(B|A) * P(A) / P(B)
def calculate_probability_disease_given_positive(prevalence, sensitivity, specificity):
    # Making sure the values are between 0 and 1
    if not ( 0 <= prevalence <= 1 and 0 <= sensitivity <= 1 and 0 <= specificity <= 1):
        raise ValueError("Values must be between 0 and 1")
    
    #Calculating probability of testing positive given having the disease
    numerator_positive = prevalence * sensitivity
    denominator_positive = numerator_positive + (1-specificity)*(1-prevalence)
    if denominator_positive != 0:
        probability_disease_given_positive = numerator_positive/denominator_positive
    else:
        probability_disease_given_positive = 0
    return round(probability_disease_given_positive, 4)



def calculate_probability_disease_given_negative(prevalence, sensitivity, specificity):
    # Making sure the values are between 0 and 1
    if not ( 0 <= prevalence <= 1 and 0 <= sensitivity <= 1 and 0 <= specificity <= 1):
        raise ValueError("Values must be between 0 and 1")
    
    #Calculating probability of testing negative given having the disease
    numberator_negative = (1-sensitivity)*prevalence
    denominator_negative = numberator_negative + (1-prevalence)*specificity
    if denominator_negative != 0:
        probability_disease_given_negative = numberator_negative/denominator_negative
    else:
        probability_disease_given_negative = 0
    return round(probability_disease_given_negative,4)