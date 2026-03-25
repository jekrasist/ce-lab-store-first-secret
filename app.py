import boto3
import json

def get_secret():
    secret_name = "lab/m8-05/db-credentials"
    region_name = "us-east-1"
    client = boto3.client("secretsmanager", region_name=region_name)
    response = client.get_secret_value(SecretId=secret_name)
    return json.loads(response["SecretString"])

if __name__ == "__main__":
    creds = get_secret()
    print(f"Connected to {creds['host']} as {creds['username']}")
