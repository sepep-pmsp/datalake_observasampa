import os

from core.utils.file_path import solve_dir, solve_path
from core.utils.io import save_binary_file, save_text_file, save_json_file
from typing import Union, Callable
from config import TIERS


class SimpleFileSaver:

    tiers = TIERS

    file_types = {
        'text' : {'.csv', '.txt'},
        'json' : {'.json', '.geojson'},
        #all else is binary
        'binary' : {}
    }

    def __init__(self, tier:str='bronze'):

        self.tier = tier

    def extract_extension(self, fpath:str)->str:

        try:
            return os.path.splitext(fpath)[1]
        #if file has no extension, such  as ".bashrc"
        except IndexError:
            return ''

    @property
    def save_func_mapper(self):

        mapper = {
            'txt' : save_text_file,
            'json' : save_json_file,
            'binary' : save_binary_file
        }

        return mapper

    @property
    def type_mapper(self):

        mapper = {
            'txt' : str,
            'json' : dict,
            'binary' : bytes
        }

        return mapper

    def solve_file_type(self, extension:str)->Callable:

        for type_, extensions in self.file_types:
            if extension in extensions:
                return type_
        else:
            return 'binary'

    def solve_save_func(self, file_type:str)->Callable:

        save_func = self.save_func_mapper[file_type]

        return save_func

    def check_content_type(self, content:Union[bytes, str, dict], file_type:str)->None:

        content_type = type(content)

        expected_type = self.type_mapper[file_type]

        if content_type != expected_type:
            raise ValueError(f'To save a file of type {file_type} must pass content of type {expected_type}.'
                             f'{content_type} content was provided')

    @property
    def tier_folder(self, tier:str)->str:

        try:
            return self.tiers[tier]
        except KeyError:
            raise ValueError(f'Tier must be in {self.tiers}')

    def get_full_path(self, tier:str, fpath:str)->str:

        tier_folder = self.tier_folder(tier)

        return solve_path(fpath, parent=tier_folder)


    def save_pipeline(self, fpath:str, content:Union[bytes, str, dict], tier:str)->None:
    
        extension = self.extract_extension(fpath)
        file_type = self.solve_file_type(extension)
        self.check_content_type(content, file_type)
        save_func = self.solve_save_func(file_type)

        full_file_path = self.get_full_path(tier, fpath)

        save_func(full_file_path, content)

        return full_file_path

    def __call__(self, fpath:str, content:Union[bytes, str, dict])->str:

        return self.save_pipeline(fpath, content, self.tier)
