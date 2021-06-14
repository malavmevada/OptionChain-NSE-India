# OptionChain-NSE-India

![Cover Page](./stck.png)

##
### You only need to install **Docker**
[Docker installtion](https://docs.docker.com/engine/install/)
##
After installing docker run this commands,


#### `docker-compos up -d --build`

##
After executing above command run this two command for database migrations,


```
docker-compose run web python3 manage.py  makemigrations

docker-compose run web python3 manage.py migrate
```

Then, open your browser and,go to [http://0.0.0.0:8000/](http://0.0.0.0:8000/)
