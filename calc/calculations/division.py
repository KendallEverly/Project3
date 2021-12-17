"""Division Class"""
from calc.calculations.calculation import Division
# import pandas as pd

class Division(Calculation):
    """ calculation division class"""
    def get_result(self):
        """get the division results"""
        quotient = 0.0
        for value in self.values:
            quotient = value + quotient
        return quotient
# """imports"""
# from calc.calculations.calculation import Calculation
# import pandas as pd
# from datetime import datetime
# import glob
# from os import path
# import shutil

#
# class Division(Calculation):
#     dest = "C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\done"
#     files = glob.glob("C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\input\\*.csv")
#     res_df = pd.DataFrame(columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
#     exc_df = pd.DataFrame(columns=['input filename', 'row num'])
#     for f in files:
#         filepath = f
#     fn = [path.basename(x) for x in glob.glob(f)]
#     print("Reading", fn)
#     data = pd.read_csv(filepath)
#     results = pd.read_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv')
#     exc = pd.read_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\exception.csv')
#     """Loop for running calc on each input row"""
#     nrow = data.shape[0]
#     for x in range(0, nrow):
#         print("Iter: ", x + 1)
#         """extract values"""
#         value_a = data.at[x, 'a']
#         value_b = data.at[x, 'b']
#         """operations"""
#         calc_result = value_a / value_b
#         """initialize list of values"""
#         tmpstp = datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
#         res_data = [[tmpstp, filepath, x + 1, "Division", calc_result]]
#         """Create the pandas DataFrame"""
#         res_iter = pd.DataFrame(res_data, columns=['timestamp', 'input filename', 'row num', 'operation', 'result'])
#         """Append to results"""
#         res_df = res_df.append(res_iter)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
#         # try:
#         if (value_b == 0):
#             print("Divide by zero error row:", x + 1)
#             """initialize list of values"""
#             exc_data = [[filepath, x + 1]]
#             """create the pandas dataframe"""
#             exc_iter = pd.DataFrame(exc_data, columns=['input filename', 'row num'])
#             """Append to results"""
#             exc_df = exc_df.append(exc_iter)[['input filename', 'row num']]
#     """Move file from input to done"""
#     shutil.move(f, dest)
#     exc_out = exc.append(exc_df)[['input filename', 'row num']]
#     exc_out.to_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\exception.csv', index=False)
#     """Append results to results.csv"""
#     res_out = results.append(res_df)[['timestamp', 'input filename', 'row num', 'operation', 'result']]
#     res_out.to_csv('C:\\Users\\kenda\\PycharmProjects\\calc2\\datafile\\results.csv', index=False)
#
