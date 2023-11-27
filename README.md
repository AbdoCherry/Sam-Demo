# SAM (CLI) Demo

## Overview

This project is a learning exercise focused on building an AWS Lambda function with Python using the SAM CLI and Docker. The Lambda function is a simple example that loads environment variables and demonstrates the setup for different environments (dev and prd). The Dockerfile is designed for a multi-stage build to optimize the Lambda deployment package.

## Project Structure

docker: Contains the Dockerfile for building the Lambda function.
envs: Includes environment configuration files for development (dev) and production (prd).
src: Holds the Python source code for the Lambda function.
.dockerignore: Specifies files and directories to exclude from Docker builds.
requirements.txt: Lists Python dependencies for the Lambda function.
template.yml: Defines the AWS SAM template for deploying the Lambda function.

## Lambda Function (app.py)

The app.py file contains the entrypoint for the Lambda function (lambda_handler).
It loads environment variables and prints them. It serves as a basic demonstration and learning tool for handling environment variables in a Lambda function.

## Docker Setup

The Dockerfile follows a multi-stage build:

Stage I (builder): Installs build dependencies, copies the requirements file, installs Python dependencies, and removes unnecessary dependencies.
Stage II (final): Copies the Python dependencies from the builder stage, copies the source code, and sets the entrypoint for the Lambda function.

## SAM Template (template.yml)

The SAM template (template.yml) defines the AWS resources for the Lambda function.
It includes parameters for environment-specific configurations such as database connection details and AWS IAM credentials.
The template also specifies the Docker image configuration and build context.

## How to Use

1. Environment Setup: Create environment configuration files (dev.env and prd.env) in the envs directory with appropriate values.
2. AWS Profile: Ensure you have an AWS profile configured with the necessary permissions.
3. IAM User: Create a separate IAM user for the Lambda function and provide the required permissions.
4. SAM CLI: Install the SAM CLI and Docker on your machine.
5. Build and Deploy: Run the following commands in the project root directory:

```bash
sam build
sam deploy --guided
```

Follow the prompts to configure deployment settings.

## Notes

- The .dockerignore file excludes virtual environment and environment files from Docker builds.
- The Dockerfile uses the official AWS ECR base image for Python Lambda functions.
- The SAM template supports different environments with parameters for configuration.

## Disclaimer
This project is intended for educational purposes, and the code may not be suitable for production use without further refinement and security considerations.
Ensure that you follow best practices when handling sensitive information and deploying AWS resources.



