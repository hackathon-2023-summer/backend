- GitHub からクローン直後では alembic フォルダと alembic.ini は存在しない。これらは自動生成される。
- alembic は model.py と schema.py に基づいてデータベースをマイグレーションする。
- マイグレーションの履歴は alembic/version フォルダに蓄積されるが、削除しても構わない。
- 手動マイグレーション　 Dev Container に入って models.py や schema.py を更新したら
  alembic revision --autogenerate -m "message hoge" →alembic upgrade head

- ./docker_clear.sh を実行するとコンテナ image 等が消去、初期化される。

- 動作不良で困ったら、alembic フォルダ、alembic.ini、mysql フォルダを削除する。
  データベースは破壊されるので注意。

- Dev Container の仕様が変わったのか、Reopen するまで root 権限でコンテナを動かす必要がある模様。
  コンテナに入って $su appuser -> bash を入力すること。

- マイグレーションファイルを削除しても大丈夫と分かったので、backend.sh で docker-compose.yml を実行するたびに
  alembic フォルダと alembic.ini を削除更新するようにした。
