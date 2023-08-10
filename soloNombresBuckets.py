import boto3

# Configurar el cliente de S3
s3_client = boto3.client('s3')

def list_files(bucket_name):
    try:
        # Obtener la lista de objetos en el bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        # Imprimir los nombres de los archivos
        for obj in response.get('Contents', []):
            print(obj['Key'])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    bucket_name = "tallerawsclilocal"  # Reemplaza con el nombre de tu bucket
    list_files(bucket_name)

