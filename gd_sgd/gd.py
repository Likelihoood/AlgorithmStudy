import random

def load(filename='l.data'):
    sample_list = []
    y_list = []
    y_aver = 0
    for line in open(filename):
        c_list = line.strip().split('\t')
        x1 = float(c_list[0])
        y = float(c_list[1])
        x0 = 1
        sample_list.append((x0,x1))
        y_list.append(y)
        y_aver += y
    print len(y_list), y_aver / len(y_list)
    return sample_list, y_list

def cal_inner(sample, theta_list):
    size = len(sample)
    inner = 0
    for i in range(size):
        inner = inner + sample[i] * theta_list[i]
    return inner

def sgd(sample_list, y_list,theta_list,alpha):
    local_sample_list = sample_list[0:]

    size = len(local_sample_list)
    theta_size = len(theta_list)
    #while size > 0:
    #    i = random.randint(0,size-1)
    for i in range(size):
        sample = local_sample_list[i]
        inner = cal_inner(sample, theta_list)
        y = y_list[i]
        for index in range(theta_size):
            theta = theta_list[index] + alpha * (y-inner) * sample[index]
            theta_list[index] = theta
        #size = len(local_sample_list)
    return theta_list
    

def cal_gd(sample_list, x_index, y_list,theta_list):
    gd = 0
    size = len(sample_list)
    gd = 0
    for i in range(size):
        sample = sample_list[i]
        inner = cal_inner(sample, theta_list)
        y = y_list[i]
        gd = gd + (y - inner) * sample[x_index]
    return gd/size


def gd(sample_list, y_list,theta_list):
    size = len(theta_list)
    gd_list = []
    for index in range(size):
        gd = cal_gd(sample_list, index, y_list, theta_list)
        gd_list.append(gd)
    return gd_list

def gd_loop(sample_list, y_list, theta_list, iter_num,alpha):
    for i in range(iter_num):
        gd_list = gd(sample_list, y_list, theta_list)
        
        size = len(gd_list)
        for index in range(size):
            theta_list[index]  = theta_list[index]  + alpha * gd_list[index]
        cost = cal_cost_function(sample_list, theta_list, y_list)
        print i, theta_list,cost

def sgd_loop(sample_list, y_list, theta_list, iter_num, alpha):
    for i in range(iter_num):
        theta_list = sgd(sample_list, y_list,theta_list,alpha)
        cost = cal_cost_function(sample_list, theta_list, y_list)
        print i, theta_list, cost

def cal_cost_function(sample_list, theta_list, y_list):
    size = len(sample_list)
    cost = 0
    for  i in range(size):
        sample = sample_list[i]
        inner = cal_inner(sample, theta_list)
        y = y_list[i]
        cost += (y-inner)**2
    return cost/2


if __name__ == '__main__':
    sample_list, y_list = load()
    theta_list = [0,0]
    alpha = 0.01
    iter_num = 100

    sgd_loop(sample_list, y_list, theta_list, iter_num,alpha)

