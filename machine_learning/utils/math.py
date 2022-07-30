import numpy as np
def get_regression_parameters(X,y):

    xtx = np.matmul(X.T,X)
    xtx_inverse = np.linalg.inv(xtx)
    xty = np.matmul(X.T,y)
    return np.matmul(xtx_inverse,xty)

def get_sum_given_feature(data,all_features,xaxis_metric,yxis_metric):
    xaxis_index = all_features.index(xaxis_metric)
    yaxis_index = all_features.index(yxis_metric)
    xaxis_values = data[xaxis_index]
    yaxis_values = data[yaxis_index]
    dict_of_sums_temp = {}
    for index,x in enumerate(xaxis_values):
        if str(int(x)) in dict_of_sums_temp.keys():
            existing_list = dict_of_sums_temp[x]
            existing_list.append(yaxis_values[index])
            dict_of_sums_temp[str(int(x))] = existing_list
        else:
            dict_of_sums_temp[str(int(x))] = [yaxis_values[index]]
    dict_of_sums = {}
    for key,list_to_add in dict_of_sums_temp.items():
        dict_of_sums[key] = np.sum(list_to_add)
    return dict_of_sums