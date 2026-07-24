class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;

        for (int i = 0; i < 32; i++) {
            res <<= 1;          // make room at the bottom
            res |= (n & 1);     // drop in n's current lowest bit
            n >>= 1;            // advance to the next bit
        }

        return res;
    }
};