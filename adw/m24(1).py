months={
    30:['April','June','September','November'],
    31:['Jan','March','May','July','August','Oct','December'],
    29:['February'],
    28:['February'] }
a=(input("Enter the month :"))
if a in months[30]:
    print(30)
elif a in months[31]:
    print(31)
elif a in months[29]:
    print(29)
elif a in months[28]:
    print(28)