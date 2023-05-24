months={
    30:['April','June','September','November'],
    31:['Jan','March','May','July','August','Oct','December'],
    29:['February'],
    28:['February'] }
a=int(input("Enter the no:of dates :"))
if a==30:
    print(months[30])
elif a==31:
    print(months[31])
elif a==29:
    print(months[29])
elif a==28:
    print(months[28])

