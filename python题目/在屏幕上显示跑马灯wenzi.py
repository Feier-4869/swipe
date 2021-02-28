import os
import time

def main():
    content = '菲儿老婆，我爱你'
    while True:
        os.system('cls')
        print(content)
        time.sleep(1)
        content = content[1:] + content[0]

# if __name__ == '__main__':
#     main()


