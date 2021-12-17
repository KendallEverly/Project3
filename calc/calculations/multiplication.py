"""Multiplication Class"""
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """multiplication calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result
# """imports"""
# from calc.calculations.calculation import Calculation
# import pandas as pd
# from datetime import datetime
# import glob
# from os import path
# import shutil
#
#
# class Multiplication(Calculation):
#     dest = "C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\done"
#     files = glob.glob("C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\input\\*.csv")
#     res_df = pd.DataFrame(columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
#     for f in files:
#         filepath = f
#     fn = [path.basename(x) for x in glob.glob(f)]
#     print("Reading", fn)
#     data = pd.read_csv(filepath)
#     results = pd.read_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv')
#     """Loop for running calc on each input row"""
#     nrow = data.shape[0]
#     for x in range(0, nrow):
#         print("Iter: ", x + 1)
#         """extract values"""
#         value_a = data.at[x, 'a']
#         value_b = data.at[x, 'b']
#         """operations"""
#         calc_result = value_a * value_b
#         """initialize list of values"""
#         tmpstp = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#         res_data = [[tmpstp, filepath, x + 1, "Multiply", calc_result]]
#         """Create the pandas DataFrame"""
#         res_iter = pd.DataFrame(res_data, columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
#         """Append to results"""
#         res_df = res_df.append(res_iter)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
#     """Move file from input to done"""
#     shutil.move(f, dest)
#     """Append results to results.csv"""
#     res_out = results.append(res_df)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
#     res_out.to_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv', index=False)
