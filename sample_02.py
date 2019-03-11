def main():
    f = open("sale.csv", mode="w")

    f.write("1月,150万円\n")
    f.write("2月,60万円\n")
    f.write("3月,200万円\n")

    f.close()


if __name__ == '__main__':
    main()
