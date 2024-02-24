class Solution:
    def reverseBits(self, n: int) -> int:
        binary_string = bin(n)[2:].zfill(32)
        reverse_bits = int((binary_string)[::-1], 2)
        return reverse_bits