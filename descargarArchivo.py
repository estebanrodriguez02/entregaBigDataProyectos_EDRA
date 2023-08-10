import boto3

# Configura las credenciales si es necesario
# boto3.setup_default_session(profile_name='your_profile_name')

# Crea un cliente de Amazon S3
s3 = boto3.client('s3')


def download_file_from_bucket(bucket_name, object_name, local_file_path):
    try:
        s3.download_file(bucket_name, object_name, local_file_path)
        print(f"Archivo '{object_name}' descargado exitosamente como '{local_file_path}'")
    except Exception as e:
        print("Error al descargar el archivo:", str(e))

# Reemplaza 'your_bucket_name' con el nombre de tu bucket
bucket_name = 'tallerawsclilocal'
object_name = 'taller_aws_cli.docx'  # Ruta dentro del bucket al archivo que deseas descargar
local_file_path = '/home/ubuntu/python-proyect/archivoDescargado.docx'  # Ruta local donde deseas guardar el archivo descargado

download_file_from_bucket(bucket_name, object_name, local_file_path)
