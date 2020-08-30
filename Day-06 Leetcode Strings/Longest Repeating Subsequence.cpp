#include <iostream>
using namespace std;

int main() {
	int n;
	cin>>n;
	while(n>0)
	{
	    int a;
	    string s;
	    cin>>a;
	    cin>>s;
	    
	    int dp[a+1][a+1];
	    for(int i=0;i<=a;i++)
	    {
		dp[i][0]=0;
        }
	
	    for(int j=0;j<=a;j++)
	    {
		dp[0][j]=0;
        }
        
        for(int i=1;i<=a;i++)
	    {
	    for(int j=1;j<=a;j++)
	    {
			if(s[i-1]==s[j-1] && i!=j)
			{
			dp[i][j]=dp[i-1][j-1]+1;
			}
            else
			{
			dp[i][j]=max(dp[i-1][j],dp[i][j-1]);
		    }
	    }
	    }
	    cout<<dp[a][a]<<endl;
	    n=n-1;
	}
	return 0;
}