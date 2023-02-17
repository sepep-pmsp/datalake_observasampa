
from core.utils.file_path import solve_dir, solve_path, check_dir_exists, list_files_recursive, delete_existing_files
from core.utils.io import download_binary_file, unzip_file


class ShpDownloader:
    
    
    domain = 'http://download.geosampa.prefeitura.sp.gov.br/PaginasPublicas/'

    def get_file_uri(self, fname:str)->str:

        uri = f'downloadArquivo.aspx?orig=DownloadCamadas&arq={fname}&arqTipo=Shapefile'

        return self.domain + uri
    
    def download_shp_zip(self, fname:str, zip_folder:str)->str:

        uri = self.get_file_uri(fname)
        fname = solve_path(f'{fname}.zip', parent=zip_folder)

        download_binary_file(uri, fname)

        return fname
    
    
    def unzip_shp(self, fname:str, zip_folder:str, shp_folder:str)->None:

        if fname.endswith('.zip'):
            fname = fname[:-4]
        fname = solve_path(f'{fname}.zip', parent=zip_folder)

        unzip_file(fname, shp_folder)


    def check_shp_exists(self, shp_folder:str)->bool:
        
        checagem = check_dir_exists(shp_folder)
        if checagem:
            shp = list_files_recursive(shp_folder, '.shp')
            if shp:
                return True
        return False

    def pipe_download_shp(self, fname:str, shp_folder:str, zip_folder:str, check=True)->None:

        if check:
            checagem = self.check_shp_exists(shp_folder)
            if checagem:
                print(f'Shape {shp_folder} já salvo')
                return shp_folder

        zip_path = self.download_shp_zip(fname, zip_folder)

        self.unzip_shp(zip_path, zip_folder, shp_folder)

    
    def __call__(self, fname:str, shp_folder:str, zip_folder:str, check_already_exists=True)->None:

        self.pipe_download_shp(fname, shp_folder, zip_folder, check_already_exists)