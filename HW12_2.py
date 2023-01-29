import asyncio
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 5000))
sock.listen(5)
print('server is up now')


async def summ(a, b):
    print('start sum')
    s = a + b
    await asyncio.sleep(0)
    print('sum result:', s)
    conn.send(bytes(str(f'sum = {s}'), encoding='UTF-8'))


async def div(a, b):
    print('start div')
    d = a / b
    await asyncio.sleep(0)
    print('div result:', d)
    conn.send(bytes(str(f'div = {d}'), encoding='UTF-8'))


async def mult(a, b):
    print('start mult')
    m = a * b
    await asyncio.sleep(0)
    print('mult result:', m)
    conn.send(bytes(str(f'mult = {m}'), encoding='UTF-8'))


while True:
    conn, addr = sock.accept()
    print('client is connected')
    data = []
    for i in range(1, 3):
        num = int((str(conn.recv(1024)).replace("b'", "").replace("'", "")))
        data.append(num)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(summ(data[0], data[1])),
             loop.create_task(div(data[0], data[1])),
             loop.create_task(mult(data[0], data[1]))]
    wait_tasks = asyncio.wait(tasks)
    loop.run_until_complete(wait_tasks)
    loop.close()
    # break
