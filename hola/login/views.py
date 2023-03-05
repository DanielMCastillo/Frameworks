from django.shortcuts import render

def login(request):
    mensaje = None
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        mensaje = 'Usuario no válido'
        if username == 'alex' and password == 'admin1234':
            mensaje = f"Bienvenido al sistema {username}"
        
    return render(request, 'login.html', {'mensaje':mensaje})