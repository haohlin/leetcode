class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0 for i in range(len(num1) + len(num2))]
        for i in reversed(range(len(num2))):
            for j in reversed(range(len(num1))):
                cur_idx = i + j
                mul = int(num2[i]) * int(num1[j])
                sum_i = result[cur_idx + 1] + mul
                result[cur_idx] += sum_i // 10
                result[cur_idx + 1] = sum_i % 10
        result = ''.join(list(map(str, result)))
        return str(int(result))
                