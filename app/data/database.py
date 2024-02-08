from pymongo import MongoClient

def get_database_client():
    # Establecer la conexión con la base de datos
    client = MongoClient('mongodb+srv://abrahamsoto3031:hjj4anvu9SFud4ey@cluster0.ok7s10o.mongodb.net/abrahamsoto3031')
    return client