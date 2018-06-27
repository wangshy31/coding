#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cmath>
#include <math.h>
#include <algorithm>
using namespace std;

long long int a[200005];
long long int b[200005];

long long int tot,small;
int N;
long long int calc(long long int index)
{
    long long int low=small,high=tot,mid=(low+high)>>1,less=0,equal=0,ans=0,cnt;
    int i,j;

    while(low<=high)
    {
        //cout<<"low is : "<<low<<" "<<"high is: "<<high<<" mid is: ";
        mid=(low+high)>>1;
        //cout<<mid<<" ";
        less=0;
        equal=0;
        j=0;

        for(i=1;i<=N;i++)
        {
            while(j<i&&(a[i]-a[j])>mid)
                j++;


            if(i!=j)
            {
                if(a[i]-a[j]==mid)
                {
                    equal++;
                    less+=i-1-j;
                }
                else
                    less+=i-j;
            }

        }
        //cout<<"less is: "<<less<<" equal is: "<<equal<<endl;
        //cout<<mid<<" "<<less<<" "<<equal<<endl;
        if(less+equal<index)
            low=mid+1;
        else if(less>index)
            high=mid-1;
        else if(less+equal>=index)
            break;
    }

    ans+=(index-less)*mid;
    j=0;
    for(i=1;i<=N;i++)
    {
        while(j<i&&(a[i]-a[j])>mid)
            j++;

        if(j!=i)
        {
            if((a[i]-a[j])==mid)
            {
                ans+=(i-j-1)*a[i]-(b[i-1]-b[j]);
            }
            else
                ans+=(i-j)*a[i]-(b[i-1]-b[j-1]);
        }

    }
    return ans;
}

int main()
{
    int T,t,Q;
    long long int l,r;
    int i,j;

    freopen("in.txt","r",stdin);
    freopen("out3.txt","w",stdout);
    cin>>T;

    for(t=1;t<=T;t++)
    {
        cin>>N>>Q;
        tot=0;
        small=200;
        for(i=1;i<=N;i++)
        {
            scanf("%lld",&a[i]);
            //cout<<a[i]<<" ";
            small=small>a[i]?a[i]:small;
            a[i]+=a[i-1];
            tot+=a[i];
            b[i]=tot;
        }
        tot = a[N];
        //cout<<endl;
        cout<<"Case #"<<t<<":"<<endl;

        //for (i = 1; i<=N; i++)
            //cout<<a[i]<<" ";
        //cout<<endl;
        //for (i = 1; i<=N; i++)
            //cout<<b[i]<<" ";
        //cout<<endl;

        for(i=0;i<Q;i++)
        {
            cin>>l>>r;
            //cout<<"left and right: "<<l<<" "<<r<<endl;
            long long int ans= calc(r)-calc(l-1);
            cout<<ans<<endl;
        }

    }
    return 0;
}
