## Cikibike Null Hypothesis project review

The Null hypotheisis is correctly formulated and the data supports the question.

The data is properly pro-processed. The means that are extracted are ideal for a test of means, which can be as simple as a **t-test**, which would answer the question (Of course for that you also have to extract the standard deviation of the sample, not only the mean!)

However the conclusion that is outlined that the longer duration trips would indicate the attempt of costumers to maximize their money investment is over-reaching. For example: subscribers that use the bike for commuting would likely have a fixed, probably relatively short route as their main trip, and not take stops in between that would increment the trip time. 

So since you also present the data separate by day of the week, it would be interesting to see if the ratio of customers to subscriber mean trip duration is significantly different over week days than over weekend. This can be done with a test of proportions (**Z test for proportions or chi-sq**), or if the distribution of trip durations is the same for subscribers over weekends and over week days (KS 2-sample, if the duration not Gaussian and the KS is a non-parametric test which does not assume gaussianity. If the distribution of duration is reasonably Gaussian then also andersonDarling test. The Gaussianity can be checked by looking at the skewness of the distribution and cuspiness of the distribution, or Kurtosis, the 3rd and 4th moments respectively. If those are near 0 and near 1 respectively than the distribution is similar to a Gaussian.) Or even if the distributions  of subscribers and customer trip durations are more similar in weekends than they are in weekdays (again KS or AD tests).

You do not have to do all of these things, they are just ideas.

Also notice that since you are working with a lot of data Effect size should be reported along with statistical significance.

