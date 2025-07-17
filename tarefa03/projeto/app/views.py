from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def usuarios(request):
    lista_usuarios = [
        {'nome': 'Ana Silva', 'matricula': '202301', 'idade': 22, 'cidade': 'São Paulo'},
        {'nome': 'Bruno Souza', 'matricula': '202302', 'idade': 25, 'cidade': 'Rio de Janeiro'},
        {'nome': 'Carla Mendes', 'matricula': '202303', 'idade': 20, 'cidade': 'Belo Horizonte'},
        {'nome': 'Diego Lima', 'matricula': '202304', 'idade': 23, 'cidade': 'Recife'},
        {'nome': 'Eduarda Rocha', 'matricula': '202305', 'idade': 21, 'cidade': 'Curitiba'}
    ]
    return render(request, 'usuarios.html', {'usuarios': lista_usuarios})
