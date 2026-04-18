int reverse(int n) {
    int res = 0;
    while (n != 0) {
        res = (res * 10) + (n % 10);
        n /= 10;
    }
    return res;
}

int mirrorDistance(int n) {
    int res = reverse(n) - n;
    if (res < 0) {
        return -res;
    }
    return res;
}
