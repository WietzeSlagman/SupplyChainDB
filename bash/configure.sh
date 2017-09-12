sudo docker run \
  --interactive \
  --rm \
  --tty \
  --volume $HOME/bigchaindb_docker:/data \
  bigchaindb/bigchaindb \
  -y configure mongodb

sudo sed -i -e 's/"host": "localhost",/"host": "172.17.0.1",/' $HOME/bigchaindb_docker/.bigchaindb
