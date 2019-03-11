class List:
    def __init__(self, name, age, price):
    self.name = name
    self.age = age
    self.price = price

def main():

    f = open("user_data.csv", mode="r")
    data = f.read()
    print(data)
    print("--------")

    data2 = data.replace('\n',",")
    print(data2)
    print("--------")

    data_list = data2.split(",")
    print(data_list)
    print("--------")

    print(data_list[0])
    print(data_list[3])
    print(data_list[6])



if __name__ == '__main__':
    main()