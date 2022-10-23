# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def reduction1(items):
    # 计算满减+优惠券
    total_num = 0
    shangping = 0
    shangping_num = 0
    for num,item in enumerate(items):
        total_num += item['price']
        if item['shangpinquan']>shangping:
            shangping = item['shangpinquan']
            shangping_num = num
    huiyuan = 90
    if total_num <1200:
        huiyuan = 30
    if huiyuan>shangping:
        shangping = 0
        shangping_num = 0
    dianpu = max(huiyuan,shangping)
    manjian = total_num/300*50
    pinlei = 30
    quanhou_price = total_num - dianpu - manjian - pinlei
    return total_num,quanhou_price,(shangping_num,shangping)

def shifu_price(items, total_num, quanhou_price, shangping, vip,gouwujin_zhekou):
    shifu_prices = []
    dingjins = []
    if shangping == (0,0):
        quankou = quanhou_price / total_num
        price = [item['price']*quankou for item in items]
    else:
        quankou = (quanhou_price+shangping[1])/total_num
        price = [item['price']*quankou for item in items]
        price[shangping[0]] -= shangping[1]
    if vip:
        price = [p*0.95 for p in price]
    for num,p in enumerate(price):
        dingjin = items[num]['ding'] * 0.95 if vip else 1.0
        dingjins.append(dingjin)
        p = dingjin + (p - dingjin) * gouwujin_zhekou
        shifu_prices.append(p)
    return shifu_prices,dingjins


def daoshou(items,fukuan_price,dingjins,gouwujin_zhekou):
    miandan = min(fukuan_price)
    shaofan = 0
    for num,item in enumerate(items):
        shao = 0
        if fukuan_price[num] == miandan:
            if item['mianding']:
                shao += dingjins[num]
            if item['hongbao']!= 0:
                shao += item['hongbao']
            if shao>=shaofan:
                shaofan = shao
                miandan_id = num
    weikuan = [fukuan_price[i] - dingjins[i] for i,_ in enumerate(fukuan_price)]
    mianjin = dingjins[miandan_id] + weikuan[miandan_id]*gouwujin_zhekou
    print('免单:',items[miandan_id]['name'],',免单价格:',miandan)
    for num,item in enumerate(items):
        if num == miandan_id:
            continue
        if item['mianding']:
            mianjin += dingjins[num]
        mianjin += item['hongbao']
    return sum(fukuan_price) - mianjin

def gain_list():
    items = []
    list1 = {'name': 'leisi', 'price': 369, 'ding': 40, 'mianding': False, 'hongbao': 20, 'shangpinquan': 0}
    # list1 = {'name': 'tangguo', 'price': 419, 'ding': 50, 'mianding': False, 'hongbao': 10, 'shangpinquan': 0}
    # list1 = {'name': 'huaxin', 'price': 449, 'ding': 50, 'mianding': False, 'hongbao': 0, 'shangpinquan': 0}
    # list1 = {'name': 'bobo', 'price': 439, 'ding': 50, 'mianding': False, 'hongbao': 10, 'shangpinquan': 0}
    list2 = {'name': 'baijin', 'price': 439, 'ding': 50, 'mianding': False, 'hongbao': 20, 'shangpinquan': 0}
    list3 = {'name': 'huwai', 'price': 499, 'ding': 50, 'mianding': False, 'hongbao': 20, 'shangpinquan': 0}
    # list2 = {'name': 'naicha', 'price': 409, 'ding': 50, 'mianding': False, 'hongbao': 0, 'shangpinquan': 0}
    # list1 = {'name': 'zuanshi', 'price': 449, 'ding': 50, 'mianding': True, 'hongbao': 0, 'shangpinquan': 0}
    # list2 = {'name': 'shandian', 'price': 499, 'ding': 50, 'mianding': False, 'hongbao': 20, 'shangpinquan': 0}
    list2 = {'name': 'shandian', 'price': 499, 'ding': 50, 'mianding': False, 'hongbao': 10, 'shangpinquan': 110}
    # list3 = {'name': 'huafu', 'price': 509, 'ding': 60, 'mianding': False, 'hongbao': 0, 'shangpinquan': 110}
    items.append(list1)
    items.append(list2)
    items.append(list3)
    return items

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    items = gain_list()
    final = []
    gouwujin = 1150
    gouwujin_zhekou = 1000/gouwujin
    vip = True
    print('\n购物金:',gouwujin,',88vip:',vip)
    total_num, quanhou_price, (shangping_num, shangping) = reduction1(items)
    pay_in_taobao,dingjins = shifu_price(items,total_num,quanhou_price,(shangping_num,shangping),vip,gouwujin_zhekou)
    pay_real = daoshou(items,pay_in_taobao,dingjins,gouwujin_zhekou)
    final_zhekou = pay_real/total_num
    final_price = [item['price']*final_zhekou for item in items]
    for num,item in enumerate(items):
        print('鞋名:',item['name'],',原价:',item['price'],',到手:',final_price[num])
    # print(final_price)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
