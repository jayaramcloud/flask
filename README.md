# Python flask docker build


**Step 1: Get the files from the repository**

```
jayadmin@cloudshell:~$ git clone https://github.com/jayaramcloud/flask-python.git
Cloning into 'flask-python'...
remote: Enumerating objects: 145, done.
remote: Counting objects: 100% (145/145), done.
remote: Compressing objects: 100% (101/101), done.
remote: Total 145 (delta 31), reused 4 (delta 0), pack-reused 0
Receiving objects: 100% (145/145), 26.79 KiB | 8.93 MiB/s, done.
Resolving deltas: 100% (31/31), done.
jayadmin@cloudshell:~$ ls
README-cloudshell.txt  all.yaml  flask-python  init.yaml  nginx.yaml  pod.yaml  springboot  test
jayadmin@cloudshell:~$ cd flask-python/;ls
Dockerfile  README.md  app
```

**Step 2: Make the required changes**

```
jayadmin@cloudshell:~/flask-python$ vi app/
app.py            requirements.txt  
jayadmin@cloudshell:~/flask-python$ cat app/app.py 
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Demo Flask & Docker application is up and running! This is the updated version 0.1 with awesome changes on Dec 01,2021"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
jayadmin@cloudshell:~/flask-python$ vi app/app.py 
# Change the return value

```

**Step 3: Login to Docker**

```
jayadmin@cloudshell:~/flask-python$ docker login docker.io --username kubetrain
Password: 
WARNING! Your password will be stored unencrypted in /home/jayadmin/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded

```

**Step 4: Build the Docker container image**

```
jayadmin@cloudshell:~/flask-python$ docker build -t docker.io/kubetrain/flask:0.1 .

Sending build context to Docker daemon  91.14kB
Step 1/5 : FROM python
latest: Pulling from library/python
647acf3d48c2: Pull complete 
b02967ef0034: Pull complete 
e1ad2231829e: Pull complete 
5576ce26bf1d: Pull complete 
a66b7f31b095: Pull complete 
05189b5b2762: Pull complete 
af08e8fda0d6: Pull complete 
287d56f7527b: Pull complete 
dc0580965fb6: Pull complete 
Digest: sha256:f44726de10d15558e465238b02966a8f83971fd85a4c4b95c263704e6a6012e9
Status: Downloaded newer image for python:latest
 ---> f48ea80eae5a
Step 2/5 : WORKDIR /opt/demo/
 ---> Running in 97b06e80a057
Removing intermediate container 97b06e80a057
 ---> 7cccec2c6aef
Step 3/5 : COPY /app .
 ---> 983894300c91
Step 4/5 : RUN pip install -r requirements.txt
 ---> Running in 62bd2b6df6b8
Collecting flask
  Downloading Flask-2.0.2-py3-none-any.whl (95 kB)
Collecting itsdangerous>=2.0
  Downloading itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Jinja2>=3.0
  Downloading Jinja2-3.0.3-py3-none-any.whl (133 kB)
Collecting click>=7.1.2
  Downloading click-8.0.3-py3-none-any.whl (97 kB)
Collecting Werkzeug>=2.0
  Downloading Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Collecting MarkupSafe>=2.0
  Downloading MarkupSafe-2.0.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl (30 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-3.0.3 MarkupSafe-2.0.1 Werkzeug-2.0.2 click-8.0.3 flask-2.0.2 itsdangerous-2.0.1
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
WARNING: You are using pip version 21.2.4; however, version 21.3.1 is available.
You should consider upgrading via the '/usr/local/bin/python -m pip install --upgrade pip' command.
Removing intermediate container 62bd2b6df6b8
 ---> aeebe1535dc1
Step 5/5 : ENTRYPOINT python app.py
 ---> Running in 9ef2df3447a1
Removing intermediate container 9ef2df3447a1
 ---> 6217b5192b86
Successfully built 6217b5192b86
Successfully tagged kubetrain/flask:0.1
jayadmin@cloudshell:~/flask-python$ 

```

**Step 5: Ensure you can see the locally built image**

```
jayadmin@cloudshell:~/flask-python$ docker image ls
REPOSITORY                          TAG       IMAGE ID       CREATED              SIZE
kubetrain/flask                     0.1       6217b5192b86   About a minute ago   928MB
kubetrain/springboot-demo-jayaram   v0.1      b0c0de18a9e5   About an hour ago    122MB
python                              latest    f48ea80eae5a   2 weeks ago          917MB
```

**Step 6: Run it locally to test if it runs**

```
jayadmin@cloudshell:~/flask-python$ docker run -d -p 80:80  docker.io/kubetrain/flask:0.1  
616eb7ee6d500f893941ca8ebda29466ee9b1e43f7b5c0e5f955924b3f695dad
jayadmin@cloudshell:~/flask-python$ curl localhost:80
Demo Flask & Docker application is up and running! This is the updated version 1.9 with awesome changes on Dec 01,2021
```

**Step 7: Push it to the Docker Registry**

```

jayadmin@cloudshell:~/flask-python$ docker push  docker.io/kubetrain/flask:0.1
The push refers to repository [docker.io/kubetrain/flask]
024ad2f1da1a: Pushed 
40864b0a2f62: Pushed 
69d029689e3b: Pushed 
42ce61e841fa: Mounted from library/python 
a9b125f164c3: Mounted from library/python 
e24045f8c247: Mounted from library/python 
b7b662b31e70: Mounted from library/python 
6f5234c0aacd: Mounted from library/python 
8a5844586fdb: Mounted from library/python 
a4aba4e59b40: Mounted from library/python 
5499f2905579: Mounted from library/python 
a36ba9e322f7: Mounted from library/python 
0.1: digest: sha256:368d589fb136b91368d36e35561199f0befca591450ef6b746397de2020d6e5a size: 2843
```

**Step 8: Login to Docker hub and ensure the container image is present**

https://hub.docker.com/repository/docker/kubetrain/flask
