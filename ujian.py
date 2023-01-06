#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate

import streamlit as st

# st.markdown(""" <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style> """, unsafe_allow_html=True)

# st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("logolabti.png", width=150)

with col3:
    st.write(' ')

st.markdown("<h1 style='text-align: center; color: white;'>Information Technology Laboratory</h1>", unsafe_allow_html=True)

st.markdown("""
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
""", unsafe_allow_html=True)

st.markdown("""
<!-- Image and text -->
<nav class="navbar fixed-bottom navbar-expand-lg navbar-dark" style="background-color: #BA3EC8">
  <a class="navbar-brand" href="#">
    University of Gunadarma
  </a>
</nav>
""", unsafe_allow_html=True)

st.write("""
# **Final Score IMK 3IA20**
Keep fighting and never surrender. #ThisIsOnlyTheBegining
""")

npm = st.text_input("NPM : ")
search = st.button("Search")

if search or npm:
    if npm == "20422065":
        pretest = (160)/7
        posttest = (180)/7
        activity = (90)/7
        fnlrpt = (70)/7
        exscore = 0
        attdnc = (5/7)*100
        st.write("Name: ABI NAUFAL KHALID")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "12345678":
        pretest = (95+90+80+60+50+90+90+70)/7
        posttest = (95+90+80+50+95+90+20+70)/7
        activity = (20+70+70+70+70+90+20+70)/7
        fnlrpt = (20+70+70+70+70+90+100+70)/7
        exscore = 78
        attdnc = (7/8)*100
        st.write("Name: CONTOH INPUT")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)
    
    elif npm == "20422099":
        pretest = (500)/7
        posttest = (480)/7
        activity = (390)/7
        fnlrpt = (440)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: ADNAN NAUFAL FADHILA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422134":
        pretest = (600)/7
        posttest = (700)/7
        activity = (580)/7
        fnlrpt = (550)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: AHMAD UZAIR")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422167":
        pretest = (480)/7
        posttest = (640)/7
        activity = (580)/7
        fnlrpt = (640)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: ALFUR NUR HIDAYAT")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422289":
        pretest = (80)/7
        posttest = (100)/7
        activity = (150)/7
        fnlrpt = (70)/7
        exscore = 0
        attdnc = (4/7)*100
        st.write("Name: ATHAR HAKIM DARMAWAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/3/5")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422004":
        pretest = (620)/7
        posttest = (660)/7
        activity = (500)/7
        fnlrpt = (540)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: BAYU PAMUNGKAS")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422358":
        pretest = (500)/7
        posttest = (540)/7
        activity = (350)/7
        fnlrpt = (560)/7
        exscore = 85
        attdnc = (5/7)*100
        st.write("Name: CHRISTHOPER PRAYOGA SEBASTIAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/3")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422516":
        pretest = (500)/7
        posttest = (600)/7
        activity = (270)/7
        fnlrpt = (70)/7
        exscore = 0
        attdnc = (5/7)*100
        st.write("Name: FAREL ALFAREZA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422554":
        pretest = (260)/7
        posttest = (200)/7
        activity = (140)/7
        fnlrpt = (210)/7
        exscore = 90
        attdnc = (5/7)*100
        st.write("Name: FEBRIANSAH ISNAINI")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422015":
        pretest = (480)/7
        posttest = (620)/7
        activity = (490)/7
        fnlrpt = (460)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: FIKRI ARDIANSYAH")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422609":
        pretest = (240)/7
        posttest = (300)/7
        activity = (250)/7
        fnlrpt = (460)/7
        exscore = 80
        attdnc = (3/7)*100
        st.write("Name: GERALD RENHART ONKEI SIAHAAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/4/5/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422653":
        pretest = (560)/7
        posttest = (580)/7
        activity = (490)/7
        fnlrpt = (480)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: HANPAN GIFARI AL AFGANI")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422721":
        pretest = (640)/7
        posttest = (620)/7
        activity = (400)/7
        fnlrpt = (490)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: IRHAM KHADAFI HARISMAWAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 3")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422786":
        pretest = (60)/7
        posttest = (100)/7
        activity = (0)/7
        fnlrpt = (210)/7
        exscore = 78
        attdnc = (2/7)*100
        st.write("Name: KHAIRUL ALFI SANTOSO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/3/4/5/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422813":
        pretest = (640)/7
        posttest = (660)/7
        activity = (600)/7
        fnlrpt = (450)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: LOUIS PETER YOAS SILALAHI")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "20422897":
        pretest = (440)/7
        posttest = (400)/7
        activity = (420)/7
        fnlrpt = (380)/7
        exscore = 90
        attdnc = (5/7)*100
        st.write("Name: MOHAMAD ARYA FEBRIYANTO")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422058":
        pretest = (0)/7
        posttest = (0)/7
        activity = (70)/7
        fnlrpt = (0)/7
        exscore = 90
        attdnc = (5/7)*100
        st.write("Name: MUHAMMAD FIQRI FADILLAH")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 3/4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422154":
        pretest = (280)/7
        posttest = (180)/7
        activity = (250)/7
        fnlrpt = (210)/7
        exscore = 80
        attdnc = (3/7)*100
        st.write("Name: MUHAMMAD SABIQ KAYYAS")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 1/2/4/6")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422285":
        pretest = (580)/7
        posttest = (660)/7
        activity = (550)/7
        fnlrpt = (470)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: Paulinus Kenas Angger Widodo")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422351":
        pretest = (560)/7
        posttest = (680)/7
        activity = (480)/7
        fnlrpt = (310)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: RAHMATULLAH FATURONIY ASSILA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422470":
        pretest = (620)/7
        posttest = (640)/7
        activity = (490)/7
        fnlrpt = (410)/7
        exscore = 95
        attdnc = (6/7)*100
        st.write("Name: RIZKY FADHILLAH")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422538":
        pretest = (460)/7
        posttest = (660)/7
        activity = (600)/7
        fnlrpt = (490)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: SIEMENS ERLANGGA HAICAL PUTRA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422637":
        pretest = (620)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (490)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: WYRA ALDY FERRERO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "21422649":
        pretest = (580)/7
        posttest = (660)/7
        activity = (500)/7
        fnlrpt = (520)/7
        exscore = 100
        attdnc = (7/7)*100
        st.write("Name: YOGIE ARI SAMUDRA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420401":
        pretest = (700)/7
        posttest = (680)/7
        activity = (560)/7
        fnlrpt = (520)/7
        exscore = 92
        attdnc = (7/7)*100
        st.write("Name: NANDI RIFALDI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420004":
        pretest = (600)/7
        posttest = (600)/7
        activity = (560)/7
        fnlrpt = (155)/7
        exscore = 0
        attdnc = (6/7)*100
        st.write("Name: PETRA EUAGGELION DEVON")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420007":
        pretest = (0)/7
        posttest = (0)/7
        activity = (0)/7
        fnlrpt = (0)/7
        exscore = 0
        attdnc = (0/7)*100
        st.write("Name: PRAMUDYA REIHANSYAH SUNDAFA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4/5/7")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420011":
        pretest = (700)/7
        posttest = (700)/7
        activity = (650)/7
        fnlrpt = (610)/7
        exscore = 95
        attdnc = (7/7)*100
        st.write("Name: PRAYOGA DANUARTA")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 4")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420051":
        pretest = (700)/7
        posttest = (700)/7
        activity = (570)/7
        fnlrpt = (400)/7
        exscore = 100
        attdnc = (6/7)*100
        st.write("Name: RALFATIHANUR ZIAFIQ MAKPAL")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420162":
        pretest = (700)/7
        posttest = (700)/7
        activity = (580)/7
        fnlrpt = (480)/7
        exscore = 95
        attdnc = (7/7)*100
        st.write("Name: SALSABILA FEBRIYANA")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420219":
        pretest = (540)/7
        posttest = (500)/7
        activity = (150)/7
        fnlrpt = (300)/7
        exscore = 80
        attdnc = (0/7)*100
        st.write("Name: SYAFIQ SHAFWAN FAUZAN")
        st.write("Attendance: %.0f" % attdnc, "% Absent on week 8")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420289":
        pretest = (680)/7
        posttest = (700)/7
        activity = (150)/7
        fnlrpt = (150)/7
        exscore = 78
        attdnc = (0/7)*100
        st.write("Name: YAZID FARHAN MUZAKKY")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51420299":
        pretest = (660)/7
        posttest = (700)/7
        activity = (600)/7
        fnlrpt = (550)/7
        exscore = 92
        attdnc = (7/7)*100
        st.write("Name: YONATHAN CHRISTIANTO")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421466":
        pretest = (800)/7
        posttest = (800)/7
        activity = (740)/7
        fnlrpt = (640)/7
        exscore = 100
        attdnc = (8/8)*100
        st.write("Name: TEGAR DWI SEPTIADI")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    elif npm == "51421552":
        pretest = (800)/7
        posttest = (780)/7
        activity = (640)/7
        fnlrpt = (640)/7
        exscore = 90
        attdnc = (8/8)*100
        st.write("Name: ZAHIDAN ARDHIANSYAH")
        st.write("Attendance: %.0f" % attdnc, "%")
        st.write("Average pre-test score: %.1f" % pretest)
        st.write("Average post-test score: %.1f" % posttest)
        st.write("Average activity score: %.1f" % activity)
        st.write("Average final report score: %.1f" % fnlrpt)
        st.write("Exam Score: ", exscore)

    else:
        st.write("NPM not found")

    estgrade = (pretest+posttest+activity+fnlrpt+exscore)/5
    if estgrade >= 80:
        st.write("Estimation grade from LAB TI: A")
    elif estgrade >= 70:
        st.write("Estimation grade from LAB TI: B")
    elif estgrade >= 60:
        st.write("Estimation grade from LAB TI: C")
    else:
        st.write("Estimation grade from LAB TI: D")
    st.balloons()

#/home/mufin/.local/share/virtualenvs/My_Projects-23sAJxQN/bin/activate
