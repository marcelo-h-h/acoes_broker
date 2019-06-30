import devices
import data.stocks
from multiprocessing import Process



def start_broker(front_port: int, back_port: int):
    p = Process(target=devices.start_new_broker, args=(
        front_port, back_port))
    p.start()

def start_server(front_port: int, stock: str, stock_value: float):
    p = Process(target=devices.start_new_server, args=(
        front_port, stock, stock_value))
    p.start()

def start_sub(back_port: int, stock: str, monitor_port: int):
    p = Process(target=devices.start_new_sub, args=(
        back_port, stock, monitor_port))
    p.start()

def start_monitor(monitor_port: int):
    p = Process(target=devices.start_new_monitor, args=(
        monitor_port,))
    p.start()

def main():
    start_broker(8008, 8808)
    for value in data.stocks.return_stocks():
        start_server(8008, value, data.stocks.return_stocks()[value])
    for value in data.stocks.return_stocks():
        start_sub(8808, value, 8070)
    start_monitor(8070)



if __name__ == '__main__':
    main()