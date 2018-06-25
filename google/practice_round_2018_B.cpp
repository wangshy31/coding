#include <iostream>
using namespace std;


int S(long long length, long long index) {
    if ((index*2 - 1) == length)
        return 0;
    else if ((index*2 - 1) < length)
        return S((length - 1) / 2, index);
    else {
        return (1 - S((length - 1) / 2, length + 1 - index)); 
    }
         
}
int main() {
  int t;
  long long k;

  cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  for (int i = 1; i <= t; ++i) {
    cin >> k;
    long long rval = 1;  
    int count = 0;
    while(rval-1<k) {
        rval<<=1;  
        count++;
    }
    int result = S(rval - 1, k);
    //int result = next_p2()
    cout << "Case #" << i << ": "<<result<<endl;

  }

  return 0;
}

