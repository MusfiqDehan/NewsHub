<h1 align="center"> NewsHub</h1>
  <p align="center"> A multi-functional News Aggregator web app using Django</p>
  
***Home Page***
![home-latest](https://user-images.githubusercontent.com/47440165/120078143-d341cc00-c0cf-11eb-8af6-81507ac5d15c.png)

**_Archive Page_**
![archive](https://github.com/MusfiqDehan/newshub/blob/master/static/Screenshots/archive.png)

## Live Demo

https://newshub-nl2p.onrender.com

## How to run on your own pc

-   Clone or Download on repository

```
git clone https://github.com/MusfiqDehan/newshub.git
```

-   Change Directory <br>
    `cd newshub-master`

-   Install dependencies from requirements.txt file <br>
    `pip3 install -r requirements.txt`

-   Run migrations and migrate to update database <br>
    `python3 manage.py makemigrations && python3 manage.py migrate`

-   Run server on localhost and open website in a browser <br>
    `python3 manage.py runserver 8000`

-   This newshub app will be live on <br>
    `http://127.0.0.1:8000/`
