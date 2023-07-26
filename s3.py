import boto3


# Initialize AWS SDK clients
def initialize_clients(access_key, secret_key):
    session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    s3_client = session.client('s3')
    cf_client = session.client('cloudfront')
    return s3_client, cf_client


# Function to pull billing details
def get_billing_details():
    client = boto3.client('ce')  # Cost Explorer client
    response = client.get_cost_and_usage(
        TimePeriod={
            'Start': '2023-07-01',
            'End': '2023-07-25',
        },
        Granularity='DAILY',
        Metrics=['BlendedCost'],
    )
    return response['ResultsByTime']


# Function to upload files to S3 and CloudFront
def upload_to_s3_and_cloudfront(bucket_name, file_path, distribution_id):
    s3_client, cf_client = initialize_clients(ACCESS_KEY, SECRET_KEY)

    # Upload file to S3
    with open(file_path, 'rb') as file:
        s3_client.upload_fileobj(file, bucket_name, file_path)

    # Invalidate CloudFront distribution cache
    cf_client.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': ['/*'],
            },
            'CallerReference': 'unique-invalidation-id',
        }
    )


if __name__ == "__main__":
    ACCESS_KEY = 'your-access-key'
    SECRET_KEY = 'your-secret-key'
    BUCKET_NAME = 'your-s3-bucket-name'
    FILE_PATH = 'path/to/your/file.txt'
    DISTRIBUTION_ID = 'your-cloudfront-distribution-id'

    s3_client, cf_client = initialize_clients(ACCESS_KEY, SECRET_KEY)

    # Get billing details
    billing_details = get_billing_details()
    print(billing_details)

    # Upload file to S3 and invalidate CloudFront cache
    upload_to_s3_and_cloudfront(BUCKET_NAME, FILE_PATH, DISTRIBUTION_ID)
