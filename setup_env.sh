ENV=pistem

python3 -m venv $HOME/$ENV

source $HOME/$ENV/bin/activate

pip3 install hcsr04sensor

pip install raspberrypi-tm1637

pip3 install adafruit-circuitpython-ads1x15

pip3 install adafruit-circuitpython-bme280