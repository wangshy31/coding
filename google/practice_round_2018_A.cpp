#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <vector>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

typedef struct bus {
    int begin;
    int end;
}bus;

int main() {
  int t, n, P;
 // vector <bus> a;
 // vector <int> city;
  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    int result[5001] = {0};
    cin >> n;
    for (int j = 1; j <= n; j++) {
        bus onebus;
        cin >> onebus.begin >> onebus.end;
        //a.push_back(onebus);
        for (int k = onebus.begin; k <= onebus.end; k++) {
            result[k]++;
        }
    }
    cin>>P;
    cout << "Case #" << i << ": ";
    for (int m = 1; m <= P; m++) {
        int city_num;
        cin >> city_num;
        cout << result[city_num] << " ";
    }
    cout<<endl;
    // cout knows that n + m and n * m are ints, and prints them accordingly.
    // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
  }

  return 0;
}
