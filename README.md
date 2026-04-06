# a_b_testing
An A/B Testing Python Programme Using Logistics Regression vs Random Forest Non-Linear Alpha Extraction &amp; Probability Calibration

I had made this project on December 2025 and preserved it. 

Identifying "Hidden" Interactions (Non-Linear Alpha)

 Brier Score (0.0535 vs 0.0640)

Interaction Detection: Logistic Regression assumes independent contributions from each variable (x_0+ x_1 + x_2). The expression which leads to Alpha is ,  $x_0⋅ x_1$  + $x_2$.

Recursive Partitioning: The Random Forest uses decision trees that split on  $x_0$ and then  $x_1$. This creates a step-wise approximation of the multiplication.

	

The Theory of Signal Calibration (Brier Score)
$BS = \frac{1}{N} \sum_{t=1}^{N} (f_t - o_t)^2$

BS (The Brier Score)

	What it is: The "Calibration Metric."

	The Quant Logic: It measures the accuracy of your probabilistic predictions. A score of 0 is a perfect "God-mode" model, while 1 is a model that is confidently wrong every single time.

2. $1/N$  (The Averaging Term)

	N is the total number of samples (predictions) in your test set.

	We divide by N to get the Mean error. This ensures that a model tested on 100 trades can be compared fairly to a model tested on 1,000,000 trades.


3.$\sum_{t=1}^{N}$
(The Summation)

	This is the sum from the first trade (t=1) to the last trade (N).

	This aggregates the individual errors across the entire backtest period. We use this because we need to know about the model's total performance over a specific time horizon.

4. $f_t$   (The Predicted Probability)

	This is the probability output from the model (e.g., 0.85 or 85%).

	For $f_t=0.9$, the model  says that there is a 90% chance this trade hits the profit target.

5. $o_t$ (The Outcome / Ground Truth)

	 The actual result of the trade.  There are two possible outcomes :-

	1 if the event happened (Price hit target).

	0 if the event did not happen.

	Note: This is the binary reality of the market.

6. $(f_t-o_t )^2$

 (The Squared Error)

	The difference between hypothetical and real value squared

	 Squaring ensures that being "confidently wrong" (predicting 0.9 when the outcome is 0) is punished much more heavily than being "unsure" (predicting 0.5). 

	Positivity: Squaring ensures that errors don't cancel each other out (e.g., a +0.2 error and a -0.2 error don't sum to zero).


Additional Notes

	The Problem: Linear models (Logistic Regression) fail to capture multiplicative feature interactions ($x_0 \cdot x_1$), leading to miscalibrated probabilities.

	The Solution: A Random Forest Ensemble that approximates the interaction via recursive partitioning.

	The Proof: The Challenger achieved a Brier Score of 0.0535, significantly lower than the Legacy model's 0.0640, proving superior probability calibration.

	The Alpha: Feature $x_2$ was correctly identified as the primary driver (0.63 importance), while noise features $x_3$ and $x_4$ were successfully suppressed.





In modern markets, simple signals like "If Volume is high, Buy" are already priced out. Alpha now hides in contingent relationships.

•	The Code's Logic: 

$Y = x_0 \cdot x_1 + x_2$ 


•	The Alpha: This represents a scenario where $x_0$ is only valuable if $x_1$ is also present (e.g., a specific Order Book Imbalance only matters if Volatility is above a certain threshold).

•	Why it wins: By using the Random Forest Challenger, the code captures this "Multiplicative Alpha" that a standard Linear Regression (Legacy) would completely ignore or "average out" as noise.

2. Signal Calibration (The Brier Score Advantage)

In high-frequency trading (HFT), Alpha is not just about being "right"; it’s about Position Sizing.

•	The Code's Logic: Calculating the Brier Score $(f_t - o_t)^2$.

•	The Alpha: If your model says "90% probability" but is only right 60% of the time, you will over-leverage and blow up.

•	Why it wins: This code helps you select the model that is most "Honest." Lowering the Brier Score from 0.064 to 0.053 (as seen in your output) allows you to use Kelly Criterion sizing more aggressively, turning the same predictions into higher compounding returns.

3. Noise Filtering (Sharpening the Signal-to-Noise Ratio)

Alpha is often buried under 95% market noise.

•	The Code's Logic: Inclusion of $x_3$ and $x_4$ as pure noise.

•	The Alpha: The Feature Importance Analysis in your code proves the model can distinguish between "Market Regime" ($x_0$, $x_1$, $x_2$) and "Random Walk" ($x_3$, $x_4$).

•	Why it wins: It prevents you from "trading the noise." Generating Alpha is as much about not losing money on bad signals as it is about winning on good ones.

Conclusion

This framework generates Alpha by moving beyond first-order linear effects. It successfully extracts Conditional Alpha (the interaction of $x_0$ and $x_1$) while utilizing the Brier Score to ensure our probability estimates are mathematically calibrated. This allows for superior risk-adjusted position sizing compared to a traditional linear estimator.



