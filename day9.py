from replit import clear
record={}
def max_bid(record):
    for name in record:
        if record[name]==max(record.values()):
            return name


bidders=True
while(bidders==True):
    name=input("Enter your name: ")
    bid=input("Enter bid amount: $")
    temp={name:bid}
    record[name]=bid
    status=input("Are there  any more bidders? (yes/no): ").lower()
    if status=="no":
        bidders=False
        
    elif status=="yes":
        clear()
    
    else:
        print("Invalid input! Please enter 'yes' or 'no'.")
    
clear()
print(f"The winner is {max_bid(record)} with a bid of ${max(record.values())}.")
