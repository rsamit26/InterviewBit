

int Solution::gcd(int m, int n) {

    if (m==0){
        return n;
    }

    return gcd(n%m, m);

}
