# RDS Instance Management Automation

This project demonstrates how to automate the management of Amazon RDS instances using resource tags, Boto3 scripts, and AWS services. It includes the following features:

- Extracting Resource Tags
- Sending Summarized Email
- Starting and Stopping RDS Instances Using Tags

## Table of Contents

- [Project Overview](#project-overview)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

This project aims to simplify the management of Amazon RDS instances by leveraging resource tags and AWS Lambda. The Boto3 library is used for interacting with AWS services programmatically.

## Prerequisites

1. AWS Account: Ensure you have an AWS account to create and manage resources.
2. AWS CLI: Install and configure the AWS Command Line Interface.
3. Boto3: Install the Boto3 library for Python.

## Usage

### Extracting Resource Tags

Run the `extract_tags.py` script to list all RDS instances and their associated tags.

```bash
python extract_tags.py
