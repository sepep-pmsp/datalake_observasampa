from core.utils.file_path import solve_path, solve_dir, extract_extension, list_files_recursive
import pandas as pd
from pandas import DataFrame
from typing import Callable, List, Generator


from config import DATA_FOLDER

class DfLoaderGenerator:
    
    accepted_extensions = {'.csv', '.xls', '.xlsx'}
    
    def __init__(self,tier:str='bronze', data_dir:str=DATA_FOLDER, add_file=False, **parser_params):
        
        self.tier_folder = self.solve_tier_folder(tier, data_dir)
        self.parser_params = parser_params
        self.add_file=add_file
    
    def solve_tier_folder(self, tier:str, data_dir:str)->str:
        
        return solve_dir(solve_path(tier, parent=data_dir))
    
    def solve_folder(self, tier_folder:str, folder:str)->str:

        return solve_path(folder, parent=tier_folder)
    
    def get_files(self, extension:str, folder:str=None)->list:

        folder = folder or self.folder
        files = list_files_recursive(folder, extension)

        return files

    def solve_params(self, parser_params:dict=None)->dict:

        return parser_params or self.parser_params
    
    def solve_add_file(self, df:DataFrame, file:str)->None:

        if self.add_file:
            df['file'] = file

    def open_csv(self, file:str, parser_params:dict=None)->DataFrame:

        parser_params = self.solve_params(parser_params)

        df = pd.read_csv(file, **parser_params)
        self.solve_add_file(df, file)

        return df

    def open_xl(self, file:str, parser_params:dict=None)->DataFrame:

        parser_params = self.solve_params(parser_params)

        df = pd.read_excel(file, **parser_params)
        self.solve_add_file(df, file)

        return df
    
    def solve_open_func(self, extension:str)->Callable:

        if extension not in self.accepted_extensions:
            raise NotImplementedError(f'Extension {extension} not supported.'
                                      f'Only {self.accepted_extensions} accepted')
        
        if extension in {'.xls', '.xlsx'}:

            return self.open_xl
        elif extension == '.csv':

            return self.open_csv
        else:
            raise NotImplementedError(f'Extension {extension} not supported.'
                                      f'Only {self.accepted_extensions} accepted')
        

    def open_file(self, file_path:str, parser_params:dict=None)->DataFrame:

        extension = extract_extension(file_path)
        open_func = self.solve_open_func(extension)

        return open_func(file_path, parser_params)
    
    def open_files(self, file_list:List[str],parser_params:dict=None)->Generator[DataFrame, DataFrame, DataFrame]:

        for file in file_list:
            df = self.open_file(file, parser_params)
            yield df

    def pipeline_open_files(self, folder:str, extension:str, parser_params:dict=None)->Generator[DataFrame, DataFrame, DataFrame]:

        folder = self.solve_folder(self.tier_folder, folder)
        files = self.get_files(extension, folder)

        return self.open_files(files, parser_params)
    
    def __call__(self, folder:str, extension:str, **parser_params)->Generator[DataFrame, DataFrame, DataFrame]:

        return self.pipeline_open_files(folder, extension, parser_params)
        
        
        
    
        


    


    
    
