# TelloControl

## Install
```
$ pip install git+https://github.com/matanweks/FlightTello
```
or
```
$ git clone https://github.com/matanweks/FlightTello.git
$ 
$ pip install -e ./TelloControl
```

## Usage

### Simple example

```python
from TelloControl.tello import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)

tello.land()
tello.end()
```