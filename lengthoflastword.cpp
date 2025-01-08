#include <iostream>
#include <string>
using namespace std;

int lengthOfLastWord(const string& s) {
    int length = 0;
    int i = s.size() - 1;

    // Skip trailing spaces
    while (i >= 0 && s[i] == ' ') {
        i--;
    }

    // Count the length of the last word
    while (i >= 0 && s[i] != ' ') {
        length++;
        i--;
    }

    return length;
}

int main() {
    string s;
    cout << "Enter a string: ";
    getline(cin, s);

    int result = lengthOfLastWord(s);
    cout << "The length of the last word is: " << result << endl;

    return 0;
}
