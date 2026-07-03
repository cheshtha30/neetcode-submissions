class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_string = ""
        curr_number = 0

        for ch in s:
            if ch.isdigit():
                curr_number = curr_number *10 + int(ch)

            elif ch == '[':
                stack.append((curr_string , curr_number))
                curr_string = ""
                curr_number = 0

            elif ch == ']':
                prev_string , repeat = stack.pop()
                curr_string = prev_string + curr_string * repeat

            else:
                curr_string += ch

        return curr_string
