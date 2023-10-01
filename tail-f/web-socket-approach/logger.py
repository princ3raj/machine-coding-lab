import time

with open("Apache_2k.log", "r") as read_f:
    with open("index.log", "a") as f:
        bytes = read_f.readlines()
        for byte in bytes:
            f.write(byte)
            f.flush()
            time.sleep(1)
