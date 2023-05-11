#1.HAFTA
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton,
QPushButton, QLabel, QButtonGroup)
 
#3.HAFTA(shuffle)  4.HAFTA(randint)
from random import shuffle , randint
 
#3.HAFTA
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    # bir nesne oluştururken tüm stringlerin ayarlanması gerekmektedir, bunlar özelliklerde saklanmaktadırlar
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
 
questions_list = []
questions_list.append(Question('Brezilya\'nın resmi dili', 'Portekizce', 'ingilizce', 'İspanyolca',
'Brezilyaca'))
questions_list.append(Question('Rusya bayrağında hangi renk yoktur?', 'Yeşil', 'Kırmızı', 'Beyaz', 'Mavi'))
questions_list.append(Question('Yakutların yöresel evleri', 'Urasa', 'Yurt', 'İglo', 'Peri bacaları'))
 
#1.HAFTA
app = QApplication([])
 
window = QWidget() #pencerenin getirilmesi
window.setWindowTitle('Memo Card') #pencere başlığı
window.resize(400,300) #pencerenin yeniden boyutlandırılması 
 
'''Memory Card uygulamasının arayüzü'''
btn_OK = QPushButton('Cevapla') # cevap düğmesi oluşturma ve etiketini ekleme
lb_Question = QLabel('Soru cümlesi buraya yazılacak?') # soru metni
 
#1.HAFTA
#seçeneklerin radio buton olarak ayarlanması
RadioGroupBox = QGroupBox("Cevap seçenekleri") # ekrandaki grup cevapları olan anahtarlar içindir
rbtn_1 = QRadioButton('Seçenek 1') #cevap seçeneklerinin radio buton olarak oluşturulması
rbtn_2 = QRadioButton('Seçenek 2') #cevap seçeneklerinin radio buton olarak oluşturulması
rbtn_3 = QRadioButton('Seçenek 3') #cevap seçeneklerinin radio buton olarak oluşturulması
rbtn_4 = QRadioButton('Seçenek 4') #cevap seçeneklerinin radio buton olarak oluşturulması
 
#2.HAFTA 
#grubun oluşturulması
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
#1.HAFTA
#Hizalamalar
layout_ans1 = QHBoxLayout() #yatay hizalama
layout_ans2 = QVBoxLayout() # dikey hizalama (dikey olanlar yatay olanın içinde olacak)
layout_ans3 = QVBoxLayout() #dikey hizalama
layout_ans2.addWidget(rbtn_1) #ilk sütuna iki cevap (butonun dikey hizalamaya eklenmesi)
layout_ans2.addWidget(rbtn_2) #butonun dikey hizalamaya eklenmesi
layout_ans3.addWidget(rbtn_3) # ikinci sütuna iki cevap (butonun dikey hizalamaya eklenmesi)
layout_ans3.addWidget(rbtn_4) #butonun dikey hizalamaya eklenmesi
 
layout_ans1.addLayout(layout_ans2) #sütunlar tek satıra yerleştirildi
layout_ans1.addLayout(layout_ans3) #sütunlar tek satıra yerleştirildi
 
RadioGroupBox.setLayout(layout_ans1) # cevap seçeneklerini içeren "panel" hazır
 
#2.HAFTA
#test sonucunun D/Y kontrol edileceği arayüz
AnsGroupBox = QGroupBox("Test sonucu")   #grupbox başlığı
lb_Result = QLabel('haklı mısın değil misin?')  #D/Y yazdırılması
lb_Correct = QLabel('cevap burda olacak!') #Yanlışsa doğru cevabın gösterilmesi
layout_res = QVBoxLayout() #dikey hizalama
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop)) #dikey hizalamaya veri atama
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2) #dikey hizalamaya veri atama
AnsGroupBox.setLayout(layout_res)
 
#1.HAFTA
#ekrandahi yatay hizalamaların hazırlanması
layout_line1 = QHBoxLayout() # soru
layout_line2 = QHBoxLayout() # cevap seçenekleri veya test sonucu
layout_line3 = QHBoxLayout() # "Cevapla" düğmesi
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) #1.satıra soruyu ekleme
layout_line2.addWidget(RadioGroupBox) #2. satıra grupbox'ın eklenmesi
 
#2.HAFTA
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide() #cevap ekranı gizlenir. Sonuca göre daha sonra gösterilir.
 
#1.HAFTA
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # düğme büyük olmalı (3. satıra butonun eklenmesi)
layout_line3.addStretch(1)
 
# Şimdi oluşturulan satırları birbirinin altına yerleştireceğiz:
layout_card = QVBoxLayout() #ana ekranda dikey hizalamnın oluşturulması
 
