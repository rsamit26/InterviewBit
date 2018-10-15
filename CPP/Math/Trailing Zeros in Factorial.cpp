/* Description

when a number have factor as 5 and 2 we have a zero in the trail

loop through the given number:
  find no of 5, 25, 125, 625....
  since multiple of 5 has extra no of fives so count them
  and return total count

*/

int Solution::trailingZeroes(int n) {
    int zeros = 0;
    int mul = 5;
    while(n/mul>0){
        zeros += n/mul;
        mul *= 5;
    }
    return zeros;

}
