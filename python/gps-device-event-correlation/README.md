# GPS / Device Event Correlation Analysis

This project contains a sanitized reconstruction of Python analysis I developed while troubleshooting enterprise fleet technology systems.

## Purpose

The analysis was used to investigate whether there was a measurable relationship between recurring poor GPS-quality events and device loose-connection events.

The underlying event datasets were generated through separate SQL-based troubleshooting analyses.

## Technical Approach

The Python analysis:

- Loaded GPS-quality and loose-connection event data using pandas
- Compared the two event datasets
- Calculated a Pearson correlation coefficient using SciPy
- Created a scatter plot using Matplotlib to visualize the relationship

## Technologies

- Python
- pandas
- SciPy
- Matplotlib
- NumPy
- Excel-based data analysis

## Confidentiality

The original production datasets are intentionally excluded from this repository.

Personal workstation paths and other environment-specific information have been removed from the public version. The analytical method and core code structure have been retained to represent the technical work performed.
