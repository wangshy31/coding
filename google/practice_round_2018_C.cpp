#include <iostream>
#include <map>

using namespace std;


int main() {
  int t;
  long long n;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    map <string, string> flight;
    map <string, string> reverse_flight;
    string begin, end;
    cin >> begin >> end;
    flight[begin] = end;
    reverse_flight[end] = begin;
    map <string, string>::iterator it;
    for (it = reverse_flight.begin(); )
    
    
    cout << "Case #" << i << ": "<<result<<endl;

  }

  return 0;
}

