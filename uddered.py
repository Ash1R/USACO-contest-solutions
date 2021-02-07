def main():
    alph = input().strip()
    word = list(input().strip())
    ans = 0
    check = False
    while True:
        ans +=1
        for i in alph:
            if i == word[0]:
                word.pop(0)
            if word == []:
                check = True
                break
        if check:
            break
    print(ans)
main()
