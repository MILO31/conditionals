# Determining if someone qualifies
# for a loan.
salary_per_annum =_float(inpt("Enter your salary per annum: "))
eployment_period =_int(input('Enter employment period: '))

if salary_per_annum >= 30000:
    if employment_period >= 2:
        print("You qaulify for a loan")
else:
    print("You do not qaulify for a loan")


# Driver speed

average_speed =_float(input("Enter average speed: "))
allowed_speed =_int(input("Enter your speed: "))
points=(average_speed - allowed_speed )//5

if average_speed <= allowed_speed :
     print("OK")

elif points <= 12:
    print(str(points))
else:
    print("You going to jail")

