#include<iostream>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;


class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Arrays to track the presence of digits in rows, columns, and sub-grids
        int rowFlags[9] = {0};
        int colFlags[9] = {0};
        int gridFlags[9] = {0};

        // Loop through each cell of the board
        for (int row = 0; row < 9; ++row) {
            for (int col = 0; col < 9; ++col) {
                char cell = board[row][col];

                // Skip empty cells
                if (cell == '.') continue;

                // Convert character digit to a 0-based index
                int digit = cell - '1';

                // Calculate the index of the 3x3 sub-grid
                int gridIndex = (row / 3) * 3 + (col / 3);

                // Check if the digit is already present in the row, column, or sub-grid
                if ((rowFlags[row] & (1 << digit)) ||
                    (colFlags[col] & (1 << digit)) ||
                    (gridFlags[gridIndex] & (1 << digit))) {
                    return false; // Invalid Sudoku board
                }

                // Mark the digit as seen in the row, column, and sub-grid
                rowFlags[row] |= (1 << digit);
                colFlags[col] |= (1 << digit);
                gridFlags[gridIndex] |= (1 << digit);
            }
        }

        return true; // Valid Sudoku board
    }
};

//Valid sudoku better code with hashset from neetcode

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int row = 0; row < 9; row++) {
            unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[row][i] == '.') continue;
                if (seen.count(board[row][i])) return false;
                seen.insert(board[row][i]);
            }
        }
        
        for (int col = 0; col < 9; col++) {
            unordered_set<char> seen;
            for (int i = 0; i < 9; i++) {
                if (board[i][col] == '.') continue;
                if (seen.count(board[i][col])) return false;
                seen.insert(board[i][col]);
            }
        }
        
        for (int square = 0; square < 9; square++) {
            unordered_set<char> seen;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int row = (square / 3) * 3 + i;
                    int col = (square % 3) * 3 + j;
                    if (board[row][col] == '.') continue;
                    if (seen.count(board[row][col])) return false;
                    seen.insert(board[row][col]);
                }
            }
        }
        
        return true;
    }
};
