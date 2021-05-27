from django.shortcuts import render, redirect
import qrcode
from pathlib import Path

def index(request):
    if request.method == 'POST':#nessa condição o app sempre espera alguma ação q vem do botao do HTML
        home = Path.home()
        path_image = home / 'Downloads' #path de onde o QRCODE i´ra ficar salvo
        
        url = request.POST.get('link')#link que vem do formulario la do HTML
        nome = request.POST.get('nome')#nome do arquivo que vem do formulario la do HTML
        
        if url != '':
            img = qrcode.make(url)#Converter os dados
                
            img.save(f'{path_image}/{nome}.png')#Salvando a imagem/qrcode
        else:
            print('deu merda')
    else:
        pass
    return render(request, 'html/main.html')