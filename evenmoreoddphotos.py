def main():
    n = int(input().strip())
    nums = []
    for i in input().strip().split():
        nums.append(int(i))

    odds = 0
    evens = 0
    for i in nums:
        if i % 2 == 1:
            odds += 1
        else:
            evens += 1
    if evens > odds:
        ans = (2 * odds) + 1
    elif evens == odds:
        ans = (2 * odds)
    else:
        mod = (n - 2*evens) % 3
        if mod == 0:
            ans = (2 * evens) + (((n-(2*evens)) // 3) * 2)
        elif mod == 2:
            ans = ((2 * evens) + (((n-(2*evens)) // 3) * 2)) + 1
        else:
            odds = odds - 2
            n = n - 2
            if evens > odds:
                ans = (2 * odds) + 1
            else:
                ans = ((2 * evens) + (((n - (2 * evens)) // 3) * 2)) + 1
    print(ans)
main()
