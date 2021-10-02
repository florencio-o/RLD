import random

from docx import Document
from docx.shared import Inches

from csv import DictReader

document = Document()

# sets document title
document.add_heading('Generic Test Title', 0)

# sets paragraph under title
document.add_paragraph('Generic description for said test ')

# set current question number to one
i = 1

# opens test.csv as read_obj
with open('test.csv', 'r') as read_obj:
		csv_dict_reader = DictReader(read_obj)

		# begins to read each row
		for row in csv_dict_reader:

			# adds heading, which is the question
			document.add_heading(f"{i}. {row['Question']}", level=1)

			# lets the user know what question its working on
			print(f"Working on question {i}..")

			# add all the questions into a list
			answers = list([row['Correct'], row['Distractor1'], row['Distractor2'], row['Distractor3']])

			# shuffles questions in list
			random.seed()
			random.shuffle(answers)

			# adds each answer as a paragraph
			document.add_paragraph(f"A. {answers[0]}", style='List')
			document.add_paragraph(f"B. {answers[1]}", style='List')
			document.add_paragraph(f"C. {answers[2]}", style='List')
			document.add_paragraph(f"D. {answers[3]}", style='List')

			# lets the user know that the question has been completed
			print(f"Question {i} is complete!")

			# sets current question number with an additional one
			i = i + 1


section = document.sections[0]
 
# adds footer
footer = section.footer
footer_para = footer.paragraphs[0]
footer_para.text = "\tGenerated with love by Florencio"

# save document
document.save('demo.docx')

# lets the user know that the document is now complete
print("Document is now complete! It should be named as 'demo.docx'")