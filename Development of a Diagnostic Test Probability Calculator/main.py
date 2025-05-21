from src.logic import calculate_probability_disease_given_positive, calculate_probability_disease_given_negative

def main():
    print("Bayesian Disease Probability Calculator")
    print("Enter the following values:")
    
    try: 
        # Get user input for prevalence of the disease (between 0 and 1)
        prevalance = float(input("Enter the prevalance of the disease (between 0 and 1): "))
        # Get user input for sensitivity of the test (between 0 and 1)
        sensitivity = float(input("Enter the sensitivity of the test (between 0 and 1): "))
        # Get user input for specificity of the test (between 0 and 1)
        specificity = float(input("Enter the specificity of the test (between 0 and 1): "))

        # Calculate probability of having the disease given a positive test result
        probability_disease_given_positive = calculate_probability_disease_given_positive(prevalance, sensitivity, specificity)
        # Calculate probability of having the disease given a negative test result
        probability_disease_given_negative = calculate_probability_disease_given_negative(prevalance, sensitivity, specificity)

        # Print the calculated probabilities
        print("Probability of having the disease given a positive test result: {:.4f}".format(probability_disease_given_positive))
        print("Probability of having the disease given a negative test result: {:.4f}".format(probability_disease_given_negative))



    except Exception as e:
        print("Invalid input:", e)



if __name__ == "__main__":
    main()