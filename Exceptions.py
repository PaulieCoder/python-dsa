class Exception:
    def simpleOps(self):
        try:
            num = 10 / (0 + 1)
        except ZeroDivisionError as err:
            print(err)
        else:
            print("This will execute when the exception didn't occur")
        finally:
            print("This will always execute")
        # raise exception
        try:
            raise NameError
        except NameError:
            print("Name error is raised")

if __name__ == "__main__":
    Exception().simpleOps()