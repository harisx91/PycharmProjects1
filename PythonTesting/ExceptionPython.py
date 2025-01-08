ItemsInCart = 0
#2 items will be added to card

if ItemsInCart != 2:
    #raise Exception("Product Cart Count no matching")
    pass

#Assert expects a condition
assert(ItemsInCart == 0)

##try , catch

try:
    with open("ttest.txt", "r") as reader:
        reader.read()

except:
    print("Somehow I reach here because there is failure in try block")

try:
    with open("ttest.txt", "r") as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up records")