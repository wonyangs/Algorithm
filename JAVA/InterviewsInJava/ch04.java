package JAVA.InterviewsInJava;

public class ch04 {
    public static short countBits(int x) {
        short numBits = 0;
        while (x != 0) {
            numBits += (x & 1);
            x >>>= 1;
        }
        return numBits;
    }

    public static short parity(long x) {
        x ^= x >>> 32;
        x ^= x >>> 16;
        x ^= x >>> 8;
        x ^= x >>> 4;
        x ^= x >>> 2;
        x ^= x >>> 1;
        return (short)(x & 0x1);
    }

    public static long swapBits(long x, int i, int j) {
        if (((x >>> i) & 1) != ((x >>> j) & 1)) {
            long bitMask = (1L << i) | (1L << j);
            x ^= bitMask;
        }
        return x;
    }

    public static long closestIntSameBitCount(long x) {
        final int NUM_UNSIGNED_BITS = 63;
        for(int i = 0; i < NUM_UNSIGNED_BITS-1; ++i) {
            if((((x >>> i) & 1) != ((x >>> (i+1))& 1))) {
                x ^= (1L << i) | (1L << (i + 1));
                return x;
            }
        }
        throw new IllegalArgumentException("");
    }

    public static long reverse(int x) {
        long result = 0;
        long xRemaining = Math.abs(x);
        while (xRemaining != 0) {
            result = result * 10 + xRemaining % 10;
            xRemaining /= 10;
        }
        return x < 0 ? -result : result;
    }

    public static boolean isPalindromeNumber(int x) {
        if (x < 0) {
            return false;
        }

        final int numDigits = (int)(Math.floor(Math.log10(x))) + 1;
        int msdMask = (int)Math.pow(10, numDigits - 1);
        for (int i = 0; i < (numDigits / 2); ++i) {
            if ( x / msdMask != x % 10) {
                return false;
            }
            x %= msdMask;
            x /= 10;
            msdMask /= 100;
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(countBits(15));
    }
}
