import collections

class RpcLogger:
  def __init__(self, timeout=3):
    self._timeout = timeout
    # OrderedDict remembers the order of keys being inserted
    self._active_rpcs = collections.OrderedDict()

  def start(self, id, start_timestamp):
    self._active_rpcs[id] = start_timestamp
    self.clean_timeout_entries(start_timestamp)
  
  def end(self, id, end_timestamp):
    self.clean_timeout_entries(end_timestamp)
    if id in self._active_rpcs:
      print('ID: ', id, ' start: ', self._active_rpcs[id], ' end: ', end_timestamp)
      del self._active_rpcs[id]

  # This is called every time I start or end a process.
  def clean_timeout_entries(self, current_timestamp):
    if self._active_rpcs:
      to_be_removed_keys = []
      for key in self._active_rpcs:
        if self._active_rpcs[key] + self._timeout < current_timestamp:
          to_be_removed_keys.append(key)
          print('ID: ', key, ' start: ', self._active_rpcs[key], 'timeout. Detected at: ', current_timestamp)
        else:
          break
      
      for key in to_be_removed_keys:
        del self._active_rpcs[key]

