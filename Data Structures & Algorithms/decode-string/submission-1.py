class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = []
        string_stack = []

        curr_number = 0
        curr_string = ""

        for ch in s:
            if ch.isdigit():
                curr_number = curr_number * 10 + int(ch)

            elif ch == '[':
                number_stack.append(curr_number)
                string_stack.append(curr_string)

                curr_number = 0
                curr_string = ""

            elif ch == ']':
                repeat = number_stack.pop()
                previous = string_stack.pop()

                curr_string = previous + curr_string * repeat 

            else :
                curr_string += ch

        return curr_string

                 

