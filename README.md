# csv2reqif
for creating reqif format


# imageの全削除
docker system prune -a --volumes

# containerの実行
sh run.sh

# containerからデータのコピー
docker cp <container_name>:app .
docker cp csv2reqif-reqif-1:app .
