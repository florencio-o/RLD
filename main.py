import random

from docx import Document
from docx.shared import Inches

from csv import DictReader

document = Document()

document.add_heading('Generic Test Title', 0)

document.add_paragraph('Generic description for said test ')

i = 1

with open('test.csv', 'r') as read_obj:
		csv_dict_reader = DictReader(read_obj)
		for row in csv_dict_reader:

			document.add_heading(f"{i}. {row['Question']}", level=1)

			print(f"Working on question {i}..")

			answers = list([row['Correct'], row['Distractor1'], row['Distractor2'], row['Distractor3']])

			random.seed()
			random.shuffle(answers)

			document.add_paragraph(f"A. {answers[0]}", style='List')
			document.add_paragraph(f"B. {answers[1]}", style='List')
			document.add_paragraph(f"C. {answers[2]}", style='List')
			document.add_paragraph(f"D. {answers[3]}", style='List')
			print(f"Question {i} is complete!")
			i = i + 1


section = document.sections[0]
 
footer = section.footer

footer_para = footer.paragraphs[0]
 
footer_para.text = "\tGenerated with love by Florencio"

document.save('demo.docx')

print("Document is now complete! It should be named as 'demo.docx'")