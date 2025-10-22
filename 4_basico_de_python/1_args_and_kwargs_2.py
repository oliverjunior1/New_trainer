import pandas as pd
#Do args with arithmetics operations

def sum_args(*args):
    x=pd.Series(args)
    return print(x.sum())

sum_args(500,300,-200)

