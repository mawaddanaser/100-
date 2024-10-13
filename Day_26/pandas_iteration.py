import pandas
student_dic = {"student": ["Angela", "James", "lily"],
               "score": [56, 76, 98]}
student_data_frame = pandas.DataFrame(student_dic)
print(student_data_frame)

# Loop through rows of data_frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    if row.student == "Angela":
        print(row.score)

















# import pandas as pd
#
# # Sample DataFrame
# data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# df = pd.DataFrame(data)
#
# # Iterating over DataFrame rows using iterrows()
# for index, row in df.iterrows():
#     print(f"Index: {index}")
#     print(row)
#     print("------------------")
# ###############

# import pandas as pd
#
# # Sample DataFrame
# data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
# df = pd.DataFrame(data)
#
# # Iterating over DataFrame rows using itertuples()
# for row in df.itertuples():
#     print(row)
