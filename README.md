# a_b_testing   
=> An A/B Testing Python Programme Using Logistics Regression vs Random Forest Non-Linear Alpha Extraction & Probability Calibration

=> This project was originally developed in Dec'25 was being published on Apr 6,'26 as part of a curated Top 6 Quant Portfolio to demonstrate foundational concepts in signal interaction and probability calibration.

=> THIS SECTION CONTAINS ALL THEORY BEHIND THIS PROJECT 

=> Identifying "Hidden" Interactions (Non-Linear Alpha)

1. Brier Score (0.0535 vs 0.0640)

i) Interaction Detection: Logistic Regression assumes independent contributions from each variable $(x_0+x_1+x_2)$. The expression which leads to Alpha is,  $x_0⋅ x_1$  + $x_2$.

ii) Recursive Partitioning: The Random Forest uses decision trees that split on  $x_0$ and then  $x_1$. This creates a step-wise approximation of the multiplication.

2. The Problem :

==> Linear models (Logistic Regression) fail to capture multiplicative feature interactions, leading to miscalibrated probabilities:

$$x_0 \cdot x_1$$

3. Logic Behind The Code

==> The model captures the relationship defined by:

$$Y = x_0 \cdot x_1 + x_2$$

4. The Alpha: This represents a scenario where $x_0$ is only valuable if $x_1$ is also present (e.g., a specific Order Book Imbalance only matters if Volatility is above a certain threshold).

5. Advantage : By using the Random Forest, the code captures this "Multiplicative Alpha" that a standard Linear Regression would completely ignore or "average out" as noise.


6. Signal Calibration (The Brier Score Advantage)
   
==>In high-frequency trading (HFT), Alpha is also about "position sizing". This code calculates the Brier Score to ensure probability estimates are mathematically calibrated:

$$BS = \frac{1}{N} \sum_{t=1}^{N} (f_t - o_t)^2$$

7. Noise Filtering (Sharpening the Signal-to-Noise Ratio)

==> The Feature Importance Analysis distinguishes between "Market Regime" signals and "Random Walk" noise:

i)Market Regime: $(x_0, x_1, x_2)$

ii)Random Walk: $(x_3, x_4)$

==> Inclusion of $x_3$ and $x_4$ as pure noise.

iii) The Alpha: The Feature Importance Analysis in your code proves the model can distinguish between "Market Regime" $(x_0, x_1, x_2)$ and "Random Walk" $(x_3, x_4)$. The Alpha is often covered by 95% market noise.

iv)Advantages: It prevents you from "trading the noise." Generating Alpha is as much about not losing money on bad signals as it is about winning on good ones.

==> Note: This framework allows for superior risk-adjusted position sizing compared to a traditional linear estimator by moving beyond first-order linear effects.


8. The Theory of Signal Calibration (Brier Score)

$BS = \frac{1}{N} \sum_{t=1}^{N} (f_t - o_t)^2$

i) BS (The Brier Score)

  ==> The "Calibration Metric"

     => It measures the accuracy of your probabilistic predictions. A score of 0 is a perfect ideal model, while 1 is a      model that is confidently wrong every single time.

ii) $1/N$  (The Averaging Term)

  ==> N is the total number of samples (predictions) in your test set.

  ==> We divide by N to get the Mean error. This ensures that a model tested on 100 trades can be compared fairly to a model tested on 1,000,000 trades.


iii) $$\frac{1}{N} \sum_{t=1}^{N}$$ (The Summation)

  ==> This is the sum from the first trade (t=1) to the last trade (N).

  ==> This aggregates the individual errors across the entire backtest period. We use this because we need to know about the model's total performance over a specific time horizon.

iv) $f_t$   (The Predicted Probability)

  ==> This is the probability output from the model (e.g., 0.85 or 85%).

  ==> For $f_t=0.9$, the model  says that there is a 90% chance this trade hits the profit target.

v) $o_t$ (The Outcome / Ground Truth)

  ==> The actual result of the trade.  There are two possible outcomes :-

  ==> 1 if the event happened (Price hit target).

  ==> 0 if the event did not happen.

  ==> Note: This is the binary reality of the market.

vi) $(f_t-o_t )^2$

 ==> (The Squared Error)

	=> The difference between hypothetical and real value squared.

	=> Squaring ensures that being "confidently wrong" (predicting 0.9 when the outcome is 0) is punished much more heavily than being "unsure" (predicting 0.5). 

	=> Positivity: Squaring ensures that errors don't cancel each other out (e.g., a +0.2 error and a -0.2 error don't sum to zero).

9. Additional Notes

I.The Problem: Linear models (Logistic Regression) suffer from high Structural Bias. They fail to capture multiplicative feature interactions, specifically the term $x_0 \cdot x_1$, leading to miscalibrated probabilities and sub-optimal risk pricing.

II.The Solution: A Random Forest Ensemble that approximates the non-linear interaction via recursive partitioning. By splitting the feature space hierarchically, the ensemble can map the conditional relationship between $x_0$ and $x_1$.
Logistic Regression suffers from Structural Bias in this context because it assumes an additive relationship $(x_0 + x_1)$. By contrast, the Random Forest captures the Conditional Alpha—where signal $x_0$ is only valid if $x_1$ exceeds a threshold—mirroring real-world market regimes.

III.The Proof: The Random Forest achieved a Brier Score (BS) of 0.0535, significantly lower than the Linear Regression model's 0.0640. This reduction in quadratic loss proves superior probability calibration, essential for Kelly Criterion-based position sizing.

$$
BS = \frac{1}{N} \sum_{t=1}^{N} (f_t - o_t)^2
$$

IV.The Alpha: Feature importance analysis (Gini Impurity) confirmed that $x_2$ was correctly identified as the primary driver:

i) $x_2$ (Signal): 0.6364
ii) $x_0, x_1$ (Interactions): 0.15 (approx.)
iii) $x_3, x_4$ (Noise): < 0.03 (Successfully suppressed)

In modern markets, simple signals like "If Volume is high, Buy" are already priced out. Alpha now hides in contingent relationships.

10. Conclusion

==> This framework generates Alpha by moving beyond first-order linear effects. It successfully extracts Conditional Alpha (the interaction of $x_0$ and $x_1$) while utilizing the Brier Score to ensure our probability estimates are mathematically calibrated. This allows for superior risk-adjusted position sizing compared to a traditional linear estimator.

11. Packages Required

==> This project requires the following Python libraries for data processing and statistical inference:

   => Pandas: Data structuring and conversion rate calculation.

   => NumPy: Vectorized mathematical operations.

   => SciPy: Statistical distribution functions and p-value derivation.  

   => Statsmodels: Statistical power analysis and proportion testing.  

   => Matplotlib/Seaborn: Visualizing distribution overlaps and confidence intervals.

12. Installation

```bash
pip install pandas numpy scikit-learn
```




