# mouse-movement-app

## 1. Application description
The application tracks the movement of the mouse and when the left mouse’s button is pressed a picture is taken with the connected webcam.

## 2. Technologies
 - Python
 - FastAPI
 - Multithread / asyncio
 - Websockets
 - Pyserial
 - openCV 
 - SQLite

## 3. API Architecture

### 1) Controller is split between application layer(`routers`) and business logic(`services`)

## 4. Instructions on how to setup and run the project locally

### 1) You can set local virtual environment using your terminal and the commands are:
- For Linux/Mac: 
    - `python3 -m venv .venv`
    - `.venv/bin/activate`
- For Windows: 
    - `py -m venv .venv`
    - `.venv\Scripts\activate`

### 2) The modules that are used for this project can be found in `requirements.txt`. You can install them in your terminal using the command:
- For Linux/Mac: 
    - `python3 -m pip install -r requirements.txt`
- For Windows: 
    - `py -m pip install -r requirements.txt`

### 3) When you are ready with the instructions above you need to go to the `main.py` file and run it to start your server. 

### 4) Once your server is on you can use your browser to check the functionality of the app
- `http://127.0.0.1:8000`

### 5) When you start using the app a folder `saved_pictures` and a data base file `mouse_data` would be created.