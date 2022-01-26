def calculatePay():
    
    # This first line is provided for you
    pay = 0.0
    try:
        hrs = float(input("Enter Hours: "))
        rate = float(input("Enter Rate: "))   
    except:
        print("Error, please enter numeric input")
        exit()
    if hrs > 40.0:
        overtime = hrs-40
        overtime *= (rate*1.5)
        pay = (40*rate)+overtime
        print ("Pay: " + str(pay))
    else:
        pay = hrs*rate
        print ("Pay: " + str(pay))
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculatePay()