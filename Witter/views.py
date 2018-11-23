from django.shortcuts import render



def signup(request):
    print("****************************************************")
    if request.method=="POST":
        firstname=request.POST.get['Firstname']
        lastname=request.POST.get['Lastname']
        date_of_birth=request.POST.get['dob']
        email=request.POST.get['email']
        gender=request.POST.get['gender']
        pic=request.POST.get['pic']

        context ={"firstname":firstname,
        "lastname":lastname,
        'date_of_birth':date_of_birth,
        'email':email,
        'gender':gender,
        'pic':pic,

        }
        return render (request,"Witter/display.html", context)
    else:
        print("/////////////////////////////////")
        return render(request,"Witter/signup.html")








        # Firstname:<input type="text" name="firstname">
        #     Lastname:<input type="text" name="firstname">
        #     email:<input type="text" name="firstname">
        #     DateOfBirth:<input type="date" name="dob">
        #     <input type="radio" name="gender" value="male" checked> Male<br>
        #     <input type="radio" name="gender" value="female"> Female<br>
        #     <input type="radio" name="gender" value="other"> Other<br><br>
        #     <input type="file" name="pic" accept="image/*">
        #     <input type="submit" value="S