# Alex Baldree - Module 1 Assignment: Beer Bottle Countdown

def beer_song(bottles):
    # Loop from the number of bottles down to 1
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down and pass it around, {bottles - 1} bottle(s) of beer on the wall.\n")
        else:
            # When there's only one bottle left
            print(f"{bottles} bottle of beer on the wall, {bottles} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1


# Main Program
def main():
    num_bottles = int(input("Enter number of bottles: "))
    beer_song(num_bottles)
    print("Time to buy more beer!")


# Run the main function
if __name__ == "__main__":
    main()
