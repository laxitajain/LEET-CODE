class Solution {
public:
    bool isPalindrome(int x) {
        long long r=0,temp;
        temp=x;
        while(x>0)
        {
         r=r*10+x%10;
         x=x/10;
        }
        if(r==temp)
         return true;
        else
         return false;
    }
};
