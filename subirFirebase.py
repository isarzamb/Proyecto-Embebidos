import os
import socket
import RPi.GPIO as GPIO
#import serial 
from time import*
from firebase import firebase
from http.server import BaseHTTPRequestHandler, HTTPServer

firebase = firebase.FirebaseApplication('https://proyectozambrano-d1c46-default-rtdb.firebaseio.com/', None)
#ser = serial.Serial("/dev/ttyACM0", baudrate=9600)

luz1 = 5
luz2 = 6
luz3 = 12
luz4 = 13
AC1 = 16
AC2 = 19
Temp = 10
myip = socket.gethostbyname(socket.gethostname())
print (myip)


def estadoluz1():
 firebase.put("/EstadoLuz", "/luz1", GPIO.input(luz1))
 
def estadoluz2():
 firebase.put("/EstadoLuz", "/luz2", GPIO.input(luz2))
 
def estadoluz3():
 firebase.put("/EstadoLuz", "/luz3", GPIO.input(luz3))
 
def estadoluz4():
 firebase.put("/EstadoLuz", "/luz4", GPIO.input(luz4))
 
def estadoAC1():
 firebase.put("/EstadoAC", "/AC1", GPIO.input(AC1))
 
def estadoAC2():
 firebase.put("/EstadoAC", "/AC2", GPIO.input(AC2))

def estadoTemp():
 firebase.put("/EstadoTemp", "/Temperatura", GPIO.input(Temp))
 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(luz1, GPIO.OUT)
 GPIO.setup(luz2, GPIO.OUT)
 GPIO.setup(luz3, GPIO.OUT)
 GPIO.setup(luz4, GPIO.OUT)
 GPIO.setup(AC1, GPIO.OUT)
 GPIO.setup(AC2, GPIO.OUT)
 GPIO.setup(Temp, GPIO.IN)
 
 GPIO.add_event_detect(Temp,GPIO.RISING,estadoTemp,bouncetime=30)
 
 estadoluz1()
 estadoluz2()
 estadoluz3()
 estadoluz4()
 estadoAC1()
 estadoAC2()
 estadoTemp()
 
def servidor():
 Request = None

 class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
   global Request

   messagetosend = bytes('Solicitando',"utf")
   self.send_response(200)
   self.send_header('Content-Type', 'text/plain')
   self.send_header('Content-Length', len(messagetosend))
   self.end_headers()
   self.wfile.write(messagetosend)
   Request = self.requestline
   Request = Request[5 : int(len(Request)-9)]
   #print(Request)
   if Request == 'on1':
    print('luz1 encendida')
    GPIO.output(luz1,True)
    
   if Request == 'off1':
    print('luz1 apagada')
    GPIO.output(luz1,False)
      
   if Request == 'on2':
    print('luz2 encendida')
    GPIO.output(luz2,True)
    
   if Request == 'off2': 
    print('luz2 apagada')
    GPIO.output(luz2,False)
      
   if Request == 'on3':
    print('luz3 encendida')
    GPIO.output(luz3,True)
    
   if Request == 'off3':
    print('luz3 apagada')
    GPIO.output(luz3,False)
   
   if Request == 'on4':
    print('luz4 encendida')
    GPIO.output(luz4,True)
    
   if Request == 'off4':
    print('luz4 apagada')
    GPIO.output(luz4,False)
  
   if Request == 'on5':
    print('AC1 encendido')
    GPIO.output(AC1,True)
    
   if Request == 'off5':
    print('AC1 apagado')
    GPIO.output(AC1,False)
    
   if Request == 'on6':
    print('AC2 encendido')
    GPIO.output(AC2,True)
    
   if Request == 'off6':
    print('AC2apagado')
    GPIO.output(AC2,False)
    
 server_address_httpd = (myip,8001)
 httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
 print('conectando a servidor')
 print(httpd.fileno())
 httpd.serve_forever()
 
def main () :

# Setup
 peripheral_setup()

# Infinite loop
 try:
  while 1 :  
   servidor()
   '''
   comando = input("Ingresar comando (on/off): ")
   comando = comando + "\n"
   comandoBytes = comando.encode()
   ser.write(comandoBytes)
   time.sleep(0.1)
   read = ser.readline()
   print(read)
   '''
   #pass
 except(KeyboardInterrupt,SystemExit):
  print ("BYE")
  GPIO.cleanup()
# Command line execution
if __name__ == '__main__' :
   main()
