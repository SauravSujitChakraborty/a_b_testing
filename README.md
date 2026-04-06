# a_b_testing
An A/B Testing Python Programme Using Logistics Regression vs Random Forest Non-Linear Alpha Extraction &amp; Probability Calibration
Identifying "Hidden" Interactions (Non-Linear Alpha)

In modern markets, simple signals like "If Volume is high, Buy" are already priced out. Alpha now hides in contingent relationships.

•	The Code's Logic: 



$Y = x_0 \cdot x_1 + x_2$ 


•	The Alpha: This represents a scenario where x_0 is only valuable if x_1 is also present (e.g., a specific Order Book Imbalance only matters if Volatility is above a certain threshold).

•	Why it wins: By using the Random Forest Challenger, the code captures this "Multiplicative Alpha" that a standard Linear Regression (Legacy) would completely ignore or "average out" as noise.

2. Signal Calibration (The Brier Score Advantage)

In high-frequency trading (HFT), Alpha is not just about being "right"; it’s about Position Sizing.

•	The Code's Logic: Calculating the Brier Score (f_t - o_t)^2.

•	The Alpha: If your model says "90% probability" but is only right 60% of the time, you will over-leverage and blow up.

•	Why it wins: This code helps you select the model that is most "Honest." Lowering the Brier Score from 0.064 to 0.053 (as seen in your output) allows you to use Kelly Criterion sizing more aggressively, turning the same predictions into higher compounding returns.

3. Noise Filtering (Sharpening the Signal-to-Noise Ratio)

Alpha is often buried under 95% market noise.

•	The Code's Logic: Inclusion of x_3 and x_4 as pure noise.

•	The Alpha: The Feature Importance Analysis in your code proves the model can distinguish between "Market Regime" (x_0, x_1, x_2) and "Random Walk" (x_3, x_4).

•	Why it wins: It prevents you from "trading the noise." Generating Alpha is as much about not losing money on bad signals as it is about winning on good ones.

🏛️ The "AIR 1" Interview Summary

When asked if this code helps with Alpha, you should say:

"This framework generates Alpha by moving beyond first-order linear effects. It successfully extracts Conditional Alpha (the interaction of x_0 and x_1) while utilizing the Brier Score to ensure our probability estimates are mathematically calibrated. This allows for superior risk-adjusted position sizing compared to a traditional linear estimator."



