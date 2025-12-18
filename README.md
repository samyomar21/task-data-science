# task-data-science
## 1. What is the difference between descriptive and inferential statistics? Provide an example of each
descriptive statistics summarize data using measures like mean or graphs
example: average height of students in a class
inferential statistics use sample data to make predictions about a population
example: predicting election results from a poll

---

## What is a confidence interval? What does a 95% confidence interval mean?
a confidence interval gives a range of values likely to contain the true population parameter
a 95% confidence interval means we are 95% sure the true value lies within that range

---

## Explain the difference between correlation and causation. Why is this distinction important?
correlation means two variables move together, but one doesn't necessarily cause the other.
causation means one variable directly affects the other.
this distinction matters to avoid false conclusions in research and decision-making.

---

## What is a probability distribution? Name two discrete and two continuous distributions.
a probability distribution shows how probabilities are assigned to outcomes.
discrete: binomial, poisson
continuous: normal, exponential

---
## What’s the difference between population and sample? Do the same measurements (mean, mode, median) apply to both?
population is the entire group being studied.
sample is a subset of the population.
mean, mode, and median apply to both, but sample statistics estimate population parameters.

---

## What is a histogram? What insights can it provide about a dataset?
a histogram is a bar graph showing frequency of data ranges.
it reveals distribution shape, central tendency, and spread of data.

---

## What is the difference between range and interquartile range (IQR)?
range is the difference between maximum and minimum values.
interquartile range (iqr) is the difference between the third and first quartiles.
iqr is better for showing spread without being affected by outliers

---

Explain what a frequency distribution is and why it is useful.
a frequency distribution shows how often each value or range occurs in a dataset.
it helps understand patterns, trends, and data concentration.

---

## 2.<img width="704" height="455" alt="image" src="https://github.com/user-attachments/assets/9f279de0-d45a-43ec-ba68-328bdc5800ed" />
mean: = 5–6 (skewed due to higher values towards the right)

median: = 4 (middle of the dataset, less affected by outliers)

mode: = 3 (most frequent value, highest bar)

variance: Relatively high due to data spread

standard Deviation: Moderate to high because of the wide range and larger values

differences if this was the Whole Population:

for a sample: Variance and standard deviation are calculated with (n-1).

for a population: Variance and standard deviation are calculated with n, so they would be slightly smaller.

distribution Insights:

the distribution is right-skewed (positively skewed)

the mean > median > mode, as the mean is affected by the larger values

---

## 3. <img width="711" height="462" alt="image" src="https://github.com/user-attachments/assets/d2ed5409-88f8-4e0a-ae7f-55e7d38e86c5" />
values are concentrated on the higher end while fewer values appear on the lower end.

the distribution suggests a moderate spread, since the data covers a wide range of values but most observations are clustered within a smaller interval.

if the dataset were treated as a population rather than a sample, the variance and standard deviation would represent the true measures of variability for the entire population instead of estimates based on a sample.

---
## 4.
1.output: true false

2.interpreter runs code line by line and shows result immediately
compiler translates whole code into machine language before running

3.slicing means extracting part of a sequence using [start:end:step]
example: x[1:4] returns elements from index 1 to 3

4.shallow copy copies outer object but keeps references to inner objects
deep copy copies everything including nested objects
shallow copy breaks code if inner objects are modified, affecting both copies

5. map() applies a function to each item in a list
filter() keeps items that match a condition
list comprehension can do both and is more readable sometimes
use map() for transformation, filter() for selection, and list comprehension for flexibility

6.output: [1] [1, 1] [1, 1, 1]

7. raise triggers an exception manually
 assert checks a condition and raises error if false

8.sort:Modify the original menu (In-place)
sorted:It does not modify the original, but rather returns a new, arranged list








