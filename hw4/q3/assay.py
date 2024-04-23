import csv

def read_csvs(files):
    neg_data = []
    pos_data = []
    field_data = []
    for file in files:
        with open(file, 'r') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                # Assuming each file contains only one column of data
                if file == files[0]:
                    neg_data.append(float(row[0]))  # Assuming first column contains negative data
                elif file == files[1]:
                    pos_data.append(float(row[0]))  # Assuming first column contains positive data
                elif file == files[2]:
                    field_data.append(float(row[0]))  # Assuming first column contains field data
    return neg_data, pos_data, field_data

def get_sp(c, neg_data):
    ##specificy (sp) = TN/TN + FP
    t_neg = 0
    f_pos = 0
    for data in neg_data:
        if c > data:
            f_pos += 1
        else:
            t_neg += 1
    sp = t_neg/(f_pos + t_neg)
    return sp


def get_se(c, pos_data):
     ##sensitivity (se) = TP/TP+FN
    t_pos = 0
    f_neg = 0
    for data in pos_data:
        if c > data:
            t_pos += 1
        else:
            f_neg += 1
    se = t_pos/(t_pos + f_neg)
    return se

def get_phi_hat(c, field_data):
    # Raw prevalence in the field data for a given cutoff c
    n_pos = 0
    n = len(field_data)
    for data in field_data:
        if data > c:
            n_pos += 1
        else:
            continue
    phi_hat = n_pos / n
    return phi_hat

# def get_theta_hat(se, sp, phi_hat):
#     # Corrected prevalence in the field data for a given cutoff c
#     if (se + sp - 1) == 0:
#         return None
#     else:
#         theta_hat = (phi_hat - (1 - sp))/(se + sp -1)
#         return theta_hat
def get_theta_hat(se, sp, phi_hat):
    # Corrected prevalence in the field data for a given cutoff c
    if (se + sp - 1) == 0:
        return None
    else:
        theta_hat = max(0, (phi_hat - (1 - sp)) / (se + sp - 1))
        return theta_hat

def get_youden_j_c(se_c, sp_c):
    J_c = se_c + sp_c - 1
    return J_c