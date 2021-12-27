import os 
import shutil
import logging


LATEX_EXTENSION = 'tex'

MAIN_DIR = 'paper'
SECTIONS_DIR = 'sections'
IMAGES_DIR = 'images'
TABLES_DIR = 'tables'
ALGORITHMS_DIR = 'algorithms'
PLOTS_DIR = 'plots'

FOLDERS = [SECTIONS_DIR, IMAGES_DIR, TABLES_DIR, ALGORITHMS_DIR, PLOTS_DIR]


def _create_directories(path: str) -> None:
    try:
        os.makedirs(path)
    except OSError as e:
        logging.error(f'Creation of directories "{path}" failed. {e}')
    else:
        logging.info(f'Created directories: {path}.')


def gen_folder_structure() -> None:
    if os.path.exists(MAIN_DIR):
        shutil.rmtree(MAIN_DIR)
        
    for folder in FOLDERS:
        dir = os.path.join(MAIN_DIR, folder)
        _create_directories(dir)


def gen_latex_section(id: int, name: str, label: str, content: str = None) -> None:
    filepath = os.path.join(MAIN_DIR, SECTIONS_DIR, f'sec0{id}_{label}.{LATEX_EXTENSION}')
    with open(filepath, mode='w', encoding='utf-8') as file:
        file.write(f'\section{{{name}}}\n')
        file.write(f'\label{{sec:{label}}}\n')

        if content:
            file.write(content)