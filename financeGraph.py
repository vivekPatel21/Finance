import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

# Getter for names
def getNames(finances):
    return [line.split()[0] for line in finances]

# Getter for values
def getValues(finances):
    return [float(line.split()[1]) for line in finances]

# Generate distinct colors
def getColors(num_colors):
    cmap = cm.get_cmap('tab20', num_colors)  # Use the 'tab20' colormap for up to 20 distinct colors
    return [cmap(i) for i in range(num_colors)]

# Display current finances
def display(filename):
    # Get the data from the file
    with open(filename, "r") as f:
        finances = f.readlines()

    # Parse names and values
    names = getNames(finances)
    values = getValues(finances)

    # Generate distinct colors
    colors = getColors(len(names))

    # Create pie chart
    plt.pie(values, labels=names, autopct='%1.1f%%', startangle=140, colors=colors)
    #plt.pie(values, labels=names,colors=colors)
    
    plt.title("Current Finances")
    plt.show()


# Python entry point
if __name__ == "__main__":
    print("select your following options:")

    while True:
        print("option '1': display current")
        print("option '2': change record.txt")
        print("option 'd': quit")
        choice = input("Enter your choice: ")
        if(choice == 'd'):
            break

        if(choice == 1):
            display("record.txt")
            continue
        elif(choice == 2):
            changeRecord()
            continue
        else:
            print("That was not valid")