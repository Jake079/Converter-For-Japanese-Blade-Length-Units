from decimal import Decimal, getcontext, InvalidOperation
# Higher precision decimal arithmetic + error handling

# Set the precision to X significant digits (default is 28)
getcontext().prec = 28

# 1尺(しゃく/Shaku) = 30.3022センチ(cm)
JAPANESE_UNIT_SHAKU = Decimal('30.3022')

# 1寸(すん/Sun) = 3.03022センチ(cm)
JAPANESE_UNIT_SUN = Decimal('3.03022')

# 1分(ぶ/Bu) = 0.303022センチ(cm)
JAPANESE_UNIT_BU = Decimal('0.303022')

# 単位 Constant Strings
SENCHI = "センチ(cm)"
SHAKU = "尺(Shaku)"
SUN = "寸(Sun)"
BU = "分(Bu)"

# 単位の自動換算 Converter Function センチ(cm) → 尺(Shaku)
def nagasa_convert_to_shaku() -> None:
    """
    刀の長さを入力させ、和式の単位に換算する
    
    Prompts user for blade length in cm and converts it to traditional Japanese unit.

    """
    nagasa_input_value_cm = input(f"\n刀の長さ Blade Length {SENCHI}: ")
    try:
        nagasa_shaku, nagasa_shaku_remain = divmod(
            Decimal(nagasa_input_value_cm), JAPANESE_UNIT_SHAKU)
        nagasa_sun, nagasa_sun_remain = divmod(
            nagasa_shaku_remain, JAPANESE_UNIT_SUN)
        nagasa_bu = nagasa_sun_remain / JAPANESE_UNIT_BU
        print(f"\n〄 {nagasa_input_value_cm}cm = {int(nagasa_shaku)}{SHAKU} {int(nagasa_sun)}{SUN} {nagasa_bu:.2f}{BU}")
    except InvalidOperation:
        print("\n不正な数値 Please enter a valid number")

# 単位の自動換算 Converter Function 尺(Shaku) → センチ(cm)
def nagasa_convert_to_cm() -> None:
    """
    和式単位の尺．寸．分は順に別々で入力させ、刀の長さ(センチ)に換算する。
    
    Prompts user for blade length in traditional Japanese unit and converts it to cm.
    Must enter 尺(Shaku), 寸(Sun), and 分(Bu) separately in order.
    """
    print(
        f"\n刀の長さを尺．寸．分の順に入力する\nEnter the blade length in the order of {SHAKU}, {SUN} and {BU}")
    nagasa_input_value_shaku = input(f"Enter {SHAKU}: ")
    nagasa_input_value_sun = input(f"Enter {SUN}: ")
    nagasa_input_value_bu = input(f"Enter {BU}: ")
    try:
        nagasa_shaku_total = Decimal(
            nagasa_input_value_shaku) * JAPANESE_UNIT_SHAKU
        nagasa_sun_total = Decimal(
            nagasa_input_value_sun) * JAPANESE_UNIT_SUN
        nagasa_bu_total = Decimal(
            nagasa_input_value_bu) * JAPANESE_UNIT_BU
        nagasa_total_cm = nagasa_shaku_total + nagasa_sun_total + nagasa_bu_total
        print(f"\n{nagasa_input_value_shaku}{SHAKU} {nagasa_input_value_sun}{SUN} {nagasa_input_value_bu}{BU} = {nagasa_total_cm:.2f}cm")
    except InvalidOperation:
        print("\n不正な数値 Please enter a valid number")

# 換算を選ぶ Choose Converter Function
def choose_converter() -> None:
    """
    変換を選択させるか、終了させる。
    
    Prompt user to choose between two conversion options or end the program.
    """
    while True:
        converter_choice = input(
            f"\n> 入力して選択 Enter to select:\n'1' [{SENCHI} → {SHAKU}]\n'2' [{SHAKU} → {SENCHI}]\n'end' [プログラムを終了 End the program]\n\n> ")
        if converter_choice.lower() == "end":
            print("\n完 END")
            break
        elif converter_choice == "1":
            nagasa_convert_to_shaku()
        elif converter_choice == "2":
            nagasa_convert_to_cm()
        else:
            print("\n無効な操作 Please enter a valid choice")


if __name__ == '__main__':
    choose_converter()
