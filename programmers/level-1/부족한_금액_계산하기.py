def solution(price, money, count):
    # print(money - count * (price + price*count)//2)
    return max(count * (price + price*count)//2 - money, 0)

if __name__ == "__main__":
    price = 3
    money = 20
    count = 4
    print(solution(price, money, count))