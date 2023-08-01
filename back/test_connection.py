from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# .env ファイルをロード
load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
server = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DATABASE")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}/{db}"
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_connection():
    try:
        # セッションを作成
        session = SessionLocal()
        # 簡単なクエリを実行
        result = session.execute(text("SELECT 1"))
        print(result.fetchone())
        # セッションをクローズ
        session.close()
    except Exception as e:
        print(f"接続に失敗しました: {e}")

if __name__ == "__main__":
    test_connection()
