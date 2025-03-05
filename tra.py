translator={
    'dependent':'залежний',
    'independent':'незалежний',
    'confident':'впевнений у собі',
    'boring':'нудно',
    'advert':'оголошення',
    'disappointed':'розчарований',
    'happy':'щасливий',
    'lottery':'лотерея',
    'casino':'казино',
    'map':'карта',
}
dac=input('Напишіть слово яке вас зацікавило і ми його перекладемо:\n').lower()
if dac in translator:
    print(f'Слово {dac} означає-{translator.get(dac)}')
else:
    print("Нажаль ми не знаємо такого слова")
