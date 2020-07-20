"""
chat_client
autor:李炜
time:2020-7-14
"""

from socket import *
from multiprocessing import Process


HOST = "127.0.0.1"
PORT = 8888
ADDR = (HOST,PORT)


#发送消息
def send_msg(sock,name):
    #1.确定消息内容格式
    #2.将消息内容循环的发送给服务端
    while True:
        msg =input("我:")
        data = ("C %s: %s"%(name,msg))
        sock.sendto(data.encode(),ADDR)

#接受消息
def recv_msg(sock):
    #1.循环接收消息内容,并打印
    while True:
        data,addr = sock.recvfrom(1024)
        print(data.encode())



def login(sock):
    """
    进入聊天室
    :param sock:建立连接
    :return:
    """
    while True:
        name = input("name:")
        msg = "L "+name  #建立通信协议
        sock.sendto(msg.encode(), ADDR)
        result,addr = sock.recvfrom(2048)
        if result.decode() =='ok':
            print("您以成功登录聊天室")
        elif result.decode() =='full':
            print("您的名字太受欢迎了,换一个吧!")
            return

#启动函数
def main():
    # 建立udp 套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    login(sock)#进入聊天室
    p =Process(target=recv_msg,args=(sock,))
    p.daemon = True
    p.start()
    send_msg(sock,name)





if __name__ == '__main__':
    main()