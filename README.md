## Proton CRM Demo Project

![proton-orders](https://github.com/davidcoderistov/proton-orders/assets/85624034/e4968a17-dd41-4ef2-93c0-88b3746a82ac)

This project is aimed at showcasing a simple "CRM" feature that enables users to interact with a list of customer orders. The feature retrieves the list of customer orders from a RESTful backend API, displays them on the front end, and allows users to add selected orders to a secondary list called "Follow-up Orders."

## Technologies Used
- Backend: Flask
- Frontend: Vue.js
- Database: MongoDB

## Prerequisites  
Before running the application, ensure that ports 80 and 8080 are available on your system.

## Start the application with docker compose

Navigate to the root directory of the project and execute the following command:
```
$ docker compose up -d
[+] Running 5/5
 ✔ Network proton-orders_default       Created                                                                                                                                 0.0s 
 ✔ Container proton-orders-mongo-1     Started                                                                                                                                 3.2s 
 ✔ Container proton-orders-backend-1   Started                                                                                                                                 3.4s 
 ✔ Container proton-orders-frontend-1  Started                                                                                                                                 3.7s 
 ✔ Container proton-orders-web-1       Started 
```

## Expected result

Listing containers must show four containers running and the port mapping as below:
```
$ docker ps
CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS          PORTS                    NAMES
b81ff43ed1bd   nginx                    "/docker-entrypoint.…"   34 seconds ago   Up 32 seconds   0.0.0.0:80->80/tcp       proton-orders-web-1
d4cd983d6872   proton-orders-frontend   "docker-entrypoint.s…"   47 seconds ago   Up 32 seconds   0.0.0.0:8080->8080/tcp   proton-orders-frontend-1
e8deba67a986   proton-orders-backend    "python3 server.py"      47 seconds ago   Up 33 seconds                            proton-orders-backend-1
fa72f88e5274   mongo                    "docker-entrypoint.s…"   47 seconds ago   Up 33 seconds   27017/tcp                proton-orders-mongo-1
```

After the application starts, navigate to `http://localhost:8080` in your web browser.

## Stop the application with docker compose

Navigate to the root directory of the project and execute the following command:
```
$ docker compose down
[+] Running 5/5
 ✔ Container proton-orders-web-1       Removed                                                                                                                                 0.4s 
 ✔ Container proton-orders-frontend-1  Removed                                                                                                                                 0.3s 
 ✔ Container proton-orders-backend-1   Removed                                                                                                                                 1.1s 
 ✔ Container proton-orders-mongo-1     Removed                                                                                                                                 0.4s 
 ✔ Network proton-orders_default       Removed    
```
