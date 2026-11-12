print("Hi ! Welcome !")
expense=[]
def category_wise_data(data):
    res={}
    for dict in data:
        res[dict["category"]]=res.get(dict["category"],0)+ dict["amount"]
    return res
def Total(data):
    total =0
    for i in data.values():
        total =total + i 
    return total
while True :
    print("...Press done if you want to finish...")
    name=input("product or service name : ")
    if name == "done":
        break
    amount =int(input("Enter the estimated product or service amount : "))
    category=input ("Enter the service or profuct category : ")
    if category =="":
        category="other"
    expense.append({"name":name,"amount":amount,"category":category})
if len(expense)==0:
    print("You didnt entered any product or service yet")
else:
    res=category_wise_data(expense)
    print("\n\n")
    print("----MONTHLY REPORT----")
    total=Total(res)
    hcategory=""
    hamount=-1234
    print(f"TOTAL: {total} TAKA")
    for c , a in res.items():
        print(f"{c}: {a} TK ({round(a*100/total)}%)")
        if hamount<a:
            hamount=a
            hcategory=c
    print(f"You spent the most on {hcategory}: {hamount} TK")
    print("----------------------")
    print("\n")