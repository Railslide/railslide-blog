Title: Tips and tricks for developing locally with Docker
Date: 2018-03-03
Tags: docker, dev env
Slug: tips-and-tricks-for-developing-locally-with-docker
Summary: ???
Status: Draft

One of the perks of Docker is that it gives

## Use Docker Compose

## Leverage cache

Docker caches layer while building and chances are that you want to leverage that cache as much as possible (we all love fast builds!). But, in order to do that, you need to keep in mind how caching works in Docker.


## Use Docker Compose for overriding Dockerfiles

Another good reason for using Docker Compose is that it gets priority over Dockerfiles, giving you the power to override their specification while developing.

For example, you might want uWSGI to watch and automatically reload when detecting changes to the source code in dev, but not in production. In that case, you'd have your production command in your Dockerfile:

```
CMD ["uwsgi", \
     "-s", "0.0.0.0:5000", \
     "--master", \
     "--manage-script-name", \
     "--mount", "/=app:app"]
```

and the overriding dev command in your docker-compose.yml

```
command: "uwsgi \
          --s 0.0.0.0:5000 \
          --master \
          --manage-script-name \
          --mount /=app:app \
          --python-autoreload 1"
```


## Use a volume for the source code

If you happen to be working with dynamic languages, you might get frustrated by having to wait for the build to complete in order to see your code changes applied. Thankfully there's workaround for it: use Docker Compose to override the Dockerfile and add your source folder as a volume. By doing so, changes to the code will immediately propagate to the container.

```
my_app:
  volumes:
    - ./src:/src/
```

## Use a .dockerignore file

Since fast builds and lightweight are good things, you should definitely be picky when it comes to choose which files and directory should go in your container and which ones should not.

In order to avoid bloating your own images, you should create a .dockerignore file. (The syntax for it is similar to the .gitignore one, but not quite the same, so make sure to check the [docs](https://docs.docker.com/engine/reference/builder/#dockerignore-file)).

Last but not least, remember to add Dockerfile, docker-compose.yml and even the .dockerignore itself to it.
