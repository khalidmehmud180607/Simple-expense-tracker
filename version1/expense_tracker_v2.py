# function to get the total expense
# def Total(data):
#     summ=0
#     res=category_wise_data(data)
#     for x in res.values():
#         summ=summ+x
#     return summ

#another way
def Total (data):
    summ=0
    for x in data:
        summ=summ +x["Price"]
    return summ
# function to get data categorized
def category_wise_data(data):
    res={}
    for dicto in data:
        res[dicto["Category"]]=res.get(dicto["Category"],0)+dicto["Price"]
    return res
#function to count the number of expense of a category
def category_count(data,category):
    count =0
    for dicto in data:
        if dicto["Category"]==category:
            count=count + 1
    return count
#delete an expense
def delete_expense(ll,dele):
    t=0
    for i in ll :
        if i["Name"]==dele:
            del ll[t]
            return True
        else:
            t=t+1
    return False
#this function will get the  maximum spending category
def highest_spend(data):
    hc=""
    hv=-1234
    for i,j in data.items():
        if hv < j:
            hv = j
            hc = i
    print(f"Highest spend Category : {hc}\nHighest spend money : {hv}\nPercentage : {hv*100/Total(l):.2f}%")
#this function will get the minimum spending category
def lowest_spend(data):
    lc=""
    lv=999999999
    for i , j in data.items():
        if lv> j:
            lv=j
            lc=i
    print(f"Lowest spend Category : {lc}\nLowest spend money : {lv}\nPercentage : {lv*100/Total(l):.2f}%")
# the programme mainly start from here 
print("----HI! Welcome!----")
username=input("What is your name : ")
firstname , * lastname=username.split()
l=[]
budget=10000
while True :
    print("\n")
    print(f"{firstname}....\nType the option number to choose an option...\nOPTION 1)Add expense\nOPTION 2)View reports\nOPTION 3)View expense of one category\nOPTION 4)Set budget\nOPTION 5)Delete an expense\nOPTION 6)Amount check\nOPTION 7)Quit")
    try:
        a=int(input("Choose an option or pick QUIT to quit the  app : "))
    except ValueError:
        print("Error! The entered number is not within the option!")
        continue
    if a==1:
        name=input("Product or service name : ").strip().lower()
        try:
            price=int(input("Price of the product or service : "))
        except ValueError:
            print("Error! The entered price is not valid!")
            continue
        if price<0:
            print("Error! You input negative price!")
            continue
        category=input("Category of the product or service: ").strip().lower()
        if category=="food" or category=="transport" or category=="bills" or category=="shopping" or category=="health":
            l.append({
                "Name":name,"Price":price,"Category":category
                    })
        else:
            category="other"
            l.append({
                "Name":name,"Price":price,"Category":category
                })
    elif a==2:
        if len(l)==0:
            print("You have entered zero expense yet")
        else:
            res=category_wise_data(l)
            print("-----My expense report of this month-----")
            print(f"You spend a total of {Total(l)} TAKA\n\n----The spending summary----")
            for k,s in res.items():
                print(f"Category : {k}\nPrice : {s}")
            remain=budget-Total(l)
            if remain > 0:
                print(f"Remaining budget : {remain}")
            elif remain <0:
                print(f"You have exceeded your budget limit by {-1*remain}")
            else:
                print("You have finished all your budget :(")
    elif a==3:
            dicto=category_wise_data(l)
            print("Category list.....\n1)food\n2)transport\n3)bills\n4)shopping\n5)health\n6)other")
            cate=input("Choose which category you want to see(type the category) : ").strip().lower()
            if cate in dicto:
                count=category_count(l,cate)
                print(f"Category : {cate}\nTotal number of expense of this category : {count}\nTotal amount : {dicto[cate]}")
            else:
                print("You didnt enter anything of this category ")
            # try:
            #     d=int(input("Choose whice category you want to see (type the option number) : "))
            # except ValueError:
            #     print("Error! The entered datatype is not valid!")
            #     continue
            # if d==1:
            #     if dicto.get("food",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"food")
            #         print(f"Category : food\nTotal number of expense of this category : {count}\nTotal amount : {dicto["food"]}")
            # elif d==2:
            #     if dicto.get("transport",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"transport")
            #         print(f"Category : transport\nTotal number of expense of this category : {count}\nTotal amount : {dicto["transport"]}")
            # elif d==3:
            #     if dicto.get("bills",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"bills")
            #         print(f"Category : bills\nTotal number of expense of this category : {count}\nTotal amount : {dicto["bills"]}")
            # elif d==4:
            #     if dicto.get("shopping",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"shopping")
            #         print(f"Category : shopping\nTotal number of expense of this category : {count}\nTotal amount : {dicto["shopping"]}")  
            # elif d==5:
            #     if dicto.get("health",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"health")
            #         print(f"Category : health\nTotal number of expense of this category : {count}\nTotal amount : {dicto["health"]}")  
            # elif d==6:
            #     if dicto.get("other",0)==0:
            #         print("You didnt enter anything of this category ")
            #     else:
            #         count=category_count(l,"other")
            #         print(f"Category : other\nTotal number of expense of this category : {count}\nTotal amount : {dicto["other"]}") 
            # else:
            #     print("Invalid category")
    elif a==4:
        try:
            new_budget=int (input("Set your budget : "))
        except ValueError:
            print ("Error! The entered budget is not valid!")
            continue
        if new_budget < 0:
            print("Error! You input negative budget")
            continue
        budget=new_budget
        if budget==0:
            print("Your budget is zero! Are you sure about it!")
    elif a==5:
        if len(l)!=0:
            dele=input("Delete product or service : ").strip().lower()
            if delete_expense(l,dele):
                print("Deleted")
            else:
                print("No matching product or service")
        else:
            print("There is no expense to delete!")
    elif a==6:
            print(f"Your budget was {budget}\nspend : {Total(l)}")
            remain=budget-Total(l)
            if remain > 0:
                print(f"Remaining budget : {remain}")
            elif remain <0:
                print(f"You have exceeded your budget limit by {-1*remain}")
            else:
                print("You have finished all your budget :(")
    elif a==7:
        break
    else:
        print("Input invalid")
print("\n----------------------------------------")
if len(l)!=0:
    print("---------EXPENSE SUMMARY----------")
    res=category_wise_data(l)
    total_expense=Total(l)
    for c,v in res.items():
        print(f"Category : {c}\nPrice : {v}\nCount : {category_count(l,c)}")
    print(f"TOTAL : {total_expense}")
    remain=budget-Total(l)
    if remain > 0:
        print(f"Remaining budget : {remain}")
    elif remain <0:
        print(f"You have exceeded your budget limit by {-1*remain}")
    else:
        print("You have finished all your budget :(")
    highest_spend(res)
    lowest_spend(res)
    
else:
    print(f"You didnt spend any money\nRemaining money : {budget}")