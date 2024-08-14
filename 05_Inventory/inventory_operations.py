import json
import time

#Add User
def add_user(get_details=False):
    userfile=open('e:/DataScience/01_python/05_Inventory/Files/all_users.json','r')
    users=userfile.read()
    userfile.close()

    user_details=json.loads(users)
    
    if get_details==False:
        user_Id=user_ph=input("Enter Mobile Number: ") 

        try:
            found=user_details[user_Id]
            print("Mobile Number already exists with following Details: ")
            print("User Name  : ",found["user_name"])
            print("Email ID   : ",found["user_mail"])
            print("Mobile No. : ",found["user_mail"])
        except KeyError:
            user_name=input(      "Enter Name         : ")
            user_mail=input(      "Enter Email        : ")
            user_details[user_Id]={}
            user_details[user_Id]['user_name']=user_name
            user_details[user_Id]['user_mail']=user_mail
            user_details[user_Id]['user_mobile']=user_ph
            user_details[user_Id]['registration_date']=time.ctime()

            user_details[user_Id]['history']=[]
            ud=json.dumps(user_details)
            userfile=open('e:/DataScience/01_python/05_Inventory/Files/all_users.json','w')
            userfile.write(ud)
            userfile.close()

    return user_details[user_Id]

# add_user()

#add item to the inventory   
def add_item():
    jsf=open('e:/DataScience/01_python/05_Inventory/Files/record.json','r')
    js=jsf.read()
    jsf.close()

    inventory=json.loads(js)
    product_id=input(      "Enter Product Id       : ")
    try:
        found=inventory[product_id]
        print("Item already exits with same ID")
        if input("Press Y to add more and N to exit:")=='Y':
            add_item()
        else: 
            print("Thank you")        
    except :    
        product_name=input(    "Enter Product Name     : ")
        product_price=input(   "Enter Product Price    : ")
        product_quantity=input("Enter Product Quantity : ")

        inventory[product_id]={}
        inventory[product_id]['product_name']=product_name
        inventory[product_id]['product_price']=product_price
        inventory[product_id]['product_quantity']=product_quantity
        
        dt=json.dumps(inventory)
        f=open('e:/DataScience/01_python/05_Inventory/Files/record.json','w')
        f.write(dt)
        f.close()
        print("Product Added!")

        if input("Want to add more Y/N:  ")=='Y':
            add_item()

# add_item()

def update_inventory(ui_pid,ui_qty):
    jsf=open('e:/DataScience/01_python/05_Inventory/Files/record.json','r')
    js=jsf.read()
    jsf.close()
    inventory=json.loads(js)
    if not ui_pid in inventory:
        add_item()
    else:
        if not (int(ui_qty) <= 0):
            inventory[ui_pid]["product_quantity"]=ui_qty

    data=json.dumps(inventory)
    f=open('e:/DataScience/01_python/05_Inventory/Files/record.json','w')
    f.write(data)
    f.close()    

def update_sales(info,user_id):
    fd=open('e:/DataScience/01_python/05_Inventory/Files/sales.csv','a')
    fd.write(info)
    fd.close()

    userfile=open('e:/DataScience/01_python/05_Inventory/Files/all_users.json','r')
    s=userfile.read()
    userfile.close()

    users=json.loads(s)
    users[user_id]["history"].append(info)

    us=json.dumps(users)
    userfile=open('e:/DataScience/01_python/05_Inventory/Files/all_users.json','w')
    userfile.write(us)
    userfile.close()


#Display Menu, input user product demand and Bill
def process_request():
    jsf=open('e:/DataScience/01_python/05_Inventory/Files/record.json','r')
    js=jsf.read()
    jsf.close()

    inventory=json.loads(js)
    # Display menu
    print("Menu".center(60,'-'))
    print("Product ID".center(15,' '),"Product Name".center(25,' '),"Product Price".center(20,' '))
    print("-"*60)
    i=1
    for id,val in inventory.items():
        print(id.center(15,' '),val['product_name'].center(25,' '),val['product_price'].center(20,' '))
        if i==5:
            if input("Want to see more Y/N:  ")=='N':
                break
        i+=1

    #input user product demand
    
    user_details=add_user()
    print('-'*60)
    ui_pid=input("Enter the product ID: ")
    ui_p_qty=input("Enter the product Quantity: ")

    print("User Details".center(60,'-'))
    print("User Name  : ",user_details['user_name'])
    print("User Mobile: ",user_details['user_mobile'])
    print("User Mail: ",user_details['user_mail'])
    
    for id,product in inventory.items():
        
        if(ui_pid==id):
            if(int(ui_p_qty)<=int(product["product_quantity"])):
                print("Receipt".center(60,'-'))
                print("Product Name      : ",product['product_name'])
                print("Product Price     : ",product['product_price'])
                print("Product Quantity  : ",ui_p_qty)
                print("Bill".center(60,'-'))
                cost=int(ui_p_qty)*int(product['product_price'])
                print("Total Amount  :  Rs.",cost)
                print("-"*60)

                product_quantity_left=str(int(product["product_quantity"])-int(ui_p_qty))
                update_inventory(ui_pid,product_quantity_left)
                info=user_details['user_name']+','+user_details['user_mobile']+','+user_details['user_mail']+ui_pid+','+product['product_name']+','+ui_p_qty+','+str(cost)+','+time.ctime()+'\n'
                update_sales(info,user_details['user_mobile'])

            else:
                if product['product_quantity']!='0' and input(f"We have only {product['product_quantity']} do you want to buy Y/N:  ")=='Y':
                    ui_p_qty=product['product_quantity']
                    print("Receipt".center(60,'-'))
                    print("Product Name      : ",product['product_name'])
                    print("Product Price     : ",product['product_price'])
                    print("Product Quantity  : ",ui_p_qty)
                    print("Bill".center(60,'-'))
                    cost=int(ui_p_qty)*int(product['product_price'])
                    print("Total Amount  :  Rs.",cost)
                    print("-"*60)

                    # update inventory
                    product_quantity_left=str(int(product["product_quantity"])-int(ui_p_qty))
                    update_inventory(ui_pid,product_quantity_left)
                    info=user_details['user_name']+','+user_details['user_mobile']+','+user_details['user_mail']+ui_pid+','+product['product_name']+','+ui_p_qty+','+str(cost)+','+time.ctime()+'\n'
                    #update sales
                    update_sales(info,user_details['user_mobile'])
               
                elif(product['product_quantity']=='0'):
                    print("sorry! we do not have much quantity of this product.")
                    print("Please Buy something else")
                    print("Thanking You")
                else: print("Product ID not found.")
            
#Update inventory
#Update Sales and user details 