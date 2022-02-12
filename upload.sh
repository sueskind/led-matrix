#!/bin/bash

set -e

arduino-cli compile --fqbn esp32:esp32:esp32 .
arduino-cli upload -p /dev/ttyUSB0 --fqbn esp32:esp32:esp32:UploadSpeed=921600 .
minicom -D /dev/ttyUSB0 -b 115200
