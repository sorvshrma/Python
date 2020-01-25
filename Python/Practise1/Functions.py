import classes

def func(user, *users):
    print("This is first argument: "+ user)

    for u in users:
        print("this is second argument: " + u)

func("Sourav" , 'Kanchan', 'Oggy' , 'prafful' )

ob = classes.call()
ob._call__func()