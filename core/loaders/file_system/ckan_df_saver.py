from core.utils.file_path import solve_path, solve_dir
from pandas import DataFrame
from typing import Callable

class CkanDfSaver:
    
    
    def __init__(self, pkg:str, tier:str='bronze', data_dir:str='data'):
        
        self.tier = self.solve_tier_folder(tier, data_dir)
        self.folder = self.solve_folder(pkg)
        
    def solve_folder(self, pkg:str)->str:
        
        return self.clean_name(pkg)
    
    def solve_tier_folder(self, tier:str, data_dir:str)->str:
        
        return solve_dir(solve_path(tier, parent=data_dir))
        
    def clean_name(self, name:str)->str:
        
        name = name.lower()
        name = name.replace(' ', '_').replace('-', '_')
        name = name.replace('__', '_')
        
        return name
        
    def extract_name(self, metadata:dict)->str:
        
        name = metadata['name']
        return self.clean_name(name)
    
    def extract_extension(self, metadata:dict)->str:
        
        format_ = metadata['format']
        format_ = format_.lower().strip()
        format_ = '.' + format_
        
        return format_
    
    def solve_parent_folder(self):
        
        return solve_path(self.folder, parent=self.tier)
        
    
    def add_folder(self, filename:str)->str:
        
        parent = self.solve_parent_folder()
        return solve_path(filename, parent=parent)
    
    
    def gen_file_path(self, metadata:dict)->str:
        
        name = self.extract_name(metadata)
        extension = self.extract_extension(metadata)
        filename = name + extension
        full_path = self.add_folder(filename)
        
        return full_path
    
    def save_csv(self, metadata:dict, df:DataFrame)->str:
        
        fname = self.gen_file_path(metadata)
        try:
            df.to_csv(fname, sep=';',encoding='utf-8')
        except UnicodeEncodeError:
            df.to_csv(fname, sep=';', encoding='latin-1')
        
        return fname
    
    def save_excel(self, metadata:dict, df:DataFrame)->str:
        
        fname = self.gen_file_path(metadata)
        df.to_excel(fname)
        
        return fname
    
    def solve_save(self, metadata:dict)->Callable:
        
        extension = self.extract_extension(metadata)
        
        if extension == '.csv':
            return self.save_csv
        elif extension in {'.xls', '.xlsx'}:
            return self.save_excel
        else:
            raise NotImplementedError(f"Extension {extension} not supported")
    
    def pipeline_save(self, metadata:dict, df:DataFrame)->str:
        
        fname = self.gen_file_path(metadata)
        save_func = self.solve_save(metadata)
        
        return save_func(metadata, df)
    
    def __call__(self, metadata:dict, df:DataFrame)->str:
        
        return self.pipeline_save(metadata, df)