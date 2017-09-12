sudo docker run \
  --detach \
  --name=mongodb \
  --publish=172.17.0.1:27017:27017 \
  --restart=always \
  --volume=/tmp/mongodb_docker/db:/data/db \
  --volume=/tmp/mongodb_docker/configdb:/data/configdb \
  mongo:3.4.1 --replSet=bigchain-rs


sudo docker run \
  --detach \
  --name=bigchaindb \
  --publish=9984:9984 \
  --restart=always \
  --volume=$HOME/bigchaindb_docker:/data \
  bigchaindb/bigchaindb \
  start
