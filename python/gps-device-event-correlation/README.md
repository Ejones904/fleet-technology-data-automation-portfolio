# GPS / Device Event Correlation Analysis

Sanitized reconstruction of a professional troubleshooting analysis used to investigate whether poor GPS-quality events and recurring device loose-connection events showed a measurable relationship.

## Workflow

1. Load two event datasets with pandas.
2. Compare event counts using SciPy's Pearson correlation.
3. Visualize the relationship with a scatter plot.

The included Excel files contain fully synthetic demonstration data. They are not production records.

## Public-release changes

Personal workstation paths were replaced with relative project paths. Production data is not included. The analytical method and visible code structure were retained.
