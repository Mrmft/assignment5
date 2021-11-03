

PRODUCTS = []
def load_data_from_database():
    f = open('database.csv')
    content = f.read().split('\n')
    for item in content:
        info = item.split(',')
        info_dict = {'Id': int(info[0]) , 'name': info[1] , 'price': int(info[2]) , 'tedad': int(info[3])}
        PRODUCTS.append(info_dict)
    f.close()
    
def save_data_to_database():
    f = open('database1.csv', 'w')
    for item in PRODUCTS:
        Id= str(item['Id'])
        name= item['name']
        price= str(item['price'])
        tedad= str(item['tedad'])
        result= Id + "," + name + ',' + price + ',' + tedad + '\n'
        file_result = str('')
        file_result += result
                   
    f.write(file_result)
    f.close()
        
def add():
    name= input("enter the product name: ")
    price= input("enter the product price: ")
    tedad= input("enter the product tedad: ")
    info_dict1 = {'Id': PRODUCTS[-1]['Id'] + 1 , 'name': name , 'price': price , 'tedad': tedad}
    PRODUCTS.append(info_dict1)
    

def edit():
    pass

def delete():
    print('delete by: \n1.Id\n2.name')
    choice_del=input()
    if choice_del == '1' or choice_del == "Id":
        Id_del= input("enter the product Id you want to delete: ")
        for item in PRODUCTS:
            if Id_del in str(item["Id"]):
                PRODUCTS.remove(item)
                return
    else:
        name_del= input("enter the product name you want to delete: ")
        for item in PRODUCTS:
            if name_del in item["name"]:
                PRODUCTS.remove(item)
                return
    
        
def show_list():
    for product in PRODUCTS:
        print (product)

def search():
    print('search by: \n1.Id\n2.name')
    choice_search=input()
    if choice_search == '1' or choice_search == "Id":
        Id_search= input("enter the product Id you want to search: ")
        for item in PRODUCTS:
            if Id_search in str(item["Id"]):
                index_number= PRODUCTS.index(item)
                print(item)
                return index_number
    else:
        name_search= input("enter the product name you want to delete: ")
        for item in PRODUCTS:
            if name_search in item["name"]:
                index_number= PRODUCTS.index(item)
                print(item)
                return index_number

def buy():
    pass

def show_menu():
    print('welcome to mmd store')
    print('1- add')
    print('2- edit')
    print('3- delete')
    print('4- show list')
    print('5- search')
    print('6- buy')
    print('7- exit')
    print('8- save')
    
    
load_data_from_database()
while True:
    show_menu()
    choice = int(input('please enter your choice:'))
    
    if choice == 1 :
        add()
    elif choice == 2 :
        edit()
    elif choice == 3 :
        delete()
    elif choice == 4 :
        show_list()
    elif choice == 5 :
        search()
    elif choice == 6 :
        buy()
    elif choice == 7 :
        break
    elif choice == 8 :
        save_data_to_database()
        
        
        
        
        
            