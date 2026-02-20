
def homogenous_list_to_hetrogenous_list(data):
    ret_list = []
    for val in data:
        if type(val) != str:
         ret_list.append(val)
    return ret_list

print(homogenous_list_to_hetrogenous_list(["hello",45,5.6,"appu","peksha",True ,{"name":"Apeksha","age":21}]))

