FROM python:3.10.12-bullseye
COPY . .
ENTRYPOINT ["python3", "-m", "http.server"]
CMD ["--directory", "/public", "8080"]

# ?> docker build -t myserver .
# ?> docker run --rm -d -p 8080:8080 myserver
# <container hash>
# ?> curl localhost:8080
# This is my default site

# ?> docker run --rm -d -p 3000:3000 -v ./newsite:/newsite myserver 3000 -d /newsite
# <container hash>
# ?> curl localhost:3000
# This is my new site
