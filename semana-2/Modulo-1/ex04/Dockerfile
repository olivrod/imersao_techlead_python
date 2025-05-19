FROM ubuntu
ENTRYPOINT ["/usr/bin/echo"]
CMD ["Hello from inside the container"]

# >>> docker build -t myecho .
# >>> docker run --rm myecho
# parametro --rm remove automaticamente o container para nao acumular containers antigos
# Hello from inside the container
# >>> docker run --rm myecho "Olá do Container!"
# Olá do Container!