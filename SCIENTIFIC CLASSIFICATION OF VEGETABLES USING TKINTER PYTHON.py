from tkinter import *


object = Tk()
object.config(bg="steel blue")
object.title("SCIENTIFIC CLASSIFICATION OF VEGETABLES")
object.geometry("1400x800")


lbl= Label(object,text= "SCIENTIFIC CLASSIFICATION OF VEGETABLES",bg="medium spring green",fg="midnight blue",font=("arial",15),height=2,width=105).pack()
lbl01=Label(object,text=" ",bg="steel blue",fg="steel blue",height=10,width=44).pack()

def vegetables():



 def tomato():
    lbl0 = Label(object,text=(
        "Vegetable_name=TOMATO"
        "\nBotanical_Name =Solanumlycopersicum "
        "\nKingdom=Plantae Clade= Tracheophytes, Angiosperms, Eudicots, Asterids "
        "\nFamily=Solanaceae "
        "\nGenus=Solanum "
        "\nSpecies=S.lycopersicum "
        "\nDiseases_affects_this_plant=Bacterialwilt(Ralstoniasolanacearum)"
        "\nCommon mosaic of tomato (  Tobacco mosaic virus (TMV) )"
        "\n Climatic_condition =Tomato can be grown on a wide range of soils from sandy to heavy clay "
        "\npH_of_soil =pH range of 6. 0 -7.0 "
        "\nOptimum_temperature =temperature range of 21 -24°C"
        "\nvegetable name in other languages:tamaatar(Hindi),takkāḷi(Tamil,Malayalam),Ṭamōṭā(telegu),Ṭomeṭo(kannada)")
                 ,fg="#03ffee",bg="#ff6347").pack()



 B0=Button(object,text="TOMATO",fg="#03ffee",bg="#ff6347",command=tomato,height=1,width=11)
 B0.pack()
 B0.place(x=10,y=10+60)

 def potato():
      lbl1= Label(object,text=(
      "vegetable_name=POTATO"
      "\nBotanical Name = Solanum tuberosum "
      "\nKingdom :  Plantae"
      "\nClade:   Tracheophytes,Angiosperms,Eudicots,Asterids"
      "\nOrder:    Solanales"
      "\nFamily:    Solanaceae"
      "\nGenus:    Solanum"
      "\nSpecies:  S. tuberosum " 
      "\nDiseases affects this plant: Pink eye(Pseudomonas fluorescens)"
      "\nCommon rust (Puccinia pittieriana)"
      "\nAlfalfa mosaic virus(  genus Alfamovirus, Alfalfa mosaic virus (AMV)  )"
      "\nClimatic condition :  The potato can be grown almost on any type of soil except saline and alkaline soils"
      "\npH of soil :  pH range of 5.2-6.4"
      "\nOptimum temperature :  temperature range of 20-24°C"
      "\nvegetable name in other languages:Uruḷaikkiḻaṅku(Tamil),aaloo(Hindi),uruḷakkiḻaṅṅ(Malayalam),Baṅgāḷādumpa(Telegu),Ālūgaḍḍe(Kannada)")
      ,fg="#03ffee",bg="#b79268").pack()

 B1=Button(object,text="POTATO",fg="#03ffee",bg="#b79268",command=potato,height=1,width=11)
 B1.pack()
 B1.place(x=10,y=40+60)

 def brinjal():
    lbl2= Label(object,text=(
        "vegetable_name=BRINJAL"
    "\nbotanical Name=Solanum melongena ;  Kingdom :  Plantae"
    "\nClade:   Tracheophytes,Angiosperms,Eudicots,Asterids"
    "\nOrder:  Solanales"
    "\nFamily: Solanaceae"
    "\nGenus:  Solanum"
    "\nSpecies:  S. melongena"
    "\nDiseases affects this plant: Southern Wilt (Ralstonia solanacearum) "
    "\nCercospora Leaf Spot (Cercospora spp.)"
    "\nDamping Off (Pythium spp., Fusarium spp.)"
    "\nClimatic condition : Brinjal is a warm season crop and requires a long warm growing season"
    "\npH of soil :  pH range of 5.5-6.6"
    "\nOptimum temperature :  temperature range of 13-21°C"
    "\nvegetable name in other languages:Kattirikkāy(Tamil),baingan(Hindi),vaḻutana(Malayalam),Vaṅkāya(Telegu),baingan(Kannada)")
                ,fg="#03ffee",bg="#614051").pack()

 B2=Button(object,text="BRINJAL",fg="#03ffee",bg="#614051",command=brinjal,height=1,width=11)
 B2.pack()
 B2.place(x=10,y=70+60)

 def radish():
    lbl3= Label(object,text=(
        "vegetable_name=RADISH"
        "\nBotanical Name – Raphanus raphanistrum subsp.sativus"
        "\nKingdom :  plantae"  
        "\nClade:   Tracheophytes,angiosperm,eudicots,rosids" 
        "\nOrder:  brassicales" 
        "\nFamily: brassicaceae"  
        "\nGenus:raphanus"  
        "\nSpecies: R.raphanistrum" 
        "\nDiseases affects this plant:  Alternaria blight Alternaria spp."   
        "\nClubroot Plasmodiophora brassicae"  
        "\nDowny mildew Peronospora parasitica" 
        "\nsoil type :  Sandy loam soils with high organic matter content are highly suited for radish cultivation" 
        "\npH of soil :  pH range of 5.5-6.8"  
        "\nOptimum temperature :  temperature range of 15°C"
        "\nvegetable name in other languages:muḷḷaṅki(Tamil),moolee(Hindi),muḷḷaṅki(Malayalam),Mullaṅgi(Telegu),Mūlaṅgi(Kannada)")
                ,fg="#03ffee",bg="bb1f44").pack()

 B3=Button(object,text="RADISH",fg="#03ffee",bg="#bb1f44",command=radish,height=1,width=11)
 B3.pack()
 B3.place(x=10,y=100+60)

 def carrot():
    lbl4= Label(object,text=(
        "vegetable_name=CARROT"
        "\nBotanical Name – Daucus carota subsp.sativus"
        "\nKingdom :plantae"
        "\nClade:Tracheophytes,angiosperm,eudicots,asterids "
        "\nOrder:apiaceae"
        "\nFamily:apiaceae"
        "\nGenus:  daucus"
        "\nSpecies:D. carota "
        "\nDiseases affects this plant: Cavity Spot,Common Scab,Lateral Root Dieback Leaf Blight."
        "\npH of soil :pH range of 6.0-7.0"
        "\nOptimum temperature :temperature range of 15-20°C"
        "\nvegetable name in other languages:Kēraṭ(Tamil),gaajar(Hindi),kāraṟṟ(Malayalam),Kāreṭ(Telegu),Kyāreṭ(Kannada)"),fg="#03ffee",bg="#ed9121").pack()

 B4=Button(object,text="CARROT",fg="#03ffee",bg="#ed9121",command=carrot,height=1,width=11)
 B4.pack()
 B4.place(x=10,y=130+60)

 def drumstick():
    lbl5= Label(object,text=(
        "vegetable_name=DRUM STICK"
        "\nBotanical name -Moringa oleifera"
        "\nKingdom:    Plantae"
        "\nClade:    Tracheophytes,Angiosperms,Eudicots,Rosids,"
        "\norder:Brassicales"
        "\nFamily:    Moringaceae"
        "\nGenus:    Moringa"
        "\nSpecies:    M.oleifera"
        "\nDiseases affects this plant:twig canker,red mites,fruit rots"
        "\npH of soil :pH range of6.2 to neutral 7.0"
        "\nOptimum temperature :temperature range of 25 to 30°C"
        "\nvegetable name in other languages:Muruṅkaikkāy(Tamil),dhol ka chhadee(Hindi),muriṅṅayila(Malayalam),Ḍram sṭik(Telegu),Ḍram sṭik(Kannada)")
                ,fg="#03ffee",bg="#4e5b31").pack()

 B5=Button(object,text="DRUMSTICK",fg="#03ffee",bg="#4e5b31",command=drumstick,height=1,width=11)
 B5.pack()
 B5.place(x=10,y=160+60)

 def ladiesfinger():
    lbl6= Label(object,text=(
        "vegetable_name=LADIES FINGER"
        "\nBotanical name - Abelmoschus esculentus"
        "\nKingdom: Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder:Malvales"
        "\nFamily:Malvaceae"
        "\nGenus:Abelmoschus"
        "\nSpecies:A.esculentus"
        "\nDiseases affects this plant:Damping Off (Pythium sp., Rhizoctonia sp.)"
        "\nFusarium Wilt(Fusarium oxysporum f. sp. vasinfectum)"
        "\nPowdery Mildew (Erysiphecichoracearum)"
        "\npH of soil :pH range of6.0-6.8"
        "\nsoil type: It grows best in loose, friable, well-drained sandy loam soils rich in organic matter"
        "\nOptimum temperature :temperature range of24-27°C"
        "\nvegetable name in other languages:Veṇṭaikkāy(Tamil),bhindee(Hindi),strīkaḷuṭe viral(Malayalam),Lēḍīs vēlu(Telegu),Heṅgasara beraḷu(Kannada)")
                ,fg="#03ffee",bg="#428f28").pack()

 B6=Button(object,text="LADIES FINGER",fg="#03ffee",bg="#428f28",command=ladiesfinger,height=1,width=11)
 B6.pack()
 B6.place(x=10,y=190+60)

 def bittergourd():
    lbl7= Label(object,text=(
        "vegetable_name=BITTER GOURD"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder:Cucurbitales"
        "\nFamily:Cucurbitaceae"
        "\nGenus:Momordica"
        "\nSpecies: M.charantia"
        "\nDiseases affects this plant:Downy mildew,Powdery mildew,Mosaic"
        "\nsoil type : Bitter gourd can be grown on well drained sandy to sandy loam; medium black soils rich in organic matter"
        "\npH of soil :pH range of6.0- 7.0"
        "\nOptimum temperature : temperature range of24- 27°C"
        "\nvegetable name in other languages:Pākaṟkāy(Tamil),karela(Hindi),pāvaykka(Malayalam),Kākarakāya(Telegu),Hāgalakāyi(Kannada)")
                ,fg="#03ffee",bg="#2b6b21").pack()

 B7=Button(object,text="BITTER GOURD",fg="#03ffee",bg="#2b6b21",command=bittergourd,height=1,width=11)
 B7.pack()
 B7.place(x=105,y=10+60)

 def bottlegourd():
    lbl8= Label(object,text=(
        "vegetable_name=BOTTLE GOURD"
        "\nbotanical name - Lagenaria siceraria"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder:Cucurbitales"
        "\nFamily:Cucurbitaceae"
        "\nGenus:Lagenaria"
        "\nSpecies:L.siceraria"
        "\nDiseases affects this plant:anthracnose, gummy stem blight, fusarium wilt"
        "\nsoil type :Bottle gourd can be grown in wide range of soils. But it thrives well in sandy loam soils"
        "\npH of soil :pH range of6.5 to 7.5"
        "\nOptimum temperature :temperature range of 24- 27°C"
        "\nvegetable name in other languages:Curaikkāy(Tamil),laukee(Hindi),kuppi peāṟēāṭṭa(Malayalam),Sīsā poṭlakāya(Telegu),Bāṭal sōrekāyi(Kannada)")
                ,fg="#003834",bg="#76e053").pack()

 B8=Button(object,text="BOTTLE GOURD",fg="#003834",bg="#76e053",command=bottlegourd,height=1,width=11)
 B8.pack()
 B8.place(x=105,y=40+60)

 def snakegourd():
    lbl9= Label(object,text=(
        "vegetable_name=SNAKE GOURD"
        "\nBotanical Name - Trichosanthes cucumerina L."
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder:Cucurbitales"
        "\nFamily:Cucurbitaceae"
        "\nGenus:Trichosanthes"
        "\nSpecies:T.cucumerina"
        "\nDiseases affects this plant:Downy mildew,Powdery mildew"
        "\nsoil type :Sandy loam soils rich in organic matter with good drainag"
        "\npH of soil :pH range of 6.5-7.5"
        "\nOptimum temperature :temperature range of 24- 27°C"
        "\nvegetable name in other languages:Puṭalaṅkāy(Tamil),chichinda(Hindi),paṭavaḷaṅṅa(Malayalam),Pāmukāya(Telegu),Hāvina sōrekāyi(Kannada)")
                ,fg="#03ffee",bg="#6EAE00").pack()

 B9=Button(object,text="SNAKE GOURD",fg="#03ffee",bg="#6EAE00",command=snakegourd,height=1,width=11)
 B9.pack()
 B9.place(x=105,y=70+60)

 def spinegourd():
    lbl10= Label(object,text=(
        "vegetable_name=SPINE GOURD"
        "\nBotanical Name - Momordica dioica Roxb. ex Willd."
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms, Eudicots,Rosids"
        "\nOrder:Cucurbitales"
        "\nFamily:Cucurbitaceae"
        "\nGenus:Momordica"
        "\nSpecies:M.dioica"
        "\nDiseases affects this plant:Downy mildew, anthracnose, powdery mildew"
        "\nsoil type :Spine gourd can be grown on sandy loam to clay soils"
        "\npH of soil :pH range of 5.5 to 7.0"
        "\nOptimum temperature :temperature range of25 to 40°C"
        "\nvegetable name in other languages:Mutukelumpu(Tamil),reedh kee haddee(Hindi),naṭṭell(Malayalam),Vennemuka(Telegu),Bennuhuri(Kannada)")
                 ,fg="#03ffee",bg="#8ea116").pack()

 B10 = Button(object,text="SPINE GOURD",fg="#03ffee",bg="#8ea116",command=spinegourd,height=1,width=11)
 B10.pack()
 B10.place(x=105,y=100+60)

 def spinach():
    lbl11= Label(object,text=(
        "vegetable_name=SPINACH"
        "\nBotanical Name - Spinacia oleracea L."
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots"
        "\nOrder:Caryophyllales"
        "\nFamily:Amaranthaceae"
        "\nGenus:Spinacia"
        "\nSpecies:S.oleracea"
        "\nDiseases affects this plant:Anthracnose,Cladosporium leaf spot,Damping-off/Seedling blight"
        "\nsoil type :it grows in wide range of sile which is rich in organic matter"
        "\npH of soil :pH range of 6.5 and 7.5"
        "\nOptimum temperature :temperature range of 5 °C to 24 °C"
        "\nvegetable name in other languages:Kīrai(Tamil),paalak(Hindi),cīra(Malayalam),Baccalikūra(Telegu),Soppu(Kannada)")
                 ,fg="#03ffee",bg="#124700").pack()

 B11 = Button(object,text="SPINACH",fg="#03ffee",bg="#124700",command=spinach,height=1,width=11)
 B11.pack()
 B11.place(x=105,y=130+60)

 def chillies():
    lbl12= Label(object,text=(
        "vegetable_name=CHILLIES"
        "\nBotanical Name- Capsicum frutescens"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Asterids"
        "\nOrder:Solanales"
        "\nFamily:Solanaceae"
        "\nTribe:Capsiceae L."
        "\nGenus:Capsicum L."
        "\nDiseases affects this plant:Cercospora leaf spot,Fusarium wilt,Leaf curl virus"
        "\nsoil type :Black soil which keeps hold of moisture is perfect for chillies"
        "\npH of soil :pH range of 5.0-6.0"
        "\nOptimum temperature :temperature range of 20⁰-25⁰C "
        "\nvegetable name in other languages:Miḷakāy(Tamil),mirch(Hindi),muḷak (Malayalam),Mirapakāyalu(Telegu),Meṇasinakāyigaḷu(Kannada)")
                 ,fg="blue",bg="violet").pack()

 B12 = Button(object,text="CHILLIES",fg="#03ffee",bg="#E32227",command=chillies,height=1,width=11)
 B12.pack()
 B12.place(x=105,y=160+60)

 def capsicum():
    lbl13= Label(object,text=(
        "vegetable_name=CAPSICUM"
        "\nBotanical Name- Capsicum annum"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Asterids"
        "\nOrder:Solanales"
        "\nFamily:Solanaceae"
        "\nSubfamily: Solanoideae"
        "\nTribe:Capsiceae"
        "\nGenus:Capsicum"
        "\nDiseases affects this plant:Crown Gall,Verticillium wilt,Verticillium wilt"
        "\nsoil type :Capsicums require rich, fertile soil."
        "\npH of soil :pH range of 6 to 7"
        "\nOptimum temperature :temperature range of 18-30⁰C"
        "\nvegetable name in other languages:Kuṭaimiḷakāy(Tamil),shimala mirch(Hindi),kāpsikkaṁ(Malayalam),Kyāpsikam(Telegu),Doṇṇe meṇasina kāyi(Kannada)")
                 ,fg="#00b5a9",bg="#f7f300").pack()

 B13 = Button(object,text="CAPSICUM",fg="#00b5a9",bg="#f7f300",command=capsicum,height=1,width=11)
 B13.pack()
 B13.place(x=105,y=190+60)

 def beetroot():
    lbl14= Label(object,text=(
        "vegetable_name=BEET ROOT"
        "\nBotanical Name-Beta vulgaris"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots"
        "\nOrder:Caryophyllales"
        "\nFamily:Amaranthaceae"
        "\nGenus:Beta"
        "\nSpecies:B.vulgaris"
        "\nDiseases affects this plant:Crown gall,Phoma leaf spot,Lettuce infectious yellows"
        "\nsoil type :Beetroot grows in neutral, moist, fertile soil without too much lime or acidity"
        "\npH of soil :pH range of 6.0 and 7.5"
        "\nOptimum temperature :temperature range of 18 – 25⁰C"
        "\nvegetable name in other languages:Pīṭrūṭ(Tamil),chukandar(Hindi),bīṟṟṟūṭṭ(Malayalam),Bīṭrūṭ(Telegu),Bīṭrūṭ(Kannada)")
                 ,fg="#03ffee",bg="#850909").pack()

 B14 = Button(object,text="BEET ROOT",fg="#03ffee",bg="#850909",command=beetroot,height=1,width=11)
 B14.pack()
 B14.place(x=200,y=10+60)

 def soyabean():
    lbl15= Label(object,text=(
        "vegetable_name=SOYA BEAN"
        "\nBotanical Name-Glycine max"
        "\nKingdom:    Plantae"
        "\nclade:Angiosperms,Eudicots,Rosids"
        "\nOrder: Fabales"
        "\nFamily: Fabaceae"
        "\nSubfamily: Faboideae"
        "\nGenus: Glycine"
        "\nSpecies: G.max"
        "\nDiseases affects this plant:Bacterial pustules,Phomopsis seed decay"
        "\nsoil type :The best soybean yields occur on well-drained, but not sandy soil"
        "\npH of soil :pH range of =<6.5"
        "\nOptimum temperature :temperature range of 10-15.5°C"
        "\nvegetable name in other languages:Cōyā pīṉ(Tamil),soyaabeen(Hindi),sēāyābīn(Malayalam),Sōyā bīn(Telegu),Sōyā huruḷi(Kannada)"),fg="#03ffee",bg="#700000").pack()

 B15 = Button(object,text="SOYA BEAN",fg="#03ffee",bg="#700000",command=soyabean,height=1,width=11)
 B15.pack()
 B15.place(x=200,y=40+60)

 def sweetpotato ():
    lbl16= Label(object,text=(
        "vegetable_name=SWEET POTATO"
        "\nBotanical Name-Ipomoea Batatus"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Asterids"
        "\nOrder:Solanales"
        "\nFamily:Convolvulaceae"
        "\nGenus:Ipomoea"
        "\nSpecies:I.batatas"
        "\nDiseases affects this plant:Hairy roots,Java black rot,Reniform"
        "\nsoil type :They must be planted in a well-drained, fine sandy loam soil"
        "\npH of soil :pH range of 5 to 7.5"
        "\nOptimum temperature :temperature range of 21 to 27°C"
        "\nvegetable name in other languages:Iṉippu uruḷaikkiḻaṅku(Tamil),shakarakand(Hindi),madhurakkiḻaṅṅ(Malayalam),Cilagaḍadumpa(Telegu),Iṉippu uruḷaikkiḻaṅku(Kannada)")
                 ,fg="#03ffee",bg="#6F634B").pack()

 B16 = Button(object,text="SWEET POTATO",fg="#03ffee",bg="#6F634B",command=sweetpotato,height=1,width=11)
 B16.pack()
 B16.place(x=200,y=70+60)

 def broadbean():
    lbl17= Label(object,text=(
        "vegetable_name=BROAD BEAN"
        "\nBotanical Name-Vicia faba"
        "\nKingdom:Plantae"
        "\nClade: Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder: Fabales"
        "\nFamily: Fabaceae"
        "\nTribe: Fabeae"
        "\nGenus:  Vicia"
        "\nSpecies: V.faba"
        "\nDiseases affects this plant:broad bran rust,chocolate spot"
        "\nsoil type : broad beans grows in full sun on rich, fertile, well-manured soil"
        "\npH of soil :pH range of 6-6.8"
        "\nOptimum temperature :temperature range of 4-12°C"
        "\nvegetable name in other languages:Pirāṭpīṉ(Tamil),broadbean(Hindi),brēāḍbīn(Malayalam),Brāḍbīn(Telegu),Brāḍbīn(Kannada)")
                 ,fg="#00b5a9",bg="#e9ffcc").pack()

 B17 = Button(object,text="BROAD BEAN",fg="#00b5a9",bg="#e9ffcc",command=broadbean,height=1,width=11)
 B17.pack()
 B17.place(x=200,y=100+60)

 def luffa():
    lbl18= Label(object,text=(
        "vegetable_name=LUFFA"
        "\nBotanical Name-Luffa aegyptiaca"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Eudicots,Rosids"
        "\nOrder:Cucurbitales"
        "\nFamily:Cucurbitaceae"
        "\nSubfamily:Cucurbitoideae"
        "\nTribe: Sicyoeae"
        "\nGenus:Luffa"
        "\nDiseases affects this plant:Downy mildew, powdery mildew, alternaria bligh"
        "\nsoil type :Luffas like full sun and a well-drained but moist soil, enriched with plenty of compost or well-rotted manure"
        "\npH of soil :pH range of 6.0–6.8"
        "\nOptimum temperature :temperature range of 25-30°C"
        "\nvegetable name in other languages:Luffa(Tamil),toree(Hindi),lapha(Malayalam),Laphphā(Telegu),Luphā(Kannada)"),fg="#03ffee",bg="#405920").pack()

 B18 = Button(object,text="LUFFA",fg="#03ffee",bg="#405920",command=luffa,height=1,width=11)
 B18.pack()
 B18.place(x=200,y=130+60)

 def onion():
    lbl19= Label(object,text=(
        "vegetable_name=ONION"
        "\nBotanical Name-Allium cepa" 
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Monocots"
        "\nOrder:Asparagales"
        "\nFamily:Amaryllidaceae"
        "\nSubfamily:Allioideae"
        "\nGenus:Allium"
        "\nSpecies:A.cepa"
        "\nDiseases affects this plant:Purple Blotch,Botrytis Leaf Blight,Downy Mildew"
        "\nsoil type :Onions can be grown on all types of soil such as sandy loam, silt loam and heavy clay soils"
        "\npH of soil :pH range of6.0 and 7.0"
        "\nOptimum temperature :temperature range of13-25°C"
        "\nvegetable name in other languages:Veṅkāyam(Tamil),pyaaj(Hindi),uḷḷi(Malayalam),Ullipāya(Telegu),Īruḷḷi(Kannada)")
                 ,fg="#03ffee",bg="#a82557").pack()

 B19 = Button(object,text="ONION",fg="#03ffee",bg="#a82557",command=onion,height=1,width=11)
 B19.pack()
 B19.place(x=200,y=160+60)

 def garlic():
    lbl20= Label(object,text=(
        "vegetable_name=GARLIC"
        "\nBotanical Name- Allium sativum"
        "\nKingdom:Plantae"
        "\nClade:Tracheophytes,Angiosperms,Monocots"
        "\nOrder:Asparagales"
        "\nFamily:Amaryllidaceae"
        "\nSubfamily:Allioideae"
        "\nGenus:Allium"
        "\nSpecies:A.sativum"
        "\nDiseases affects this plant:Botrytis Rot,Penicillium Decay,Downy Mildew"
        "\nsoil type :Garlic requires well drained loamy soils, rich in humus, with fairly good content of potash"
        "\npH of soil :pH range of6.0 and 7.0"
        "\nOptimum temperature :temperature range of12-24 °C"
        "\nvegetable name in other languages:Pūṇṭu(Tamil),lahasun(Hindi),veḷuttuḷḷi(Malayalam),Vellulli(Telegu),Beḷḷuḷḷi(Kannada)")
                 ,fg="#00b5a9",bg="#f2e9d2").pack()

 B20 = Button(object,text="GARLIC",fg="#00b5a9",bg="#f2e9d2",command=garlic,height=1,width=11)
 B20.pack()
 B20.place(x=200,y=190+60)

B01=Button(object,text="VEGATABLES",command=vegetables,height=13,width=39,fg="grey2",bg="Indianred")
B01.pack()

B01.place(x=10,y=10+60)


object.mainloop()
