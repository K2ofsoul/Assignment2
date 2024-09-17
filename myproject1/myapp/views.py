from django.shortcuts import render
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import io
import urllib, base64

def home(request):
    plt.plot(range(10)) 
    fig = plt.gcf() 
    
    buf = io.BytesIO()  
    fig.savefig(buf, format='png') 
    buf.seek(0) 
    
    string = base64.b64encode(buf.read())  
    uri = urllib.parse.quote(string) 
    
    return render(request, 'myapp/home.html', {'data': uri}) 
