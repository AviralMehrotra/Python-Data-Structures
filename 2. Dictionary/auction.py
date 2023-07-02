# A program which asks multiple users to enter their name
# as well as their bids ...whoever has the highest bid... WINS

auction = {}  # Dictionary to store the auction details
cont = 1  # Variable to control the loop


def findMax():
    max = 0  # Variable to store the maximum bid amount
    for key in auction:
        highestBid = int(auction[key])  # Convert the bid amount to an integer
        if highestBid >= max:  # Check if the current bid is higher than the maximum bid
            max = highestBid  # Update the maximum bid amount
            Winner = key  # Store the name of the bidder with the highest bid
    # Print the winner and the highest bid amount
    print(f"\n1...2...3...and It's sold to {Winner} at ${max}")


while cont:
    name = input("\nWhat's your Name: ")
    bid = input("\nWhat's your Bid: $")
    # Add the bidder's name and bid amount to the auction dictionary
    auction[name] = bid
    # Prompt the user if there are any other bidders
    x = input("\nIs there anyone else who wants to bid: ").lower()
    if x == "yes":
        continue  # If there are more bidders, continue to the next iteration of the loop
    else:
        findMax()  # If there are no more bidders, call the findMax function to determine the winner
        cont = 0  # Set the value of cont to 0 to exit the loop
