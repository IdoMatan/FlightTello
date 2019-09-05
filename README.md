# TelloControl

## Install
```
$ pip install git+....
```
or
```
$ git clone .....
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