def product(arr,n,mod):
    # your code here
    ans=1
    for i in arr:
        ans*=i
    return ans%mod
