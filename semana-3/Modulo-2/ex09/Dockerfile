FROM python:3.10-slim 

COPY . /cloud
WORKDIR /cloud

# Install curl, zip, unzip, less and aws cli
RUN apt-get update && \
    apt-get install -y curl zip unzip less && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    
# Install AWS CLI
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm awscliv2.zip && \
    rm -rf aws
    
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]
