class Numbers:

    def simpleOps(self):
        num1 = 5
        num2 = 11
        float_output = num2 / num1
        integer_output = num2 // num1
        remainder = num2 % num1
        print('float output : ' + str(float_output) )
        print('integer output : ' + str(integer_output) )
        print('remainder output : ' + str(remainder) )
        #You can't add a str and int you need to typecast it
        #You can add any types of numbers - float, int
        float_num = 10.1
        int_num = 1
        print(float_num + int_num)

    def otherOps(self):
        num = 2
        res = pow(2,2)
        print(res)
        num1 = 2.44444
        num1 = round(num1, 2)
        print(num1)
        #Python variables has to initialized with something - numbers, string

Numbers().simpleOps()
Numbers().otherOps()