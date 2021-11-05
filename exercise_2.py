def e_mail(text):
    x = 0
    y = 0

    for i in text:
        if i == "@":
            x += 1
        if i == ".":
            y +=1

    if x > 0 and y > 0:
        print("That's an e-mail.")
    
    else:
        print("That is not an e-mail. Please try again.")

texta = str(input("Please write a string:"))

e_mail(texta)