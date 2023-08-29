# RDS Instance Management Automation

Automate the management of Amazon RDS instances using resource tags, Boto3 scripts, and AWS services.

## Overview

This project demonstrates how to use AWS services and Boto3 scripts to automate the management of Amazon RDS instances. It includes the following features:

1. Extracting Resource Tags: Get a list of all RDS instances and their associated tags.
2. Sending Summarized Email: Send an email containing a summary of RDS instances and tags.
3. Starting and Stopping RDS Instances: Automatically start and stop RDS instances using tags.

## Prerequisites

1. **AWS Account**: Ensure you have an AWS account to create and manage resources.
2. **AWS CLI**: Install and configure the AWS Command Line Interface.
3. **Boto3**: Install the Boto3 library for Python.

## Usage

### 1. Extracting Resource Tags

Run the following command to list all RDS instances and their associated tags:

```bash
python extract_tags.py
