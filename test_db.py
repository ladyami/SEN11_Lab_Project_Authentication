import os
import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        print("🔄 Attempting to connect to database...")
        print(f"Host: {os.getenv('MYSQL_HOST')}")
        print(f"User: {os.getenv('MYSQL_USER')}")
        print(f"DB: {os.getenv('MYSQL_DB')}")
        
        connection = pymysql.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DB'),
            cursorclass=DictCursor,
             ssl=None,
            connect_timeout=10
        )
        print("✅ Connection successful!")
        
        with connection.cursor() as cur:
            cur.execute("SELECT 1")
            result = cur.fetchone()
            print(f"✅ Query successful: {result}")
        
        connection.close()
        return True
    except Exception as e:
        print(f"❌ Connection failed: {str(e)}")
        return False

if __name__ == '__main__':
    test_connection()