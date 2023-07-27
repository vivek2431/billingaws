import boto3

def check_aws_communication():
    try:
        # Replace 'your_region_name' with the AWS region you want to communicate with (e.g., 'us-east-1', 'eu-west-1', etc.)
        # If you're not sure about the region, you can use 'us-east-1' as it's a commonly used region.
        region_name = 'us-east-1'

        # Create a Boto3 session
        session = boto3.session.Session()

        # Create a low-level service client using the session
        # Replace 'your_service_name' with the AWS service you want to interact with (e.g., 's3', 'ec2', 'dynamodb', etc.)
        # You can find the service names in the Boto3 documentation for the respective service.
        client = session.client('s3', region_name=region_name)

        # Use a simple API call to check if the communication is successful
        response = client.list_buckets()

        # If the communication is successful, 'Buckets' key should be present in the response.
        if 'Buckets' in response:
            print("AWS communication using Boto3 is successful!")
        else:
            print("AWS communication using Boto3 failed.")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    check_aws_communication()
