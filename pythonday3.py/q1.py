amount = int(input("Enter the amount to withdraw (must be a multiple of 100): "))
notes_2000 = notes_500 = notes_200 = notes_100 = 0
if amount % 100 != 0:
    print("Invalid amount. Please enter an amount that is a multiple of 100.")
else:
    if amount >= 2000:
        notes_2000 = amount // 2000
        amount = amount % 2000

    
    if amount >= 500:
        notes_500 = amount // 500
        amount = amount % 500

    #
    if amount >= 200:
        notes_200 = amount // 200
        amount = amount % 200

    
    if amount >= 100:
        notes_100 = amount // 100

    output = "Please take "
    if notes_2000 > 0:
        output += f"{notes_2000} notes of 2000 Rupees, "
    if notes_500 > 0:
        output += f"{notes_500} notes of 500 Rupees, "
    if notes_200 > 0:
        output += f"{notes_200} notes of 200 Rupees, "
    if notes_100 > 0:
        output += f"{notes_100} notes of 100 Rupees, "

    output = output.rstrip(', ')
    print(output)

