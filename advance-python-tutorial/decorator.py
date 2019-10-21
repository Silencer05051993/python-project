def return_welcome(str):
    def welcome():
        return "Hello world"

    return welcome() + " " + str

def return_name(name):
    return name

#-------------------Rewrite---------------------


def return_welcome(fun):
    def welcome(name):
        return "Hello world " + fun(name)
    return welcome


@return_welcome
def return_name(name):
    return name


print(return_name("GeeksforGeeks"))



