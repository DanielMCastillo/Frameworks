from django.shortcuts import render

def sumar(request):
    num1 = num2 = 0
    resultado = ''
    
    if request.method == 'POST':
        print(request.POST)
        op = request.POST.get('operacion', None)
        
        try:
            num1 = float(request.POST.get('num1', None))
            num2 = float(request.POST.get('num2', None))
            cal = Calculadora()
            resultado = cal.operacion(op, num1, num2)
                
        except Exception as e:
            resultado = 'Verifica tus datos '+str(e)
    
    context = {
        'resultado':resultado,
        'num1':num1,
        'num2':num2,
    }
    botones = [
        {'simbolo':'0'}
        
    ]
    return render(request, 'calculadora.html', context)

class Calculadora:
    
    
    def operacion(self, op, num1, num2):
        operaciones = {
            'Sumar': self.sumar(num1, num2),
            'Restar': self.restar(num1, num2)
        }
        return operaciones[op]
    
    def sumar(self, num1, num2):
        return num1 + num2
    
    def restar(self, num1, num2):
        return num1 - num2