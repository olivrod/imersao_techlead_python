docker run \
  --rm -it \
  -p 127.0.0.1:4566:4566 \
  -p 127.0.0.1:4510-4559:4510-4559 \
  -v /run/user/$(id -u)/docker.sock:/var/run/docker.sock \
  localstack/localstack