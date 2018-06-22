#include <vector>
#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;

int main() {
    int n, m;
    double sum = 0, discount = 0;
    int ai; bool di;
    cin >> n >> m;
    for(int i = 0;i < n;i++) {
        cin >> ai >> di;
        if(di) {
            discount += ai * 0.8;
        } else {
            discount += ai;
        }
        sum += ai;
    }
    double result;
    int bi; int ci;
    result = discount;
    for( int i = 0;i < m;i++) {
        cin >> bi >> ci;
        if(sum > bi) {
            result = min(result, sum - ci);
        }
    }
    cout<<setiosflags(ios::fixed)<<setprecision(2)<<result<<endl;
    return 0;
}
