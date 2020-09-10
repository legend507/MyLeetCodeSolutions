/**
 * start(n): initialize the server at a starting sequence n
 * ack(n): this is called when a sequence number n is received.
 * getHWM()
 */

#include <unordered_map>  // Std hashmap.
#include <unordered_set>  // This stores unique single values

class JobServer  {
  public:
  void start(int n) {
    _hwm = n;
  }
  int getHWM() const {return _hwm;}

  int ack(int n) {
    // Received an old duplicated sequence number.
    // Also, making sure that _acked does NOT have numbers smaller than _hwm.
    if(n <= _hwm)  return 0;

    // 
    _acked.insert(n);
    int leap = 0; // How mnay numbers _hwm forwarded.
    while (true) {
      // it can either be null or a pointer to _hwm + 1.
      auto it = _acked.find(_hwm + 1);

      // This if happens when _hwm+1 can NOT be found.
      if (it == _acked.end()) {break;}

      // If we found _hwm + 1.
      _acked.erase(it);
      ++ _hwm;
      ++ leap;
    }
    
    return leap;
  }

  private:
  int _hwm;
  std::unordered_set<int> _acked;

};