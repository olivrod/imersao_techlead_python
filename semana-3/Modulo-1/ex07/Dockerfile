FROM python:3.10-slim
COPY . /app
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "mojifinder:app", "--host", "0.0.0.0", "--port", "5000"]