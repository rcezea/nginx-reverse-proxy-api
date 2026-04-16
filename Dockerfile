# 1. Base image
FROM python:3.11-slim

LABEL authors="rcezea"

# 2. Working directory
WORKDIR /opt/nginx-reverse-proxy-api

# 3. Copy files
COPY . .

# 4. Install dependencies
RUN pip install -r requirements.txt

# 5. Expose port
EXPOSE 8000

# 6. Run app
CMD ["uvicorn", "main:api", "--host", "0.0.0.0", "--port", "8000"]
