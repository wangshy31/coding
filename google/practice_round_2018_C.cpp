#include <iostream>
#include <map>
#include <fstream>

using namespace std;


int main() {
  int t;
  int n;
  ifstream fin("input.txt");

  fin >> t;  // read t. cin knows that t is an int, so it reads it as such.
  ofstream fout("log.txt");
  for (int i = 1; i <= t; ++i) {
      fin >> n;
      map <string, string> flight;map <string, string> reverse_flight;
      for (int j = 1; j <= n; j++) {
        string begin, end;
        fin >> begin >> end;
        flight[begin] = end;
        reverse_flight[end] = begin;
      }
      map <string, string>::iterator it;
      string begin_city = "";
      for (it = reverse_flight.begin(); it !=reverse_flight.end(); it++ ){
        if (reverse_flight.count(it->second)==0){
            begin_city = it->second;
            break;
        }
      }
      fout << "Case #" << i << ": ";
      for (int j = 1; j <=n; j++) {
          fout<<begin_city<<"-"<<flight[begin_city]<<" ";
          begin_city = flight[begin_city];
      }

      fout<<endl;
  }

  return 0;
}

