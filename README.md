# -Correlation-Analysis-Crime-Poverty-Unemployment
This project analyzes the **statistical relationship between crime, poverty, and unemployment** using a cleaned, merged international dataset.   The goal is to identify **linear correlations** between key socio-economic indicators that are often central to **policy and development analysis**.
---

## Dataset
The analysis uses a pre-processed dataset:

- `clean_merged.csv`

This dataset was created by merging:
- Crime rank data
- Poverty indicators
- Unemployment statistics  

across multiple countries and years.

---

## Data Preparation
Before analysis, columns were renamed for clarity:

| Original Column | Renamed Column |
|-----------------|---------------|
| OBS_VALUE_x | crime_rank |
| OBS_VALUE_y | poverty |
| MEAN_OBS_OF_ALL_LEVEL_OF_KNOWLEDGE | unemployment |

This ensures clear interpretation of variables during analysis.

---

## Methodology

### 1. Variable Selection
The following indicators were selected:
- **Crime Rank**
- **Poverty Level**
- **Unemployment Rate**

### 2. Correlation Calculation
A **Pearson correlation matrix** was computed using pandas to quantify the strength and direction of relationships between variables.

### 3. Visualization
The correlation matrix was visualized using:
- Heatmap (`matplotlib.pyplot.imshow`)
- Color scale (`plt.colorbar`)
- Labeled axes for interpretability

---

## Output
The script generates a **correlation heatmap** showing:
- Strength of relationships between crime, poverty, and unemployment
- Positive and negative associations
- Relative magnitude of correlations

This visualization helps quickly identify socio-economic linkages.

---

## Tools & Libraries
- Python
- pandas
- matplotlib

---

## Insights & Use Cases
This analysis can be used to:
- Support policy discussions on socio-economic vulnerability
- Identify variables that move together across countries
- Provide evidence for deeper econometric or spatial analysis
- Serve as groundwork for a **Composite Vulnerability Index**

---

## Possible Extensions
- Time-wise correlation analysis
- Country-specific correlation trends
- Regression modeling
- Geospatial correlation mapping
- Index construction and ranking

---

## Author Notes
This project demonstrates **data cleaning, transformation, statistical analysis, and visualization skills** relevant to economic research, policy analysis, and international development roles.
