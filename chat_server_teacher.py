"""
chat_server
autor:李炜
time:2020-7-14
"""



from socket import *

HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

#储存用户信息
user={}

def transiter(sock,name,addr):
    #1.首先先取到用户地址
    #2,将这个消息发送给其他人
    #3.抛出本人将信息发送给其他人
    msg = "%s:%s"%(name,addr)
    for i in user:
        if i != name:
            #遍历字典,如果收到的消息不是由本人发起的,就将消息发送给其他人
            sock.sendto(msg.encode(),name[i])



def recv_user(sock,name,addr):
    """
    判断用户是否存在,并回应用需请求
    :param sock: 建立连接
    :param name: 姓名
    :param addr:地址
    :return:
    """
    #user={name:address}
    if name in user: #表示如果这个键在这个用户字典当中
        sock.sendto(b"full",addr)
        return
    else:
        sock.sendto(b"ok",addr)
    user[name] = addr
    print(user)

#建立启动函数
def main():
    #创建udp套接字
    sock = socket(AF_INET,SOCK_DGRAM)
    #绑定地址
    sock.bind(ADDR)
    #循环接手客户端的请求
    while True:
        data,addr =sock.recvfrom(2048)
        tmp = data.decode().split(' ')
        #根据请求调用不同的函数
        #tmp =[L,name]
        if tmp[0] =='L':
            #接受用户名 ,函数参数要(建立连接,姓名,地址)
            recv_user(sock,tmp[1],addr)
        elif tmp[0] =='C':
            #转发给其他用户 [C,name,address]
            transiter(sock,tmp[1],tmp[2])


if __name__ == '__main__':
    main()