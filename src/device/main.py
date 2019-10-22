# Main application file
import gc

print("MAIN START")

def main():
  print("Type your code here!")
  gc.collect()
  #import ssl_http_server
  #ssl_http_server.start()

try:
  import machine
  import time
  #run main app here to reset on unhandled exceptions
  main()
except Exception as e:
  print("Unhandled exception:%s" % (str(e),))
  print("Runtime error encountered. Restarting in 10s")
  time.sleep(60.0)
  print("Restarting now!")
  machine.reset()
print("MAIN END")