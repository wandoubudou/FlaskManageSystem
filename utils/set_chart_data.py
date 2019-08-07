total_data = {
    'labels' : ["Mar 1", "Mar 2", "Mar 3", "Mar 4", "Mar 5", "Mar 6", "Mar 7", "Mar 8", "Mar 9", "Mar 10", "Mar 11", "Mar 12", "Mar 13"],
    'data' : [10001, 30162, 26263, 18394, 18287, 28682, 31274, 33259, 25849, 24159, 32651, 31984, 38451],
    'bar_labels' : ["January", "February", "March", "April", "May", "June"],
    'bar_data':[4215, 5312, 6251, 7841, 9821, 14984],
    'pie_labels' :  ["NewYork", "Beijing", "ShangHai", "Paris"],
    'pie_color' : ['#007bff', '#dc3545', '#ffc107', '#28a745'],
    'pie_data' : [12.21, 15.58, 11.25, 8.32],
}

def set_data(change=False):
    """
    input: chnage 为True ，修改。False， 不修改使用默认数据
    自定义图表，修改数据
    默认返回total_data
    只有在按下q的时候 退出设置data，才可以返回total_data,否则一直处于设置data的状态
    :return: dict type 包含图标的所有信息
    """
    if change==True:
        print('tips : keys---> labels   data   bar_labels   bar_data   pie_labels   pie_colors   pie_data')
        key = input("input the key you want to change . (q for quit)\n")
        if key=='q':
            return total_data
        else:
            if key in total_data:
                value = input("want to change to what ? \n").split()
                total_data[key] = value
                set_data()
            else:
                print("wrong key... please check it out ... \n")
                set_data()
    else:
        return total_data
set_data()