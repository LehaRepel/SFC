
from tkinter import *
from tkinter.ttk import Combobox
import yaml
a=1


def create1(a):
    if a == 1:
        print(1)
        runinfo_template = {'Script': Script.get(), 'Read1': Read1.get(), 'Read2': Read2.get(),
                            'Indexes': Indexes.get(), 'TailsCount': TailsCount.get()}
        #samples_template = {'Sample1': Script.get(), 'Read1:': Read1.get(), 'Read2': Read2.get(),
        #                    'Indexes': Indexes.get(), 'TailsCount': TailsCount.get()}
        chemestry_template = {'ChemistryName': ChemistryName.get(), 'Assay': Assay.get(),
                              'IndexAdapters': IndexAdapters.get(),'Adapter1': Adapter1.get(),'Adapter2': Adapter2.get()}
        library_template = {'LPWorkflow': LPWorkflow.get(), 'Chemistry': chemestry_template}
        header_template = {'FileVersion': 5, 'ExperimentName': ExperimentName.get(), 'Date': Date.get(),
                            'Workflow': Workflow.get(), 'InstrumentType': InstrumentType.get(),
                           'Comment': Comment.get()}
        to_yaml = {'Header': header_template,'LibraryPreparation': library_template,
                   'RunInfo': runinfo_template}
        with open('sw_templates.yaml', 'w') as f:
           yaml.dump(to_yaml, f)

if __name__ == '__main__':
    window = Tk()
    window.title('Sample Sheet Creator')
    window.geometry('1000x400')
    window['bg'] = 'grey'
    window.resizable(False, False)
    l0 = Label(bg='red', fg='white', width=20, text='Header').grid(row=0)
    l1 = Label(bg='black', fg='white', width=20, text='Experiment Name:').grid(row=1)
    ExperimentName = Entry(width=20)
    ExperimentName.grid(row=2)
    l2 = Label(bg='black', fg='white', width=20, text='Date:').grid(row=3)
    Date = Entry(width=20)
    Date.grid(row=4)
    l3 = Label(bg='black', fg='white', width=20, text='Workflow:').grid(row=5)
    Workflow = Combobox(window, values='GenerateFASTQ')
    Workflow.grid(row=6)
    l4 = Label(bg='black', fg='white', width=20, text='Instrument type:').grid(row=7)
    InstrumentType = Combobox(window, values='NanoforSPS')
    InstrumentType.grid(row=8)
    l5 = Label(bg='black', fg='white', width=20, text='Comment:').grid(row=9)
    Comment = Entry(width=40)
    Comment.grid(row=10)
    l02 = Label(bg='red', fg='white', width=20, text='Library Preparation:').grid(row=0, column=2)
    l12 = Label(bg='black', fg='white', width=20, text='LPWorkflow:').grid(row=1, column=2)
    LPWorkflow = Entry(width=20)
    LPWorkflow.grid(row=2, column=2)
    l22 = Label(bg='black', fg='white', width=20, text='ChemistryName:').grid(row=3, column=2)
    ChemistryName = Entry(width=20)
    ChemistryName.grid(row=4, column=2)
    l32 = Label(bg='black', fg='white', width=20, text='Assay:').grid(row=5, column=2)
    Assay = Entry(width=20)
    Assay.grid(row=6, column=2)
    l42 = Label(bg='black', fg='white', width=20, text='Library Workflow:').grid(row=7, column=2)
    LibraryPrepWorkflow = Combobox(window, width=30, values=
    ['AmpliSeq Library PLUS for illumina'])
    LibraryPrepWorkflow.grid(row=8, column=2)
    l52 = Label(bg='black', fg='white', width=20, text='IndexAdapters:').grid(row=9, column=2)
    IndexAdapters = Combobox(window, width=30, values=
    ['AmpliSeq CD Indexes (384)', 'AmpliSeq CD Indexes Plate A', 'AmpliSeq CD Indexes Plate B',
     'AmpliSeq CD Indexes Plate C', 'AmpliSeq CD Indexes Plate D'])
    IndexAdapters.grid(row=10, column=2)
    IndexAdapters.current(0)
    l62 = Label(bg='black', fg='white', width=20, text='Adapter1:').grid(row=11, column=2)
    Adapter1 = Entry(width=20)
    Adapter1.grid(row=12, column=2)
    l72 = Label(bg='black', fg='white', width=20, text='Adapter2:').grid(row=13, column=2)
    Adapter2 = Entry(width=20)
    Adapter2.grid(row=14, column=2)
    l03 = Label(bg='red', fg='white', width=20, text='RunInfo:').grid(row=0, column=3)
    l23 = Label(bg='black', fg='white', width=20, text='Script:').grid(row=1, column=3)
    Script = Combobox(window, values='workfile.py')
    Script.grid(row=2, column=3)
    l33 = Label(bg='black', fg='white', width=20, text='Read1:').grid(row=3, column=3)
    Read1 = Entry(width=20)
    Read1.grid(row=4, column=3)
    l43 = Label(bg='black', fg='white', width=20, text='Read2:').grid(row=5, column=3)
    Read2 = Entry(width=20)
    Read2.grid(row=6, column=3)
    l53 = Label(bg='black', fg='white', width=20, text='Indexes:').grid(row=7, column=3)
    Indexes = Combobox(window, values=['none', 'single', 'dual'])
    Indexes.grid(row=8, column=3)
    l63 = Label(bg='black', fg='white', width=20, text='TailsCount:').grid(row=9, column=3)
    TailsCount = Entry(width=20)
    TailsCount.grid(row=10, column=3)
    l73 = Label(bg='black', fg='white', width=20, text='SurfaceCount:').grid(row=11, column=3)
    SurfaceCount = Entry(width=20)
    SurfaceCount.grid(row=12, column=3)
    l83 = Label(bg='black', fg='white', width=20, text='DeviceSettings:').grid(row=13, column=3)
    DeviceSettings = Combobox(window, values=['default']).grid(row=14, column=3)
    Create_Button = Button(window,
                           width=80,
                           text='Create',
                           bg='green',
                           fg='white',
                           command=lambda: create1(a))
    Create_Button.grid(row=20, column=2)
    window.mainloop()

