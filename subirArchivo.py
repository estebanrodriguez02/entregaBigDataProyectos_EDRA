import boto3

# Configurar el cliente de S3
s3_client = boto3.client('s3')

def upload_file(bucket_name, file_path, object_name):
    try:
        # Subir el archivo al bucket
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"Archivo '{object_name}' subido exitosamente al bucket '{bucket_name}'.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    bucket_name = "tallerawsclilocal"
    file_path = "/home/ubuntu/python-proyect/list_buckets.py"
    object_name = "archivoSubido"

    upload_file(bucket_name, file_path, object_name)

