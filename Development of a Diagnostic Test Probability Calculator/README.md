# Bayesian Disease Probability Calculator
=====================================

This project calculates the probability of having a disease given the results of a medical test, using Bayesian inference.

## Overview
-----------

The calculator takes into account the prevalence of the disease, the sensitivity of the test, and the specificity of the test. It then calculates the probability of having the disease given a positive test result and the probability of having the disease given a negative test result.

## Functions
------------

### `calculate_probability_disease_given_positive(prevalance, sensitivity, specificity)`

Calculates the probability of having the disease given a positive test result.

* `prevalance`: The prevalence of the disease (between 0 and 1)
* `sensitivity`: The sensitivity of the test (between 0 and 1)
* `specificity`: The specificity of the test (between 0 and 1)

Returns the probability of having the disease given a positive test result.

### `calculate_probability_disease_given_negative(prevalance, sensitivity, specificity)`

Calculates the probability of having the disease given a negative test result.

* `prevalance`: The prevalence of the disease (between 0 and 1)
* `sensitivity`: The sensitivity of the test (between 0 and 1)
* `specificity`: The specificity of the test (between 0 and 1)

Returns the probability of having the disease given a negative test result.

## Usage
-----

To use the calculator, simply call the `calculate_probability_disease_given_positive` or `calculate_probability_disease_given_negative` functions with the desired input values.

Example:
```python
from logic import calculate_probability_disease_given_positive, calculate_probability_disease_given_negative

prevalance = 0.1
sensitivity = 0.9
specificity = 0.95

probability_disease_given_positive = calculate_probability_disease_given_positive(prevalance, sensitivity, specificity)
probability_disease_given_negative = calculate_probability_disease_given_negative(prevalance, sensitivity, specificity)

print("Probability of having the disease given a positive test result:", probability_disease_given_positive)
print("Probability of having the disease given a negative test result:", probability_disease_given_negative)

README generate with Windsurf

Uses:
* Quick estimate with test result value

Limitation:
* Assumes prevalence, sensitivity, and specificity are known precisely
* Ignores cost-benefit analysis or consequences of false results.
