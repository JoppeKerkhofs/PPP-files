from django.shortcuts import render
import second_app.forms as forms

# Create your views here.
def index(request):
    return render(request, 'second_app/index.html')

def help(request):
    help_dict = {'help_insert': "HELP PAGE"}
    return render(request, 'second_app/help.html', context=help_dict)

def users(request):
    # user_list = User.objects.order_by('firstName')
    # user_dict = {'users': user_list}
    # return render(request, 'second_app/users.html', context=user_dict)
    form = forms.NewUserForm()

    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM INVALID")

    return render(request, 'second_app/users.html', {'form': form})
