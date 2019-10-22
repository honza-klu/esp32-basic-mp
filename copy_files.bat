ampy --port %ESP_PORT% put src/device/boot.py
ampy --port %ESP_PORT% put src/device/main.py
ampy --port %ESP_PORT% put src/device/requirements.txt
ampy --port %ESP_PORT% put src/device/ssl_http_server.py
ampy --port %ESP_PORT% put src/device/priv.key
ampy --port %ESP_PORT% put src/device/cert.txt
ampy --port %ESP_PORT% mkdir lib
ampy --port %ESP_PORT% put src/device/lib/auto_connect.py lib/auto_connect.py
ampy --port %ESP_PORT% put src/device/lib/ftp.py lib/ftp.py
ampy --port %ESP_PORT% put src/device/lib/urequests.py lib/urequests.py
ampy --port %ESP_PORT% put src/device/lib/pkg_resources.py lib/pkg_resources.py
ampy --port %ESP_PORT% put src/device/lib/upip.py lib/upip.py
ampy --port %ESP_PORT% mkdir lib/picoweb
ampy --port %ESP_PORT% put src/device/lib/picoweb/utils.py lib/picoweb/utils.py
ampy --port %ESP_PORT% put src/device/lib/picoweb/__init__.py lib/picoweb/__init__.py
ampy --port %ESP_PORT% mkdir lib/uasyncio
ampy --port %ESP_PORT% put src/device/lib/uasyncio/core.py lib/uasyncio/core.py
ampy --port %ESP_PORT% put src/device/lib/uasyncio/__init__.py lib/uasyncio/__init__.py