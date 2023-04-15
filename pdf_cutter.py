import tkinter as tk
from tkinter import filedialog

import PyPDF2


class PDFSplitterApp:
    def __init__(self, master):
        self.master = master
        master.title('PDF Splitter')

        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()

        input_label = tk.Label(master, text='Input PDF:')
        input_label.grid(row=0, column=0, padx=10, pady=10)
        self.input_entry = tk.Entry(master, textvariable=self.input_path)
        self.input_entry.grid(row=0, column=1, padx=10, pady=10)
        input_button = tk.Button(master, text='Browse', command=self.browse_input)
        input_button.grid(row=0, column=2, padx=10, pady=10)

        output_label = tk.Label(master, text='Output PDF:')
        output_label.grid(row=1, column=0, padx=10, pady=10)
        self.output_entry = tk.Entry(master, textvariable=self.output_path)
        self.output_entry.grid(row=1, column=1, padx=10, pady=10)
        output_button = tk.Button(master, text='Browse', command=self.browse_output)
        output_button.grid(row=1, column=2, padx=10, pady=10)

        split_button = tk.Button(master, text='Split', command=self.split_pdf)
        split_button.grid(row=2, column=1, padx=10, pady=10)

    def browse_input(self):
        filename = filedialog.askopenfilename(title='Select Input PDF', filetypes=[('PDF files', '*.pdf')])
        self.input_path.set(filename)

    def browse_output(self):
        filename = filedialog.asksaveasfilename(title='Select Output PDF', filetypes=[('PDF files', '*.pdf')])
        self.output_path.set(filename)

    def split_pdf(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()

        # Open the PDF file
        input_pdf = PyPDF2.PdfReader(open(input_path, 'rb'))

        # Create a new PDF file for the output
        output_pdf = PyPDF2.PdfWriter()

        # Iterate through each page of the input PDF
        for page_num in range(len(input_pdf.pages)):
            page = input_pdf.pages[page_num]

            # Get the dimensions of the page, it can have been rotated
            if page.mediabox.height < page.mediabox.width:
                # Cut vertically
                page_width = page.mediabox.width

                upper_middle = page.cropbox.upper_right
                upper_middle = (page_width / 2, upper_middle[1])

                lower_middle = page.cropbox.lower_right
                lower_middle = (page_width / 2, lower_middle[1])

                # Create two new pages from the halves
                first_page = output_pdf.add_page(page)
                first_page.cropbox.top_right = upper_middle
                first_page.cropbox.lower_right = lower_middle

                second_page = output_pdf.add_page(page)
                second_page.cropbox.top_left = upper_middle
                second_page.cropbox.lower_left = lower_middle
            else:
                # Cut horizontally
                page_height = page.mediabox.height

                right_middle = page.cropbox.lower_right
                right_middle = (right_middle[0], page_height / 2)

                left_middle = page.cropbox.lower_left
                left_middle = (left_middle[0], page_height / 2)

                # Create two new pages from the halves
                first_page = output_pdf.add_page(page)
                first_page.cropbox.lower_left = left_middle
                first_page.cropbox.lower_right = right_middle

                second_page = output_pdf.add_page(page)
                second_page.cropbox.upper_left = left_middle
                second_page.cropbox.upper_right = right_middle

        # Save the output PDF to a file
        with open(output_path, 'wb') as output_file:
            output_pdf.write(output_file)

        tk.messagebox.showinfo('PDF Splitter', 'PDF split successfully.')


root = tk.Tk()
app = PDFSplitterApp(root)
root.mainloop()
