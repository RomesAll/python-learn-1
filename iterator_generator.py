
def read_file(path: str):
    with open(path, mode='r') as f:
        while True:
            chunk = f.readline()
            if not chunk:
                break
            yield chunk

for data in read_file(r'/home/roman/GitHub/python-learn-1/data.txt'):
    print(data)