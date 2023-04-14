def str_into_lis(string):
    respons = []
    for item in string[1:-2].split("\","):
        item = item.strip()
        respons.append(item[1:].replace('"', "'"))
    return respons

def lis_into_str(lis):
    str_array = "["
    for item in lis:
        str_array += f'"{item}", '
    
    return str_array[:-2]+"]"


if __name__ == "__main__":
    str_ls = '["user", "salom", "qalesiz?", "admin", "yaxshi raxmat", "o"zingizchi"]'
    
    array = str_into_lis(str_ls)
    # print(type(array))
    # print(array)
    
    str_ls = lis_into_str(array)
    print(type(str_ls))
    print(str_ls)