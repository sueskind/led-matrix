# led-matrix

Decorative LED dot matrix frame powered by an ESP32.

## Setup

1. Install Python dependencies:
    ```shell
    pip install -r requirements
    ```

2. Create missing `animations.ino` from template:
    ```shell
    python compile-animations.py
    ```

3. Compile/upload ESP32 code, either with *Arduino IDE* (or you tool of choice) **or** with *arduino-cli*:
    ```shell
    bash upload.sh
    ```
