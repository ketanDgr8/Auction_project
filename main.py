from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)



data_dict={}
other_user_Flag=True
i=1
while other_user_Flag is True:
  person_dict={}
  person_dict["name"]=input("What is your Name:")
  person_dict["bid_price"]=int(input("what is bid price:"))

  data_dict[i]=person_dict
  clear()
  more_user=input("Do you want to add more bidders: yes/no:").lower()
  if more_user=="yes":
    other_user_Flag=True
    i+=1
  else:
    other_user_Flag=False

#print(data_dict)
b_price=0
h_bidder={}
for entry in data_dict:
  if data_dict[entry]["bid_price"] >= b_price:
    b_price=data_dict[entry]["bid_price"]
    h_bidder=data_dict[entry]
    
    
print(h_bidder)


