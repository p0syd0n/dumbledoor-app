import socketio
SERVER = 'https://dumbledoor.posydon.repl.co'

sio = socketio.Client()
sio.connect(SERVER, wait_timeout = 10)  # replace with the actual server URL

def send_command(id, repeat, command, param1=None, param2=None, param3=None):
    data = {'type': 'command', 'repeat': int(repeat), 'command': command, 'param1': str(param1), 'param2': str(param3), 'param3': str(param3), 'param4': str(param4), 'api': 'True'}
    sio.emit('api_start_command', data=data)

@sio.on('connect')
def handle_connect():
    print('Connected to server')

@sio.on('message')
def handle_message(data):
    print('Received message:', data)
    
def get():
    return str(input("dumbledoor$ "))

def menu():
    print("Dumbledoor App")
    print("by posydon")

def shell():
    menu()
    while True:
        input = get()
        

#sio.emit('my_event', {'key': 'value'})
