# change_point_analysis

# Assumptions and Limitations

## Assumptions

1. **Piecewise Stationarity:** We assume that while the overall series is non-stationary, it can be segmented into piecewise stationary regimes with stable parameters within each epoch.
2. **Prior Distributions:** We assume that the switch-point parameter $\tau$ is uniformly distributed across the length of the time series window being analyzed.

## Limitations: Statistical Correlation vs. Causal Impact

One of the most critical aspects of this analysis is distinguishing between **statistical correlation in time** and **proving causal impact**:

- **Temporal Correlation:** When our change-point model detects a structural break on or near a specific date (e.g., March 2020) and we observe that the World Health Organization declared a global pandemic around the same date, we establish a _temporal correlation_.
- **Why this is NOT Causation:** A temporal correlation does not isolate the event from other confounding variables. For instance, in early March 2020, there was also a sudden production disagreement between OPEC and Russia (a supply shock) happening simultaneously with the COVID-19 demand shock.
- **Proving Causal Impact:** To prove causal impact, we would need to construct a counterfactual scenario—what would Brent oil prices have been _without_ the pandemic? Since we cannot run a controlled experiment on global oil markets, proving direct causality requires advanced econometric designs, such as **Synthetic Control Methods**, **Difference-in-Differences (DiD)**, or **Structural Vector Autoregressions (SVAR)** with sign restrictions to control for other concurrent global factors.
