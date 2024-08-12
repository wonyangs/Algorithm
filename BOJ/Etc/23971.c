#include <stdio.h>

int main(void) {

    int H, W, N, M;

    scanf("%d %d %d %d", &H, &W, &N, &M);
    printf("%d", ((H + N) / (N + 1)) * ((W + M) / (M + 1)));

    return 0;
}
