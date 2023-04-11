class Solution:
    def decodeString(self, s: str) -> str:
        stack_str = []
        stack_num = []
        curr_str = ''
        k = 0

        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == '[':
                stack_num.append(k)
                stack_str.append(curr_str)
                curr_str = ''
                k = 0
            elif c == ']':
                prev_str = stack_str.pop()
                repeat_times = stack_num.pop()
                curr_str = prev_str + repeat_times * curr_str
            else:
                curr_str += c

        return curr_str