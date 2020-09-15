#include <vector>
#include <string>

const int _STUCK = -1;
const int _FALL_THRU_SIDES = -2;

// O(R)
class BallMaze {
public:
  // The representation of the board is the key.
  std::vector<std::string> board;

  void flip(int row, int col) {
    board[row][col] = '/' + '\\' - board[row][col];
  }

  int drop(int col) {
    int row = 0;
    int R = board.size();
    int C = board[0].size();

    while (row < R) {
      // Case 1: we see a '\'
      if (board[row][col] == '\\') {
        // Edge cases.
        if (col == C-1) return _FALL_THRU_SIDES;
        if (board[row][col+1] == '/') return _STUCK;

        // '\' will cause the ball move to right, hence col++.
        row ++;
        col ++;
      } 
      // Case 2: we see a '/'      
      else {
        // Edge cases.
        if (col == 0) return _FALL_THRU_SIDES;
        if (board[row][col - 1] == '\\') return _STUCK;

        row ++;
        col --;
      }
    }
    return col;
  }
};