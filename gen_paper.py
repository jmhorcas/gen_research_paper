import logging

from smoke_research.gen_folder_structure import gen_folder_structure, gen_latex_section
from smoke_research.gen_introduction import gen_introduction


def main():
    gen_folder_structure()

    content = gen_introduction()
    gen_latex_section(1, 'Introduction', 'introduction', content)

    gen_latex_section(2, 'Background', 'background')
    gen_latex_section(3, 'Content 1', 'content1')
    gen_latex_section(4, 'Content 2', 'content2')
    gen_latex_section(5, 'Content 3', 'content3')
    gen_latex_section(6, 'Evaluation', 'evaluation')
    gen_latex_section(7, 'Related work', 'relatedwork')
    gen_latex_section(8, 'Conclusions and future work', 'conclusions')

    



if __name__ == '__main__':
    logging.basicConfig(filename='gen_paper.log', filemode='w', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')
    main()
