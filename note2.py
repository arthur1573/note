import note

print("-----------------------------")
print(" ")
print("This will always be run 2.")


print("The second module's name = {}".format(__name__))


def main():
    print(
    """
    This will NOT always be run. 
    This module's name = {}
    """
    .format(__name__))
    
    
 

if __name__ == "__main__":
    main()
else:
    print("this module is run from import.")

