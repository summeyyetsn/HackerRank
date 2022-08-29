"""
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between.
Example
n=5
Print the string 12345.
Input Format
The first line contains an integer n.
Constraints
1<=n<=150
Output Format
Print the list of integers from 1 through n as a string, without spaces.
"""
if __name__ == '__main__':
    def print_function(n):
        my_output=""
        for i in range(1,n+1):
            i=str(i)
            my_output+=i
        print(my_output)
    n = int(input())
    print_function(n)