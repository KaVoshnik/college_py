from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=test1,
            user=postgres,
            password=496284,
            host=127.0.0.1,
            port=5432,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
    "test1", "postgres", "496284", "127.0.0.1", "5432"
)