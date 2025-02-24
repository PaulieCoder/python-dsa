class Input:
    def fun(self):
        string = input("Enter a string : ")
        sal_age = input("Enter salary and age : ")
        sal_age = sal_age.split(' ')
        sal = float(sal_age[0])
        age = int(sal_age[1])
        print("His name is {}".format(string))
        print("His salary is {}".format(sal))
        print("His age is {}".format(age))
        print(type(age))
        pass

if __name__ == "__main__":
    Input().fun()