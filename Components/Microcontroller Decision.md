# Micro Controller Design Decision wiki!
## Pros and Cons of Raspberry Pi

---Pros---
- Linux Accessible
- Smaller compare to Raspberry B+ models
- Offers a Vast amount of peripheral support
- Combine digital and sensor inputs
- Portable

---Cons---
- Over heating
- A powerful processor causes the pi to heat up 
- Impractical use of a desktop computer

Show a plan of the resources you are going to use from your microcontroller, and how [30]. 

We will be using serial communication pin for ESP32 Chip to provide Bluetooth and Wi-Fi communication.
Power supply pins, 3V3 and 5V used to give voltage to outputs such as the ESP32, LEDs, and GSM GSM/GPRS/GNSS HAT

-----Below are the images of the Pinout for Raspberry Pi Zero----------
<img width="741" alt="raspberry pi Zero w" src="https://github.com/user-attachments/assets/723cd974-e2de-44cb-b87a-54d0f33c4133">


![JtpG7](https://github.com/user-attachments/assets/d4f3e993-5870-4e95-8d57-fdb43c61d3bf)



Show parameters you already know or have to determine, for instance duty/cycle and frequency settings for a timer that generates a PWM signal [20]. 

All Pis run at 3.3V, but need to be supplied with 5V for some peripherals. Knowing this, will need to implement a dc to dc converter that offers voltage protection for our Raspberry Pi.

In terms of configuration, we plan to ssh to connect to the Raspberry Pi






Source: 
https://robu.in/5-pros-and-5-cons-of-raspberry-pi/
