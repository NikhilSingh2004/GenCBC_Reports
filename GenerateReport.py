from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from random import uniform

for i in range(0,20):
    pdf_doc = SimpleDocTemplate(f"D:\\Nikhil\\Reports\\Test\\SampleCBC_{i}.pdf", pagesize=letter) # Set your own path 

    wbc = str(round(uniform(2.0,13.0),2))
    flag_wbc = " "
    if(float(wbc)<4.0):
        flag_wbc = "L"    
    elif(float(wbc)>11.0):
        flag_wbc = "H"

    rbc = str(round(uniform(1.40,8.0),2))
    flag_rbc = " "
    if(float(rbc)<4.40):
        flag_rbc = "L"    
    elif(float(rbc)>6.0):
        flag_rbc = "H"

    hemo = str(round(uniform(10.0,20.0),2))
    flag_hemo = " "
    if (float(hemo)<13.5):
        flag_hemo = "L"
    elif(float(hemo)>18.0):
        flag_hemo = "H" 

    hema = str(round(uniform(35.0,57.0),2))
    flag_hema = " "
    if (float(hema)<40.0):
        flag_hema = "L"
    elif(float(hema)>52.0):
        flag_hema = "H" 

    MCV = str(round(uniform(70.0,120.0),2))
    flag_MCV = " "
    if (float(MCV)<80.0):
        flag_MCV = "L"
    elif(float(MCV)>100.0):
        flag_MCV = "H" 

    MCH = str(round(uniform(23.0,37.0),2))
    flag_MCH = " "
    if (float(MCH)<27.0):
        flag_MCH = "L"
    elif(float(MCH)>33.0):
        flag_MCH = "H" 

    MCHC = str(round(uniform(26.0,41.0),2))
    flag_MCHC = " "
    if (float(MCHC)<31.0):
        flag_MCHC = "L"
    elif(float(MCHC)>36.0):
        flag_MCHC = "H" 

    RDW = str(round(uniform(0.0,19.59),2))
    flag_RDW = " "
    if (float(RDW)>16.4):
        flag_RDW = "H"

    PC = str(round(uniform(60.0,500.0),2))
    flag_PC = " "
    if (float(PC)<150):
        flag_PC = "L" 
    elif(float(PC)>400):
        flag_PC = "H"

    Neut = str(round(uniform(41.0,90.0),2))
    flag_Neut = " "
    if (float(Neut)<49.0):
        flag_Neut = "L"
    elif(float(Neut)>74.0):
        flag_Neut = "H"  

    Lymp = str(round(uniform(21.0,51.0),2))
    flag_Lymp = " "
    if (float(Lymp)<26.0):
        flag_Lymp = "L"
    elif(float(Lymp)>46.0):
        flag_Lymp = "H" 

    Mono = str(round(uniform(0.0,15.0),2))
    flag_Mono = " "
    if (float(Mono)<80.0):
        flag_Mono = "L"
    elif(float(Mono)>100.0):
        flag_Mono = "H" 

    Eosi = str(round(uniform(0.0,12.0),2))
    flag_Eosi = " "
    if (float(Eosi)>0.0):
        flag_Eosi = "H"

    Bosi = str(round(uniform(0.0,5.0),2))
    flag_Bosi = " "
    if (float(Bosi)<2.0):
        flag_Bosi = "H"

    AbNeut = str(round(uniform(0.0,12.0),2))
    flag_AbNeut = " "
    if (float(AbNeut)<2.0):
        flag_AbNeut = "L"
    elif(float(AbNeut)>8.0):
        flag_AbNeut = "H" 

    Ablymp = str(round(uniform(0.0,10.0),2))
    flag_Ablymp = " "
    if (float(Ablymp)<1.0):
        flag_Ablymp = "L"
    elif(float(Ablymp)>5.1):
        flag_Ablymp = "H" 

    AbMono = str(round(uniform(0.0,1.20),2))
    flag_AbMono = " "
    if (float(AbMono)>0.8):
        flag_AbMono = "H"

    AbEosi = str(round(uniform(0.0,1.20),2))
    flag_AbEosi = " "
    if (float(AbEosi)>0.50):
        flag_AbEosi = "H"

    AbBaso = str(round(uniform(0.0,0.80),2))
    flag_AbBaso = " "
    if (float(AbBaso)>0.20):
        flag_AbBaso = "H"

    cbc_data = [
        ["Component", "Your Value", "Standard Range", "Units", "Flag"],
        ["WBC Count", wbc, "4.0-11.0", "K/ul",flag_wbc ],
        ["RBC Count", rbc, "4.40-6.00", "M/ul", flag_rbc],
        ["Hemoglobin", hemo, "13.5-18.0", "g/dl", flag_hemo],
        ["Hematocrit", hema, "40.0-52.0", "%", flag_hema],
        ["MCV", MCV, "80-100", "fl", flag_MCV],
        ["MCH", MCH, "27.0-33.0", "pg", flag_MCH],
        ["MCHC", MCHC, "31.0-36.0", "g/dl", flag_MCHC],
        ["RDW", RDW, "<16.4", "%", flag_RDW],
        ["Platelet Count", PC, "150-400", "K/ul", flag_PC],
        ["Differential Type", "Automated", " ", " ", " "],
        ["Neutrophil %", Neut, "49.0-74.0", "%", flag_Neut],
        ["Lymphocyte %", Lymp, "26.0-46.0", "%", flag_Lymp],
        ["Monocyte %", Mono, "2.0-12.0", "%", flag_Mono],
        ["Eosinophil %", Eosi, "0.0-5.0", "%", flag_Eosi],
        ["Basophil %", Bosi, "0.0-2.0", "%", flag_Bosi],
        ["Abs. Neutrophil", AbNeut, "2.0-8.0", "K/ul", flag_AbNeut],
        ["Abs. Lymphocyte", Ablymp, "1.0-5.1", "K/ul", flag_Ablymp],
        ["Abs. Monocyte", AbMono, "0.0-0.8", "K/ul", flag_AbMono],
        ["Abs. Eosinophil", AbEosi, "0.0-0.5", "K/ul", flag_Eosi],
        ["Abs. Basophil", AbBaso, "0.0-0.2", "K/ul", flag_AbBaso]
    ]

    story = []

    title_style = getSampleStyleSheet()["Title"]
    title_style.alignment = TA_CENTER
    title_style.fontName = 'Helvetica-Bold'
    title_style.fontSize = 27
    title = Paragraph("Complete Blood Count Report", title_style)
    story.append(title) 
    story.append(Spacer(1, 30)) 

    table_style = TableStyle([
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ])

    cbc_table = Table(cbc_data, rowHeights=25, colWidths=(1.25*inch))

    cbc_table.setStyle(table_style)

    story.append(cbc_table)

    pdf_doc.build(story)
