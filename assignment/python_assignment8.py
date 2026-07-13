class Order:
    def __init__(self, addr):
        self.addr = addr

    def submit_order(self):
        print("提交订单！")

    def create_order(self):
        print(f"下单成功！，收货地址：{self.addr}")

def get_addr():
    address = input("请输入收货地址：")
    return address

if __name__ == "__main__":
    order = Order(get_addr())
    order.create_order()
    order.submit_order()
