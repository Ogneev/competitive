'''
A sequence of integers is called a beautiful sequence if all the integers in it are positive and
it is a strictly increasing sequence.

Given a sequence of integers, you have to make it a beautiful sequence. For that you can change any element you want,
but you should make as less changes as possible in order to make it a beautiful sequence.

Input

The first line of input is an integer T(T <= 5), the number of test cases. Each test case contains 2 lines.

The first line of the test case contains an integer (0 < N <= 100000),
i.e. the number of elements in the original sequence.

The second line contains N positive integers, no larger than 2000000000, which forms the original sequence.

Output
For each test case output the minimal number of elements you must change in the original sequence to make it a beautiful sequence.

Explanation for sample Input/Output

For the 1st test case you needn't to change any elements.
For the 2nd test case you can change 3 into 1 and change 1 into 3.
For the 3rd test case you can change 10 into 1.
For the 4th test case you can change the last three 2s into 3,4 and 5.

UPDATE

Test cases have been made stronger and all previous submissions have been rejudged.

SAMPLE INPUT
4
2
1 2
3
3 2 1
5
10 5 6 7 8
4
2 2 2 2
SAMPLE OUTPUT
0
2
1
3

'''

t = int(input())
for _ in range(t):
    elements = int(input())
    sequence = list(map(int, input().split()))
    if sorted(sequence) == sequence and sequence[0] > 0 and len(set(sequence)) == len(sequence):
        print(sequence)
        print(0)
    else:
        steps = 0
        if sequence[0] >= sequence[1]:
            steps += 1
            sequence[0] = 1
        for i in range(1, len(sequence)-1):
            if sequence[i] > sequence[i-1] and sequence[i] >= sequence[i+1]:
                prev = sequence[i]
                try:
                    sequence[i] = min(range(sequence[i-1] + 1, sequence[i+1]))
                except ValueError:
                    sequence[i+1] = sequence[i] + 1
                if sequence[i] != prev:
                    steps += 1
        print(sequence)
        print(steps)