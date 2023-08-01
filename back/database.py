import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
server = os.getenv("MYSQL_HOST")
db = os.getenv("MYSQL_DATABASE")
DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}/{db}"
engine = create_engine(DATABASE_URL,echo=True )
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)
# データベースとの接続に使用するBaseクラスを作成
Base = declarative_base()
'''下のコードの説明chatGPTより
このコードは、FastAPIでデータベース接続を管理するための非常に一般的な方法です。ここで使われているのはPythonのジェネレーターとyieldキーワードです。
SessionLocal()でデータベースセッションを作成します。
yield dbによって、この関数はジェネレーターとして振る舞います。yieldは一時的に制御を呼び出し元に戻し、後続の処理を一時停止します。
FastAPIはこのジェネレーターを使って依存性を解決する際、データベースセッションを必要とするエンドポイント関数にdbを供給します。エンドポイント関数が終了すると、再びジェネレーターが再開されます。
finallyブロック内のdb.close()は、エンドポイント関数が終了した後に必ず実行され、データベースセッションをクローズしてリソースを解放します。これにより、データベースの接続リークを防止します。
このようなデータベースセッションの管理方法は、FastAPIやその他のWebフレームワークでよく使われるパターンであり、データベース接続の効率的な管理とクリーンアップを実現します。'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



