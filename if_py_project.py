import pandas as pd
data = pd.read_csv("emplyee_data.csv")


def eligibility_checker(age):
    if age>=18:
        return"eligible"
    else:
         return"not eligible"
data["eligibility"] = data["age"].apply(eligibility_checker)   
print(data)
data.to_csv("emplyee_data.csv")      