
from core.utils.file_path import solve_path, solve_dir

DATA_FOLDER = solve_dir('data')

TIERS = {
    #raw data
    'bronze' : solve_path('bronze', DATA_FOLDER),
    #cleaned microdata
    'silver' : solve_path('silver', DATA_FOLDER),
    #variable data in ObservaSampa schema
    'gold' : solve_path('gold', DATA_FOLDER)
}