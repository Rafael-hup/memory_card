#создай приложение для запоминания информации
from random import randint
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,QGroupBox,QPushButton,QButtonGroup
app=QApplication([])
main_win=QWidget()
main_win.setWindowTitle('Memory Card')
RadioGroupBox=QGroupBox('Варианты ответов')
text=QLabel('')
answer1=QRadioButton('')
answer2=QRadioButton('')
answer3=QRadioButton('')
answer4=QRadioButton('')
otvet=QPushButton('Ответить')

RadioGroup=QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

layoutH4=QHBoxLayout()
layoutV1=QVBoxLayout()
layoutV2=QVBoxLayout()

layoutV1.addWidget(answer1)
layoutV1.addWidget(answer3)
layoutV2.addWidget(answer2)
layoutV2.addWidget(answer4)
layoutH4.addLayout(layoutV1)
layoutH4.addLayout(layoutV2)

RadioGroupBox.setLayout(layoutH4)

main_layout4=QVBoxLayout()
main_layout=QVBoxLayout()

AnsGroupBox=QGroupBox('Результат теста')
text1=QLabel('Правильно/Неправильно')
text2=QLabel('Правильный ответ',alignment=Qt.AlignCenter)

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question=question
        self.right_answer=right_answer
        self.wrong1=wrong1
        self.wrong2=wrong2
        self.wrong3=wrong3

main_layout4.addWidget(text1)
main_layout4.addWidget(text2)

AnsGroupBox.setLayout(main_layout4)
AnsGroupBox.hide()

questions_list=[]
q1=Question('1+1=?','2','4','3','5')
q2=Question('2*5=?','10','100','15','20')
q3=Question('Как звали первого ютуб-блогера, набравшего 100000000 подписчиков?','PewDiePie','Рэт и Линк','SlivkiShow','EeOneGuy')
q4=Question('2/5=?','0.4','0.3','10','4')
q5=Question('Государственный язык Португалии?','Португальский','Испанский','Английский','Французский')
q6=Question('Чему равна сумма углов треугольника?','180','360','90','200')
q7=Question('В каком году придумали первую машину?','1886','1900','1885','1890')
q8=Question('Какой национальности не существует?','Энцы','Смурфы','Чулымци','Алеуты')
q9=Question('В каком году был создан первый компьютер?','1927','1930','1900','1928')
q10=Question('Государственый язык Бразилии ?','Португальский','Немецкий','Испанский','Бразильский')
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
questions_list.append(q10)
answers=[answer1, answer2, answer3, answer4]
def next_question():
    main_win.total += 1
    cur_question = randint(0, len(questions_list) -1)
    a=questions_list[cur_question]
    print('Всего ответов:',main_win.total)
    ask(a)
def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    text2.setText(q.right_answer)
    text.setText(q.question)
    show_question()
def show_correct(res):  
    text1.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        show_correct('Правильно')
        print('Правильных ответов:', main_win.score)
        print('Статистика:',main_win.score/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    otvet.setText('Следующий вопрос')
def show_question():
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()
    AnsGroupBox.hide()
    otvet.setText('Ответить')
def start_test():
    if otvet.text()=='Ответить':
        show_result()
    else:
        show_question()
def click_ok():
    if otvet.text()=='Ответить':
        check_answer()
    else:
        next_question()


otvet.clicked.connect(click_ok)
main_win.score=0
main_win.total=0
next_question()

layoutH1=QHBoxLayout()
layoutH2=QHBoxLayout()
layoutH3=QHBoxLayout()

layoutH1.addWidget(text)
layoutH2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
layoutH2.addWidget(AnsGroupBox, alignment=Qt.AlignCenter)
layoutH3.addWidget(otvet)

main_layout.addLayout(layoutH1)
main_layout.addLayout(layoutH2)
main_layout.addLayout(layoutH3)

main_win.setLayout(main_layout)

main_win.show()
app.exec_()