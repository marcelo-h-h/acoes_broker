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


def main():
    start_broker(8008, 8808)
    start_server(8008, 'BRL', 40.00)


if __name__ == '__main__':
    main()