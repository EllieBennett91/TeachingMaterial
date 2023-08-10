import pandas as pd

df = pd.read_csv('SAA1lemmaandmetadupes_03042023.csv', sep=',')#when columns are separated with a comma, use '\t')

#turn into a dictionary
authordi = {"Sin-a[šared?]" : "Sin-ašared",
            'Mannu-[ki-Aššur-le’i]': "Mannu-ki-Aššur-le’i",
            '[Mannu-ki-Aššur-le’i]': 'Mannu-ki-Aššur-le’i',
            'Man[nu-ki-Aššur-le’i?]': 'Mannu-ki-Aššur-le’i',
            '[Nabu]-zer-ketti-lešir' : 'Nabu-zer-ketti-lešir',
            '[Hunni?]' : 'Hunni',
            'Samnuha-[belu-uṣur]': 'Samnuha-belu-uṣur',
            '[Samnuha-belu-uṣur]': 'Samnuha-belu-uṣur',
            '[Ilu-iq]bi': 'Ilu-iqbi',
            '[Ilu-iqbi]': 'Ilu-iqbi',
            '[Mitunu]': 'Mitunu',
            '[Šamaš-upahhir]': 'Šamaš-upahhir',
            'Ila[’i-Bel]': 'Ila’i-Bel',
        'Inurta-il[a’i]': 'Inurta-ila’i',
        '[Pan]-Aššur-lam[ur]': 'Pan-Aššur-lamur',
        'Pan-Aššur-[lamur]': 'Pan-Aššur-lamur',
        '[Ṭab-šar-Aššur?]': 'Ṭab-šar-Aššur',
        'Ṭab-šar-[Aššur]': 'Ṭab-šar-Aššur',
        '[Ṭab-šar-Aš]šur': 'Ṭab-šar-Aššur',
        '[Ṭab-šar-Aššur]': 'Ṭab-šar-Aššur',
        '[Ṭ]ab-šar-Aššur': 'Ṭab-šar-Aššur',
        '[Ṭab]-šar-Aššur': 'Ṭab-šar-Aššur',
        '[Kiṣir-Aššur]': 'Kiṣir-Aššur',
        'Išm[anni-Aššur]': 'Išmanni-Aššur',
        'Išmanni-[Aššur]': 'Išmanni-Aššur',
        '[Nabu-de’]iq': 'Nabu-de’iq',
        '[Nabu-de’iq]': 'Nabu-de’iq',
        'Na[bu-pašir]': 'Nabu-pašir',
        '(Nabu-pašir)': 'Nabu-pašir',
        'N[abu-pašir]': 'Nabu-pašir',
        '[Nabu-pašir]': 'Nabu-pašir',
        '[Senn]acherib': 'Sennacherib',
        '[Sennacherib]': 'Sennacherib',
        'S[ennacherib]': 'Sennacherib',
        '[Ašš]ur-bani': 'Aššur-bani',
        '[Aššur-bani]': 'Aššur-bani',
        '[the ki]ng': 'the king',
        '[the king]': 'the king',
        'the king': 'the king',
        'Aplaya, Šarru-lu-dari, Išmanni-Aššur': 'several',
        'Ṭab-ṣill-Ešarra, Na’di-ilu': 'several',
        'City rulers who are doing the king’s work in Milqia': 'several',
        'Nabu-belu-uṣur, Dinanu': 'several',
        'Recruitment officers [responsible for horse]s': 'several',
        '[Bel-liqbi]': 'Bel-liqbi',
        '[Bel-liqbi?]': 'Bel-liqbi',
        'Ṭab-[ṣill-Ešarra]': 'Ṭab-ṣill-Ešarra',
        '[Ṭab-ṣill-E]šarra': 'Ṭab-ṣill-Ešarra',
        '[Ṭab-ṣill-Ešarra]': 'Ṭab-ṣill-Ešarra',
        'Ṭab-ṣill-E[šarra]': 'Ṭab-ṣill-Ešarra',
        'Takl[ak-ana-Bel]': 'Taklak-ana-Bel',
        '[Taklak-ana-Bel]': 'Taklak-ana-Bel',
        '[Taklak-ana-Bel?]': 'Taklak-ana-Bel',
        'Taklak-[ana-Bel]': 'Taklak-ana-Bel',
        '[Amar-ili]': 'Amar-ili',
        '[Ama]r-ili': 'Amar-ili',
        'Ahu-lurš[i]': 'Ahu-lurši',
        'Samnu[ha-belu-uṣ]ur': 'Samnuha-belu-uṣur',
        '[Ina-šar-Bel-allak]': 'Ina-šar-Bel-allak',
        '[Nabu-pašir?], Nabu-dur-makie': 'several',
        '[Bel-duri]': 'Bel-duri',
        '[M]arduk-rem[anni]': 'Marduk-remanni'}

#turn into a dictionary
recipientdi = {"[the k]ing" : "the king",
            '"[...], [...], [...], Reman[ni-...], [...]"': "several",
            'the ki[ng]': 'the king',
            'Man[nu-ki-Aššur-le’i?]': 'Mannu-ki-Aššur-le’i',
            '100 b[rick masons]' : 'several',
            '[the ki]ng' : 'the king',
            'the crown prince': 'Sennacherib',
            '(the king)': 'the king',
            '[the kin]g of the lands': 'the king',
            '[the vizier]': 'the king',
            '[the king]': 'the king',

            'go[vernor] (of Calah)': 'Governor of Kalhu',
            'Aššur-šarru-u[ṣur]': 'Aššur-šarru-uṣur',
               }

#Run the directory on the authors column
cleanedauthors = df.replace({"ancient_author": authordi})
#Run the directory on the authors column
cleanedrecipients = cleanedauthors.replace({"ancient_recipient": recipientdi})

#saving the file
cleanedrecipients.to_csv('D:\DAA 2023\Python\SAA1_python_example.csv',index=False,sep=',')

