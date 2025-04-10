#include<bits/stdc++.h>

using namespace std;
using ll = long long;

int main(){
	int n, S; cin >> n >> S;
	int w[n + 1], v[n + 1];
	
	for(int i = 1; i <= n; i++) cin >> w[i];
	for(int i = 1; i <= n; i++) cin >> v[i];
	
	int dp[n+1][S+1];
	memset(dp, 0, sizeof(dp));
	
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= S; j++){
			// Khong chon do vat thu i bo vao tui
			dp[i][j] = dp[i-1][j];
			// Co the dua do vat thu i vao tui
			if(j >= w[i]){
				dp[i][j] = max(dp[i][j], dp[i-1][j-w[i]] + v[i]);
			}
		}
	}
	for(int i = 1; i <= n; i++){
		for(int j = 1; j <= S; j++){
			cout << dp[i][j] << " ";
		}
		cout << "\n";
	}
	cout << dp[n][S];
}