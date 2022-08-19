import time
from functools import reduce
import keyboard

def start():
    
    temp = time.localtime() # Считывание локального времени, запись его в файл
    mapped = list(map(int, time.strftime('%X', temp).split(':')))
    
    f = open('FlagMaker.txt', 'a+')
    f.write('________________________' + '\n' + time.strftime('%c', temp) + '\n')
    print(time.strftime('%c', temp))
    f.close()
               
    return mapped

def action(startTime): # Фиксирование времени при действии относительно start()
    f = open('FlagMaker.txt', 'a+')

    temp = time.localtime()
    cur_time = list(map(int, time.strftime('%X', temp).split(':')))
    
    #Чую, можно через reduce сделать
    difference = (cur_time[0] - startTime[0])*3600 + (cur_time[1] - startTime[1])*60 + (cur_time[2] - startTime[2])
    diff_struct_time = time.gmtime(difference) #ГМТайм для корректного отображения
    diff_for_human = time.strftime('%X', diff_struct_time) #Удобно для человеков
    
    f.write(diff_for_human + '\n')
    f.close()
    
    print('added ', diff_for_human)

start_time = start()
keyboard.add_hotkey('insert', lambda: action(start_time))
keyboard.wait()

