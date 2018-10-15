int Solution::coverPoints(vector<int> &A, vector<int> &B) {
    int m = 0;
    int n = A.size();
    for(int i = 1; i < n; i++)
    {
        m += max(abs(A[i]- A[i-1]), abs(B[i]-B[i-1]));
    }

    return m;
}
