# _*_ coding:utf-8 _*_

from flowstorge import FlowStorge

if __name__ == "__main__":
    pool = []
    for i in range(4):
        p = FlowStorge()
        p.daemon = True
        p.start()
        pool.append(p)
    for pro in pool:
        p.join()
