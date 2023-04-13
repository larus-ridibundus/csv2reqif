# docker build -t myapp .
# docker run myapp
# # docker cp myapp:/output.reqif .


docker-compose -f docker-compose.yml down -v
docker-compose -f docker-compose.yml up -d --build
