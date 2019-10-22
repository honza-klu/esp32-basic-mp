try:
    import usocket as socket
except:
    import socket
import ussl as ssl
import gc
key = open("priv.key", "r").read()

cert = open("cert.txt", "r").read()

CONTENT = b"""\
HTTP/1.0 200 OK


Hello #%d from MicroPython!
I want to make the content larger
bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla
bla bla bla bla bla bla bla bla
"""
CONTENT = CONTENT.replace(b"\n", b"\r\n")

def start(use_stream=True):
    s = socket.socket()

    # Binding to all interfaces - server will be accessible to other hosts!
    ai = socket.getaddrinfo("0.0.0.0", 8443)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to https://<this_host>:8443/")

    counter = 0
    while True:
        res = s.accept()
        client_s = res[0]
        client_addr = res[1]
        print("Client address:", client_addr)
        print("Client socket:", client_s)
        client_o = client_s
        client_s = ssl.wrap_socket(client_s, server_side=True, key=key, cert=cert)
        print(client_s)
        print("Request:")
        if use_stream:
            # Both CPython and MicroPython SSLSocket objects support read() and
            # write() methods.
            # Browsers are prone to terminate SSL connection abruptly if they
            # see unknown certificate, etc. We must continue in such case -
            # next request they issue will likely be more well-behaving and
            # will succeed.
            try:
                req = client_s.readline()
                print(req)
                while True:
                    h = client_s.readline()
                    print(h)
                    if h == b"" or h == b"\r\n":
                        break
                if req:
                    print("sending content")
                    client_s.write(CONTENT % counter)
                    print("sending content: done")
            except Exception as e:
                print("Exception serving request:", e)
        else:
            print("NO STREAM")
            print("sending content")
            print(client_s.recv(4096))
            client_s.send(CONTENT % counter)
            print("sending content: done")
        print("Cleaning memory")
        client_s.close()
        client_o.close()
        client_s=None
        client_o=None
        print("Free mem: %d" % gc.mem_free())
        counter += 1
        print()