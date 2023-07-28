server
├── .devcontainer 　　 Dev Container 関連
│ ├── devcontainer.json
│ └── docker-compose.yml
├── .env 　 　　　　 backend 用の環境ファイル。GitHub には存在しない。
├── .gitignore 　　　後から登録した場合、git rm --cached file_or_folder で適用。
├── backend.sh 　　 　 backendserver コンテナの最後に起動
├── docker-compose.yml
├── docker_clear.sh 　　 docker イメージ等を全て削除
├── env.py 　　　　　　　デフォルトの./alembic/env.py
├── mysql
│ ├── Dockerfile 　　　 mysql の仕様書
│ ├── data 　　　　　　データベースの本体。git で管理せずデータのみ sql で取り出すべき。
│ │ └── db
│ ├── init.sql 　　　初回のみ適用。ユーザー登録
│ └── my.cnf 　　　 mysql の設定ファイル
├── nginx
│ ├── log
│ │ ├── access.log
│ │ └── error.log
│ └── nginx.conf 　　　転送先の設定
├── phpmyadmin
│ └── sessions
└── server
├── Dockerfile
├── \_\_pycache\_\_
│ ├── main.cpython-39.pyc
│ └── models.cpython-39.pyc
├── main.py 　 API の本体
├── models.py 　 model クラス
├── requirements.txt 　 pip 登録するライブラリ名
└── test_connection.py 　参考　データベースに接続できるかの確認

(Compose Up で生成される。)
├── alembic 　　　　マイグレーション
│ ├── README
│ ├── \_\_pycache\_\_
│ │ └── env.cpython-39.pyc
│ ├── env.py 　　　./env.py に上書きされる。
│ ├── script.py.mako
│ └── versions
│ ├── 9f0dc674a524_default_model_migration.py 　　最初のマイグレーション
│ └── \_\_pycache\_\_
│ └── 9f0dc674a524_default_model_migration.cpython-39.pyc
└── alembic.ini 　　　 backend.sh によって更新される。

- GitHub からクローン直後では alembic フォルダと alembic.ini は存在しない。これらは自動生成される。
- alembic によるデータベース制御は特殊。生成されたマイグレーションファイルを古い順に適用する。
- Dev Container に入って models.py を更新したら、マイグレーションを実行してデータベースと models.py を再接続する。
  alembic revision --autogenerate -m "message hoge" →alembic upgrade head
- テーブルやコラム削除は新規マイグレーションファイルを手動編集し、適用。以下はテーブル削除例

1.  alembic revision --autogenerate -m "message" を実行。
2.  生成されたマイグレーションファイルの upgrade を編集。
    自動生成された箇所をコメントアウトし、op.drop_table('test_users)を追記、保存。
    def upgrade() -> None: # ### commands auto generated by Alembic - please adjust! ### # op.create_table('test_users', # sa.Column('id', sa.Integer(), nullable=False), # sa.Column('user_name', sa.String(length=100), nullable=False), # sa.Column('email', sa.String(length=100), nullable=True), # sa.PrimaryKeyConstraint('id') # )
    op.drop_table('test_users') # ### end Alembic commands ###
3.  alembic upgrade head でマイグレーションを適用

- ./docker_clear.shを実行するとコンテナimage等が消去、初期化される。

- 動作不良で困ったら、alembic フォルダ、alembic.ini、mysql フォルダを削除する。
  データは破壊されるので注意。
