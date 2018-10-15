int Solution::isPalindrome(int n) {
    int original = n;
    int reversed = 0;
    if (n < 0){
        return 0;
    }
    else{
        while(n>0){
            reversed = reversed*10 + n%10;
            n /= 10;
        }
        if (reversed == original){
            return 1;
        }else{
            return 0;
        }
    }
}
