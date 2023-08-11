import os
from fastapi import APIRouter
from botocore.exceptions import NoCredentialsError
import boto3
from dotenv import load_dotenv

router = APIRouter()
load_dotenv()

access_key_id = os.getenv("ACCESS_KEY_ID")
secret_access_key = os.getenv("SECRET_ACCESS_KEY")
region = os.getenv("REGION")
s3_bucket_name = os.getenv("S3_BUCKET_NAME")


@router.get("/get_presigned_url/")
async def get_presigned_url(file_name: str, content_type: str):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key,
        region_name=region,
    )

    try:
        upload_url = s3_client.generate_presigned_url(
            "put_object",
            Params={
                "Bucket": s3_bucket_name,
                "Key": file_name,
                "ContentType": content_type,
            },
            ExpiresIn=3600,
            HttpMethod="PUT",
        )

        # ダウンロード用URL（パブリックにする場合）
        download_url = f"https://{s3_bucket_name}.s3.{region}.amazonaws.com/{file_name}"

        return {"presigned_upload_url": upload_url, "download_url": download_url}
    except NoCredentialsError:
        return {"error": "Credentials not available"}
