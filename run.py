import devices
from multiprocessing import Process



def start_broker(front_port: int, back_port: int):
    p = Process(target=devices.start_new_broker, args=(
        front_port, back_port))
    p.start()

def start_server(front_port: int, stock: str, stock_value: float):
    p = Process(target=devices.start_new_server, args=(
        front_port, stock, stock_value))
    p.start()

def start_sub(back_port: int, stock: str):
    p = Process(target=devices.start_new_sub, args=(
        back_port, stock))
    p.start()



def main():
    start_broker(8008, 8808)
    for i in range(0,9):
        start_server(8008, 'BRL', 100%(i+60))
        start_server(8008, 'EUR', 100%(i+30))

    start_sub(8808, 'BRL')
    start_sub(8808, 'EUR')


if __name__ == '__main__':
    main()