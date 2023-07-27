# billingaws

This Python script provides functions to interact with AWS S3 and CloudFront services. It allows you to:
- Initialize AWS clients for S3 and CloudFront using your AWS access key and secret key.
- Fetch billing details from AWS Cost Explorer for a specified date range and granularity.
- Upload a file to an S3 bucket and create a CloudFront invalidation for the distribution.

## Prerequisites

Before running the script, ensure you have the following:
- Python installed on your machine.
- Boto3 library installed. If not, you can install it using:


## Usage

1. *Initialize Clients*:
 - To use AWS S3 and CloudFront services, call the `initialize_clients` function with your AWS access key and secret key as arguments.
 - The function returns S3 and CloudFront clients that you can use for further operations.

2. *Get Billing Details*:
 - Use the `get_billing_details` function to fetch billing details from AWS Cost Explorer for a specified date range and granularity.
 - Customize the date range in the `TimePeriod` dictionary within the function to fetch billing details for the desired period.

3. *Upload to S3 and CloudFront*:
 - Call the `upload_to_s3_and_cloudfront` function to upload a file to a specified S3 bucket and create a CloudFront invalidation for the distribution.
 - Replace `ACCESS_KEY`, `SECRET_KEY`, `BUCKET_NAME`, `FILE_PATH`, and `DISTRIBUTION_ID` with your actual AWS credentials and relevant identifiers.

4. *Running the Script*:
 - Save the script to a local file (e.g., `aws_operations.py`).
 - Open a terminal or command prompt and navigate to the directory where the script is saved.
 - Execute the script using the following command:
   
   python aws_operations.py
   
 - The script will perform the operations as defined in the `if _name_ == "_main_":` block.

## Important Note

- Ensure that the AWS IAM user associated with the provided access key and secret key has appropriate permissions to access AWS S3, CloudFront, and Cost Explorer.
- Use this script responsibly, and follow AWS best practices for security and access management.

## License

This project is licensed under the [MIT License](LICENSE).
