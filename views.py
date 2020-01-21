from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.exceptions import HTTPError
requests.get('https://api.github.com')
response = requests.get('https://api.github.com')
response.status_code
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')
if response:
    print('Success!')
else:
    print('An error has occurred.')
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}') 
    except Exception as err:
        print(f'Other error occurred: {err}')  
    else:
        print('Success!')
response = requests.get('https://api.github.com')
response.content
response.json()
response.headers
response.headers['Content-Type']
requests.post('https://httpbin.org/post', data={'key':'value'})
requests.put('https://httpbin.org/put', data={'key':'value'})
requests.delete('https://httpbin.org/delete')
requests.head('https://httpbin.org/get')
requests.patch('https://httpbin.org/patch', data={'key':'value'})
requests.options('https://httpbin.org/get')
# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'Raunak'})

def sub(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1-val2
    return render(request,'result.html',{'result':res})
def add(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1+val2
    return render(request,'result.html',{'result':res})
def mul(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1*val2
    return render(request,'result.html',{'result':res})
def div(request):
    val1=int(request.GET['num1'])
    val2=int(request.GET['num2'])
    res=val1/val2
    return render(request,'result.html',{'result':res})

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 
choice = input("Enter choice(1/2/3/4): ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if choice == '1':
   print(num1,"+",num2,"=", add(render))
elif choice == '2':
   print(num1,"-",num2,"=", sub(render))
elif choice == '3':
   print(num1,"*",num2,"=", mul(render))
elif choice == '4':
   print(num1,"/",num2,"=", div(render))
else:
   print("Invalid input")

    
    