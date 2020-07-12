from collections import deque
import sys
import os
 
nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing
 
Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)
 
 
Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.
 
Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.
 
'''
 
bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk
 
It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)
 
 
Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters
 
Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''
 
# write your code here
name_folder = sys.argv[1]
if not os.path.exists(name_folder):
    os.mkdir(name_folder)
 
history = deque()
while True:
    url = input()
 
    if '.' in url:
        path = os.path.join(name_folder, '.'.join(url.split('.')[:-1]))
        if 'bloomberg' in url:
            history.append('bloomberg')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(bloomberg_com)
                print(bloomberg_com)
        elif 'nytimes' in url:
            history.append('nytimes')
            with open(path, 'w', encoding='utf-8') as file:
                file.write(nytimes_com)
                print(nytimes_com)
        else:
            print('error')
    else:
        if url == 'exit':
            sys.exit()
        if url == 'back':
            history.pop()
            url = history.pop()
        try:
            path = os.path.join(name_folder, url)
            with open(path, 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print('error')