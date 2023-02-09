import sys
while True:
    print('type exit to terminate.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('you type: ' + response + '.')
    