#yatay hizaların (satırların) dikey tek bir çizgide toplanması
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # içerik arasındaki boşluklar
 
#2.HAFTA
# ----------------------------------------------------------
# Widget'lar ve düzenler oluşturuldu, sırada-fonksiyonlar:
# ----------------------------------------------------------
 
def show_result():
    ''' cevap panelini gösteriniz '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Sıradaki soru')
def show_question():
    ''' soru panelini gösteriniz '''
    RadioGroupBox.show() #soru formunu gösterir.
    AnsGroupBox.hide() #cevap formunu gizler
    btn_OK.setText('Cevapla') # 'Sıradaki soru' yazısını 'Cevapla' ile değiştirir.
    RadioGroup.setExclusive(False) # radyo düğme seçiminin sıfırlanabilmesi için kısıtlamalar kaldırıldı
    #tüm radio butonların seçimi kaldırılır. (Bir sonraki soruya geçtiğinde işaretin olmaması için)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # kısıtlamalar geri getirildi, şimdi sadece bir radyo düğmesi seçilebilir



#3.HAFTA
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    ''' fonksiyon, soru ve cevapların değerlerini ilgili widgetlara yazar,
    cevap seçenekleri ise rastgele dağıtılır '''
    shuffle(answers) # düğme listesi karıştırıldı, artık listenin ilk sırasında öngörülemeyen bir düğme var
    answers[0].setText(q.right_answer) # listenin ilk öğesini doğru cevapla dolduralım, geriye kalanlar yanlış cevaplarla doldurulacak
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question) # soru
    lb_Correct.setText(q.right_answer) # cevap
    show_question() # soru panelini gösteriyoruz
 
#3.HAFTA
def show_correct(res):
    ''' sonucu gösterme - iletilen metni "sonuç" etiketine yerleştirelim ve gerekli paneli gösterelim '''
    lb_Result.setText(res)
    show_result()
 
    
#4.HAFTA (3.HAFTA yazılan check_answer fonksiyonunun içeriği değiştirilir)
def check_answer():
    ''' eğer herhangi bir cevap seçeneği seçili ise kontrol edilip cevap panelinin gösterilmesi
    gerekmektedir'''
    if answers[0].isChecked():
    # doğru cevap!
        show_correct('Doğru!')
        window.score += 1 #doğru cevabın seçilmesi durumunda 1 artar.
        print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score) 
        print('Puanlama: ', (window.score/window.total*100), '%') #sorulan soruların yüzde kaçının doğru yapıldığını gösterir.
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # yanlış cevap!
            show_correct('Yanlış!')
            print('Puanlama: ', (window.score/window.total*100), '%')
    #Ör: 2 soru, 1 Doğru 1 Yanlış cevapta score %50 gibi..
 
#4.HAFTA (3.HAFTA yazılan next_question fonksiyonunun içeriği değiştirilir)
def next_question():
    ''' listeden rastgele bir soru sorar '''
    window.total += 1 #bir sonraki soruya geçildiğinde 1 artar
    print('İstatistik\n-Toplam soru: ', window.total, '\n-Doğru cevap: ', window.score)
    cur_question = randint(0, len(questions_list) - 1) # eski değere ihtiyaçımız yoktur,
    # bu nedenle lokal bir değişken kullanılabilir!
    # rastgele listeden bir soru alındı
    # yaklaşık yüz kelime girilirse, nadiren tekrarlanır
    q = questions_list[cur_question] # soruyu aldık
    ask(q) # soruldu
 
#3.HAFTA
def click_OK():
    ''' başka sorunun gösterilip gösterilmeyeceğini veya bu soruya verilen cevabın kontrol edilip
    edilmeyeceğini belirler'''
    if btn_OK.text() == 'Cevapla':
        check_answer() # cevabın kontrolü
    else:
        next_question() # sıradaki soru
 
window.setLayout(layout_card) #hepsini içinde bulunduran layout_card ekle
 
btn_OK.clicked.connect(click_OK) # butona tıklayarak tam olarak ne olacağını seçiyoruzbtn_OK.clicked.connect (test) # butona tıklandığında cevap panelinin gösterilip gösterilmediğini kontrol ediyoruz
 
''' Burayı 4.Haftada sil
#3.HAFTA
window.cur_question = -1
'''
 
#4.HAFTA
#Puanlama sisteminin oluşturulabilmesi için terminalde gösterilecek değişkenler oluşturulur.
window.score = 0 #verilen doğru cevapların sayımı için
window.total = 0  #kaç soru sorulduğunu hesaplayacak
 
next_question()
 
window.show() #pencereyi göster
app.exec() #uygulamayı çalıştır