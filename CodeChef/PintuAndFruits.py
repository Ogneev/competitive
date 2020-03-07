'''
Chef went to Australia and saw the destruction caused by bushfires, 
which made him sad, so he decided to help the animals by feeding them fruits. 
First, he went to purchase fruits from Pintu.

Pintu sells M different types of fruits (numbered 1 through M). He sells them in N baskets (numbered 1 through N), 
where for each valid i, the i-th basket costs Pi and it contains fruits of type Fi. 
Chef does not have too much money, so he cannot afford to buy everything;
instead, he wants to choose ONE of the M available types and purchase all the baskets containing fruits of that type.

Help Chef choose the type of fruit to buy such that he buys at least one basket 
and the total cost of the baskets he buys is the smallest possible.

Input:

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains two space-separated integers N and M.
The second line contains N space-separated integers F1,F2,…,FN.
The third line contains N space-separated integers P1,P2,…,PN.


Output:

For each test case, print a single line containing one integer ― the minimum price Chef must pay.

Constraints:

1≤T≤1,000
1≤M,N≤50
1≤Fi≤M for each valid i
0≤Pi≤50 for each valid i

Subtasks
Subtask #1 (30 points): M=2
Subtask #2 (70 points): original constraints

Example Input
1
6 4
1 2 3 3 2 2
7 3 9 1 1 1
Example Output
5
Explanation
Example case 1:

The sum of all baskets with fruits of type 1 is 7.
The sum of all baskets with fruits of type 2 is 5.
The sum of all baskets with fruits of type 3 is 10.
The sum of all baskets with fruits of type 4 is 0 because there are no such baskets.
Chef can only choose fruits of type 1, 2 or 3. Therefore, the minimum price he has to pay is 5.
'''''

t = int(input())


def ans():
    n, m = map(int, input().split())
    baskets = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    track = {}
    for i in range(n):
        track[baskets[i]] = 0
    for i in range(n):
        track[baskets[i]] += prices[i]
    return min(track.values())


for i in range(t):
    print(ans())