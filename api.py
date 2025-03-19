import time
from colorama import Fore, Style
import pyfiglet

# تعريف الألوان
Z = Fore.LIGHTRED_EX  # أحمر
F = Fore.LIGHTGREEN_EX  # أخضر
B = Fore.LIGHTCYAN_EX  # سماوي
C = Fore.LIGHTYELLOW_EX  # أصفر

# المفتاح الصحيح
CORRECT_KEY = "mzdk97558fjiocxdhvc4588520bbg"  # عدل هذا بالمفتاح الذي تريده

# طلب المفتاح من المستخدم
user_key = input("   Enter the key:")
if user_key != CORRECT_KEY:
    print(f"The key is wrong ❌")
    exit()

print('''
░█████╗░██╗░░██╗░█████╗░██████╗░░██████╗░███████╗
██╔══██╗██║░░██║██╔══██╗██╔══██╗██╔════╝░██╔════╝
██║░░╚═╝███████║███████║██████╔╝██║░░██╗░█████╗░░
██║░░██╗██╔══██║██╔══██║██╔══██╗██║░░╚██╗██╔══╝░░
╚█████╔╝██║░░██║██║░░██║██║░░██║╚██████╔╝███████╗
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝''')
print('''
██╗░░██╗░░██╗░░██╗░░░░███╗░░██████╗░░███████╗
╚██╗░╚██╗░╚██╗░╚██╗░░████║░░╚════██╗██╔██╔══╝
░╚██╗░╚██╗░╚██╗░╚██╗██╔██║░░░█████╔╝╚██████╗░
░██╔╝░██╔╝░██╔╝░██╔╝╚═╝██║░░░╚═══██╗░╚═██╔██╗
██╔╝░██╔╝░██╔╝░██╔╝░███████╗██████╔╝███████╔╝
╚═╝░░╚═╝░░╚═╝░░╚═╝░░╚══════╝╚═════╝░╚══════╝░''')

# القوائم المرجعية
valid_card = '4400665280532431|11|2027|195'
done_buy_cards = ['5392254658087620|05|2028|622', valid_card]
insufficient_cards = ['5502541000007075|04|2024|044', '5129915199204128|02|2026|773']

# الإحصائيات
success_count = 0
insufficient_count = 0
declined_count = 0

# معالجة الملف
file_name = input(f"\n{B}[+] {C}أدخل اسم الملف: {F}")
with open(file_name, 'r') as file:
    cards = file.readlines()

print(f"\n{Fore.CYAN}{'┌' + '─'*45 + '┐'}")

for idx, card in enumerate(cards, 1):
    cc = card.strip().replace('/', '|').replace(':', '|')
    cc_parts = cc.split('|')
    
    # تنسيق البطاقة
    formatted_cc = f"{Fore.WHITE}{cc_parts[0]}|{cc_parts[1]}|{cc_parts[2]}|{Fore.LIGHTBLUE_EX}{cc_parts[3]}"
    
    time.sleep(0)
    
    # فحص البطاقة
    if cc == valid_card:
        status = f"{Fore.LIGHTGREEN_EX}✅ Charged 13$"
        success_count += 1
    elif cc in done_buy_cards:
        status = f"{Fore.LIGHTGREEN_EX}✓ Approved"
        success_count += 1
    elif cc in insufficient_cards:
        status = f"{Fore.LIGHTGREEN_EX}🔥 Insufficient funds"
        insufficient_count += 1
    else:
        status = f"{Fore.LIGHTRED_EX}❌ Declined"
        declined_count += 1
    
    # عرض النتيجة
    print(f"{Fore.CYAN}│ {formatted_cc:<35} {status} │")
    print(f"{Fore.CYAN}├{'─'*45}┤")

# النتائج النهائية
total = len(cards)
print(f"{Fore.CYAN}└{'─'*45}┘")

# عرض الإحصائيات في مربع منظم
print(f"\n{Fore.MAGENTA}{'═'*45}")
print(f"{Fore.MAGENTA}║{Fore.CYAN}         📊  النتائج النهائية 📊          {Fore.MAGENTA}║")
print(f"{Fore.MAGENTA}{'═'*45}")
print(f"{Fore.MAGENTA}║ {Fore.GREEN}✅ Charged: {success_count:<30} {Fore.MAGENTA}║")
print(f"{Fore.MAGENTA}║ {Fore.YELLOW}🔥 Insufficient Funds: {insufficient_count:<19} {Fore.MAGENTA} ║")
print(f"{Fore.MAGENTA}║ {Fore.RED}❌ Declined: {declined_count:<27} {Fore.MAGENTA}  ║")
print(f"{Fore.MAGENTA}║ {Fore.CYAN}📌 Total Checked: {total:<24} {Fore.MAGENTA} ║")
print(f"{Fore.MAGENTA}{'═'*45}{Style.RESET_ALL}")
