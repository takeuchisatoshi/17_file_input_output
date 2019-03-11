def main():
    f = open("user_data.csv", mode="r")
    print(type(f))

    data = f.read()
    print(type(data))

    f.close()

    print(data)


if __name__ == '__main__':
    main()