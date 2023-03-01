from core.utils.file_path import solve_path, solve_dir
from pandas import DataFrame
from typing import Callable


from config import DATA_FOLDER

class DfSaver:
    
    
    save_types = {'csv', 'excel'}

    def __init__(self, folder:str, tier:str='bronze', data_dir:str=DATA_FOLDER):
        
        self.tier = self.solve_tier_folder(tier, data_dir)
        self.folder = solve_path(folder, parent = self.tier)
        
    def solve_tier_folder(self, tier:str, data_dir:str)->str:
        
        return solve_dir(solve_path(tier, parent=data_dir))

    def solve_fpath(self, fpath:str)->str:

        return solve_path(fpath, self.folder)
    
    def set_extension(self, fname:str, extension:str)->str:

        if not extension.startswith('.'):
            extension = '.' + extension

        return  fname + extension

    def save_csv(self, df:DataFrame, fname:str, **save_params)->str:

        fname = self.set_extension(fname, '.csv')
        fpath = self.solve_fpath(fname)

        df.to_csv(fpath, **save_params)

        return fpath

    def save_excel(self, df:DataFrame, fname:str, **save_params)->str:

        fname = self.set_extension(fname, '.xlsx')
        fpath = self.solve_fpath(fname)

        df.to_excel(fpath, **save_params)

        return fpath

    def check_save_type(self, save_type:str)->None:

        if save_type not in self.save_types:
            raise NotImplementedError(f'Save type {save_type} not available. Available are: {self.save_types}')

    def save(self, df:DataFrame, fname:str, how:str, **save_params)->None:

        if how == 'csv':
            return self.save_csv(df, fname, **save_params)

        elif how == 'excel':
            return self.save_excel(df, fname, **save_params)

        else:
            raise NotImplementedError(f'Save type {how} not available. Available are: {self.save_types}')

    def __call__(self, df:DataFrame, fname:str, how:str, **save_params):

        return self.save(df, fname, how, **save_params)