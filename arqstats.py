import pandas as pd 

# this class implements breadth first search algorithm
class arqstats:

    # constructor
    def __init__(self, data):
    
        # change df to numpy
        if isinstance(data, pd.DataFrame):
            self.data_np = data.to_numpy()
                       
    def get_data(self):
        return self.data_np


         

