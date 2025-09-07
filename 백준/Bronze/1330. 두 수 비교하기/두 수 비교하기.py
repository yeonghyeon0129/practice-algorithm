def main():
    n_list = list(map(int, input().split(' ')))
    a = n_list[0]
    b = n_list[1]

    result = "=="
    if a > b:
        result = ">"
    elif a < b:
        result = "<"
    
    print(result)


if __name__ == "__main__":
    main()