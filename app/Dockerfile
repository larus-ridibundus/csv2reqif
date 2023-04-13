# Use the latest Python image for ARM64 architecture
FROM python:3.7-alpine

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# # Install any required system packages here
# RUN apk add --no-cache \
#     build-base \
#     libressl-dev \
#     libffi-dev \
#     openssl-dev \
#     rust


RUN pip3 install lxml

# # Set the working directory
WORKDIR /app
# VOLUME ["/usr/src/app"]

# Copy the application code to the container
COPY . /app
# COPY . /usr/src/app/

# # Run the application
# CMD ["python", "app.py"]
# ENTRYPOINT ["python3", "/app/app.py"]
