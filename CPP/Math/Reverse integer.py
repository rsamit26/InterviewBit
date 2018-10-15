class Solution {
public:
    int reverse(int x) {
    // solution without using strings
    int rev = 0, sign = 1, digit;
    if (x < 0) {
        sign = -1;
        x *= -1;
    }
    while (x > 0) {
        digit = x%10;
        // check for overflow here
        if (rev > (INT_MAX / 10) || (rev == (INT_MAX / 10) && digit > (INT_MAX % 10))) {
            return 0;
        }
        rev = rev * 10 + digit;
        x/=10;
    }
    rev *= sign;
        return rev;
    }
};
