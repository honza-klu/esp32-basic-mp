python -m esptool --port %ESP_PORT% erase_flash
python -m esptool --port %ESP_PORT% --baud 460800 write_flash --flash_size=detect 0x1000 ./src/other/esp32-20180511-v1.9.4.bin