GR_Alphabet =   {'Α': 1, 'Β': 2, 'Γ': 3, 'Δ': 4, 'Ε': 5, 'Ζ': 6, 'Η': 7, 'Θ': 8, 'Ι': 9, 'Κ': 10, 'Λ': 11, 'Μ': 12, 'Ν': 13, 'Ξ': 14, 'Ο': 15, 'Π': 16, 'Ρ': 17, 'Σ': 18, 'Τ': 19, 'Υ': 20, 'Φ': 21, 'Χ': 22, 'Ψ': 23, 'Ω': 24,
                 0:'Ω', 1: 'Α', 2: 'Β', 3: 'Γ', 4: 'Δ', 5: 'Ε', 6: 'Ζ', 7: 'Η', 8: 'Θ', 9: 'Ι', 10: 'Κ', 11: 'Λ', 12: 'Μ', 13: 'Ν', 14: 'Ξ', 15: 'Ο', 16: 'Π', 17: 'Ρ', 18: 'Σ', 19: 'Τ', 20: 'Υ', 21: 'Φ', 22: 'Χ', 23: 'Ψ', 24: 'Ω',
                 'α': 1, 'β': 2, 'γ': 3, 'δ': 4, 'ε': 5, 'ζ': 6, 'η': 7, 'θ': 8, 'ι': 9, 'κ': 10, 'λ': 11, 'μ': 12, 'ν': 13, 'ξ': 14, 'ο': 15, 'π': 16, 'ρ': 17, 'σ': 18, 'τ': 19, 'υ': 20, 'φ': 21, 'χ': 22, 'ψ': 23, 'ω': 24
                 }
key = ''
def convert(text,key,allow_spaces=True):
    OUT= []
    if len(text)==0 or len(key)==0 or ' ' in key:
        return 'ERROR'
    j = 0
    for i in range(len(text)):
        if text[i] not in GR_Alphabet:
            if not allow_spaces:
                OUT.append(' ')
            continue
        OUT.append(GR_Alphabet [ ((GR_Alphabet[(text[i])] + GR_Alphabet[(key[j])]))   % 24 ])
        j= (j+1)%(len(key))   
    OUT = ''.join(OUT)
    return OUT


def deconvert(text,key,allow_spaces=True):
    OUT= []
    if len(text)==0 or len(key)==0 or ' ' in key:
        return 'ERROR'
    j = 0
    for i in range(len(text)):
        if text[i] not in GR_Alphabet:
            if not allow_spaces:
                OUT.append(' ')
            continue
        OUT.append(GR_Alphabet [ ((GR_Alphabet[(text[i])] - GR_Alphabet[(key[j])]))   % 24 ])

        z = GR_Alphabet [ ((GR_Alphabet[(text[i])] + GR_Alphabet[(key[j])]))   % 24 ]
        j= (j+1)%(len(key))   
    OUT = ''.join(OUT)
    return OUT


import PySimpleGUI as sg
fin = None
diadromi = None
GB_SIZE = None
sg.SetOptions(font=100)
#sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
menu_def = [['Αρχείο', ['Άνοιγμα...', 'Αποθήκευση','Αποθήκευση ως...','---','Έξοδος',]],
                ['Βοήθεια', 'Πληροφορίες για το πρόγραμμα'],]
layout = [[sg.Menu(menu_def)],
            [sg.Text('Αρχικό Κείμενο',font=GB_SIZE)],
            [sg.Output(key='_input_',font=GB_SIZE,size=(80,10))],
            
            [sg.Text('Τελικο Κείμενο',font=GB_SIZE)],
            [sg.Output(key = '_output_',font=GB_SIZE,size=(80,10))],
            
            [sg.Checkbox('Χωρις Κενα ',font =GB_SIZE,key='_chkbox_allowspaces_')],
            
            [sg.Button('Κρυπτογραφηση',font=GB_SIZE),sg.Button('Αποκρυπτογραφηση',font=GB_SIZE),sg.Button('Αλλαγη Κλειδιου',font=GB_SIZE), sg.Button('Έξοδος',font=GB_SIZE)]]

# Create the Window
#sg.theme('LightGrey3')

window = sg.Window('Κρυπτογραφηση', layout,)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    #print (event,values)
    if event in (None, 'Έξοδος'):   # if user closes window or clicks cancel
        break
    elif event in (None, 'Αλλαγη Κλειδιου'):
        key = sg.PopupGetText('Αλλαγη Κλειδιου', 'Κλειδη Κρυπτογραφησης',font=GB_SIZE,keep_on_top=True,default_text=key)
        #sg.Popup(key) 
        
        #y = window.FindElement('_output_').Get()
        #window.FindElement('_output_').Update('out='+y)
    elif event in (None, 'Κρυπτογραφηση'):
        if key is None or key=='' or key=='None':
            sg.PopupError('Το κλειδί δεν μπορεί να είναι κενό',title='Σφαλμα')
        else:
            out = convert(window.FindElement('_input_').Get(),key, allow_spaces=window.FindElement('_chkbox_allowspaces_').Get())
            window.FindElement('_output_').Update(out)
    elif event in (None, 'Αποκρυπτογραφηση'):
        if key is None or key=='' or key=='None':
            sg.PopupError('Το κλειδί δεν μπορεί να είναι κενό',title='Σφαλμα')
        else:
            out = deconvert(window.FindElement('_input_').Get(),key, allow_spaces=window.FindElement('_chkbox_allowspaces_').Get())
            window.FindElement('_output_').Update(out)

            
    elif event in (None,'Άνοιγμα...'):
        diadromi = sg.PopupGetFile('Αποθήκευση...',no_window=True,file_types=(('Text Files', '*.txt*'),))
        if diadromi != '':
            fin =open( diadromi,'r',encoding='utf-8')
            window.FindElement('_input_').Update(fin.read())
            fin.close()
        
    elif event in (None,'Αποθήκευση'):
        if diadromi is None or diadromi =='':
            diadromi = sg.PopupGetFile('Αποθήκευση...',no_window=True,save_as=True,file_types=(('Text Files', '*.txt*'),))
        if diadromi !='':
            fin = open(diadromi,'w',encoding='utf-8')
            fin.write(window.FindElement('_output_').Get())
            fin.close()
    elif event in (None,'Αποθήκευση ως...'):
        diadromi = sg.PopupGetFile('Αποθήκευση...',no_window=True,file_types=(('Text Files', '*.txt*'),))
        if diadromi !='':
            fin = open(diadromi,'w',encoding='utf-8')
            fin.write(window.FindElement('_output_').Get())
            fin.close()


window.close()


