from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

from pdf2docx import Converter
import os

def abre_pasta():
	arquivo = pdf_filename.get()
	#arquivo_docx = f"docs\{arquivo}.docx"
	comando = "start docs\\"
	os.system(comando)

def abre_documento():
	arquivo = pdf_filename.get()
	#arquivo = arquivo.replace(" ","_")
	comando = rf"start docs\{arquivo}.docx"
	os.system(comando)

def converte(pdfname, pathfile):
	#pdfname = pdfname.replace(" ","_")
	arquivo_pdf = pathfile # 'Sample.pdf'
	# arquivo_docx = 'Sample.docx'
	arquivo_docx = rf"docs\{pdfname}.docx"
	
	converter = Converter(arquivo_pdf)
	converter.convert(arquivo_docx)
	converter.close()
	abre_pasta()



def converterPDF():
  	
	if (filepath.get() == "" and pdf_filename.get() == ""):
		print("empty input")
		filepath.focus_set()

	else:
			print(pdf_filename.get())
			print(filepath.get())		
   
			pdfname_info = pdf_filename.get()
			filepath_info = filepath.get()
			
			converte(pdfname_info, filepath_info)
		
def getPdfName(path):
	arrPath = path.split('/')
	nome = arrPath[len(arrPath)-1]
	return(nome.split('.')[0])

  
# Main code
if __name__ == "__main__":
    
    # create a GUI window
	root = Tk()

	# set the background colour of GUI window
	root.configure(background='light green')

	# set the title of GUI window
	root.title("CONVERT PDF TO DOCX")

	# set the configuration of GUI window
	root.geometry("560x110")

	#excel()

	# create a Form label
	heading = Label(root, text="Selecione o arquivo PDF", bg="light green")
 
	
	# file label
	filepath_label = Label(root, text="Arquivo", bg="light green")
	
	# create a Contact No. label
	pdf_filename_label = Label(root, text="Change Name", bg="light green")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure .
	heading.grid(row=0, column=1)
	
	filepath_label.grid(row=2, column=0)
	pdf_filename_label.grid(row=3, column=0)
	# create a text entry box
	# for typing the information
 
	filepath = Entry(root)
	# bind method of widget is used for
	# the binding the function with the events 
	filepath.grid(row=2, column=1, ipadx="140")

	pdf_filename = Entry(root)
	pdf_filename.insert(0, 'Mude se quiser o nome do arquivo do Word')
	pdf_filename.grid(row=3, column=1, ipadx="140")
 
	def browsefunc():
		filename = askopenfilename(filetypes=(("pdf file", "*.pdf"), ("All files", "*.*"),))
		filepath.insert(END, filename) # add this
		nomeFile = getPdfName(filename)
		pdf_filename.delete(0, END)
		pdf_filename.insert(0, nomeFile)
		pdf_filename.focus_set()


	b1=Button(root,text="Selecione",fg="Black", bg="Yellow",command=browsefunc)
	b1.grid(row=2, column=2)

	# create a send_email Button and place into the root window
	convert_btn = Button(root, text="Converter", fg="White",
							bg="Blue", command=converterPDF)
	convert_btn.grid(row=3, column=2)
 
 
	abrir_pasta_docsx = Button(root, text="Pasta com Arquivos do Word", fg="White",
							bg="Blue", command=abre_pasta)
	abrir_pasta_docsx.grid(row=4, column=1)

	# start the GUI
	root.mainloop()