import os  
  
def main():  
    connection_string = os.environ.get('SERVICE_ACCOUNT_KEY')   
    print(connection_string)  # Imprime la cadena de conexión   
  
if __name__ == '__main__':  
    main()  
