import numpy as np


def get_sum_given_feature(data,all_features,xaxis_metric,yxis_metric):
    x_axis_index = all_features.index(xaxis_metric)
    y_axis_index = all_features.index(yxis_metric)
    x_axis_values = []
    y_axis_values = []
    for d in data:
        x_axis_values.append(str(int(d[x_axis_index])))
        y_axis_values.append(float(d[y_axis_index]))
    dict_of_vals = {}
    for index,xval in enumerate(x_axis_values):
        yval = y_axis_values[index]
        if xval in dict_of_vals:
            exist = dict_of_vals[xval]
            exist.append(float(yval))
            dict_of_vals[xval] = exist
        else:
            dict_of_vals[xval] = [yval]

    dict_of_sums = {}
    for key,list_of_vals in dict_of_vals.items():
        dict_of_sums[key] = np.sum(list_of_vals)

    return dict_of_sums


def sumdict_with_corrected_labelnames(dict_to_correct,correction_map):
    corrected_dict = {}
    for key,value in dict_to_correct.items():
        correct_name = correction_map[key]
        corrected_dict[correct_name] = value
    return corrected_dict