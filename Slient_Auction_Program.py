import os
print("*****Welcome to The Slient Auction Program*****")
def find_winner(bidder_detailes):
    higest_bid=0;
    winner=""
    for bidder in bidder_detailes:
        bidder_price = bidder_detailes[bidder]
        if bidder_price>higest_bid:
            higest_bid=bidder_price
            winner=bidder
    print(f"All bidder's details {bidder_detailes}")    
    print(f"The winner is {winner} with a bid price of {higest_bid}")
        
    
bidder_data={}
end_of_bidding= False
while not end_of_bidding:
    name=input("What is your name : ")
    price=int(input("What is your bid ? : "))
    bidder_data[name]=price
    more_bidders=input("Are There more bidders ? Type 'yes' or 'no' : " ).lower()
    if more_bidders=='no':
        end_of_bidding=True
        find_winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')