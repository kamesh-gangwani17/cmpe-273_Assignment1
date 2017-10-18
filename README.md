Build image from the Dockerfile

docker build -t assignment:least .

Running flask app container

docker run --rm -it -p8000:5000 assignment

Upload the script(uploader)

curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@foo.py" http://localhost:8000/api/v1/scripts

Run the uploaded script(invoker)

curl -i http://localhost:8000/api/v1/scripts/
