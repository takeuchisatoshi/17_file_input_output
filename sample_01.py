def main():
    f = open("user_data.csv", mode="r")
    # print(type(f))

    data = f.read()
    print("close()する前", f.closed)

    f.close()
    print("close()した後", f.closed)

    print(data)


if __name__ == '__main__':
    main()