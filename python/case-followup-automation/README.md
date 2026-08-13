# Case Follow-Up Automation

A sanitized reconstruction of a Python workflow I developed professionally to automate case follow-up communication using structured case data.

## Purpose

The workflow was designed to reduce manual follow-up work by reading case information from a structured data source and automatically generating personalized follow-up messages for individual cases.

## Workflow

Case Data  
→ pandas DataFrame  
→ Iterate Through Case Records  
→ Generate Personalized Message  
→ Build MIME Email  
→ Establish SMTP/TLS Connection  
→ Authenticate  
→ Send Follow-Up Message  
→ Handle Success / Failure

## Technical Implementation

The Python workflow demonstrates:

- Reading structured case information with pandas
- Iterating through records using `iterrows()`
- Extracting case-specific information
- Dynamically generating email subjects
- Creating personalized email content
- Constructing multipart MIME messages
- Connecting to an SMTP server
- Enabling TLS encryption
- SMTP authentication
- Automated message delivery
- Exception handling
- Environment-variable configuration

## Technologies

- Python
- pandas
- SMTP
- TLS
- MIME
- Excel / structured data processing
- Environment variables

## Security and Sanitization

This repository contains a sanitized reconstruction of the original professional workflow.

The public version does **not** contain:

- Original email credentials
- Application passwords
- Production email addresses
- Production case records
- Internal URLs
- Company-specific identifiers
- Personal workstation paths

Authentication credentials have been replaced with environment variables:

- `SMTP_USERNAME`
- `SMTP_PASSWORD`

The production case dataset is intentionally excluded from the repository.

These security changes were made specifically to allow the technical work to be demonstrated publicly without exposing confidential information.

## Source

The sanitized Python implementation is available at:

`src/case_followup_automation.py`

## Portfolio Context

This project demonstrates how I used Python not only for data analysis, but also to automate repetitive operational workflows.

The value of the project was in connecting structured business data with an automated communication process, reducing the amount of manual work required to perform case follow-up.
