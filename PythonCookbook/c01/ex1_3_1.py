from collections import deque

def search(lines, pattern, history=5):
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)

# Example use on a file
if __name__ == '_main__':
    with open('somefile.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)