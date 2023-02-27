from typing import Union
from pandas import DataFrame
from core.extractors.ckan_api_reader import Ckan

class ExtractCsvFrom2006to2016:
    '''Extract data from 2006 to 2016. After 2016 must use other class'''
    
    domain = 'http://dados.prefeitura.sp.gov.br/api/3'
    pkg = 'demanda-e-matriculas'
    earliest_year = 2017
    
    def __init__(self):
        
        self.ckan = Ckan(self.domain)
    
    @property
    def parser_params(self):
        
        return {'sep' : ';'}
        
    def get_resources(self, extract:bool=False)->Union[DataFrame, dict]:
        
        resources = self.ckan(
                    self.pkg,
                    format_=['CSV'],
                    search_string='2006 a 2017',
                    how='contains',
                    attr='name',
                    case_sensitive=True,
                    extract=extract,
                    parser_params = self.parser_params
                )
        
        return next(resources)
        
    
    def __call__(self, extract:bool=False)->Union[DataFrame, dict]:
        
        return self.get_resources(extract)