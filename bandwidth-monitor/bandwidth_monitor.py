import os
import re
import subprocess
import time

BYTES_IN_KB = 1024
BYTES_IN_MB = 1048576
BYTES_IN_GB = 1073741824

def get_bytes(stdout):
  start = end = 0
  if os.name == 'nt':
    start = stdout.find('Bytes', 0, len(stdout))
    end = stdout.find('\\r', start, len(stdout))
    output = stdout[start:end]
    return re.split(r'\s+', output)[1:]
  elif os.name == 'posix':
    raise NotImplemented
  else:
    raise NotImplemented

def format_speed(speed_in_bytes:int):
  if speed_in_bytes < BYTES_IN_KB:
    return str(speed_in_bytes) + ' bytes/sec'
  elif speed_in_bytes >= BYTES_IN_KB and speed_in_bytes < BYTES_IN_MB:
    # kilobytes
    return str(speed_in_bytes / BYTES_IN_KB) + ' kbytes/sec'
  elif speed_in_bytes >= BYTES_IN_MB and speed_in_bytes < BYTES_IN_GB:
    # megabytes
    return str(speed_in_bytes / BYTES_IN_MB) + ' mbytes/sec'
  else:
    # gigabytes
    return str(speed_in_bytes / BYTES_IN_GB) + ' gbytes/sec'

rx_bytes = current_rx_bytes = previous_rx_bytes = tx_bytes = current_tx_bytes = previous_tx_bytes = 0
args = []
if os.name == 'nt':
  args.extend(['netstat', '-e'])
elif os.name == 'posix':
  args.extend(['netstat', '-s'])
else:
  raise NotImplementedError
completed_proc = subprocess.run(args, input=None, capture_output=True, timeout=None)
full_output = str(completed_proc.stdout)
start = full_output.find('Bytes', 0, len(full_output))
end = full_output.find('\\r', start, len(full_output))
output = full_output[start:end]
output = re.split(r'\s+', output)[1:]
previous_rx_bytes = int(output[0])
previous_tx_bytes = int(output[1])
time.sleep(1)
for i in range(6000):
  completed_proc = subprocess.run(['netstat', '-e'], input=None, capture_output=True, timeout=None)
  full_output = str(completed_proc.stdout)
  start = full_output.find('Bytes', 0, len(full_output))
  end = full_output.find('\\r', start, len(full_output))
  output = full_output[start:end]
  output = re.split(r'\s+', output)[1:]
  current_rx_bytes = int(output[0])
  current_tx_bytes = int(output[1])
  rx_bytes = current_rx_bytes - previous_rx_bytes
  tx_bytes = current_tx_bytes - previous_tx_bytes
  previous_rx_bytes = current_rx_bytes
  previous_tx_bytes = current_tx_bytes
  rx_speed = format_speed(rx_bytes)
  tx_speed = format_speed(tx_bytes)
  print('rx:', rx_speed, '\ntx:', tx_speed)
  time.sleep(1)
  

print(completed_proc.stdout)