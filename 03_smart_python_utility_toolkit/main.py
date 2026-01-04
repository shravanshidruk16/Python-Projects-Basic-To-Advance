def digital_storage_converter():
    try:
        value = float(input("Enter storage value: "))
        if value <= 0:
            print("❌ Value must be greater than zero")
            return

        from_unit = input("Enter source unit (KB / MB / GB / TB): ").strip().upper()
        to_unit = input("Enter target unit (KB / MB / GB / TB): ").strip().upper()

        # Base unit: Bytes
        unit_table = {
            "KB": 1024,
            "MB": 1024 ** 2,
            "GB": 1024 ** 3,
            "TB": 1024 ** 4
        }

        if from_unit not in unit_table or to_unit not in unit_table:
            print("❌ Invalid unit entered")
            return

        bytes_value = value * unit_table[from_unit]
        converted_value = bytes_value / unit_table[to_unit]

        print(f"\n✅ {value} {from_unit} = {round(converted_value, 2)} {to_unit}")

    except ValueError:
        print("❌ Invalid numeric input")


def currency_converter():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("❌ Amount must be positive")
            return

        from_currency = input("Enter source currency (USD / INR / EUR): ").strip().upper()
        to_currency = input("Enter target currency (USD / INR / EUR): ").strip().upper()

        # NOTE : Approximate rates, hardcoded for learning
        exchange_rates = {
            "USD": 1.0,
            "INR": 90.0,
            "EUR": 0.85
        }

        if from_currency not in exchange_rates or to_currency not in exchange_rates:
            print("❌ Invalid currency")
            return

        amount_usd = amount / exchange_rates[from_currency]
        converted_amount = amount_usd * exchange_rates[to_currency]

        print(f"\n✅ {amount} {from_currency} = {round(converted_amount, 2)} {to_currency}")

    except ValueError:
        print("❌ Invalid numeric input")


def internet_speed_converter():
    try:
        value = float(input("Enter speed value: "))
        if value <= 0:
            print("❌ Speed must be positive")
            return

        from_unit = input("Enter source unit (Mbps / MBps / KBps): ").strip()
        to_unit = input("Enter target unit (Mbps / MBps / KBps): ").strip()

        # Base unit: MBps (Megabytes per second)
        unit_table = {
            "Mbps": 1 / 8,      # Megabits/sec → MBps
            "MBps": 1,          # Megabytes/sec → MBps
            "KBps": 1 / 1024    # Kilobytes/sec → MBps
        }

        if from_unit not in unit_table or to_unit not in unit_table:
            print("❌ Invalid unit (use Mbps / MBps / KBps exactly)")
            return

        # Convert source → MBps
        value_MBps = value * unit_table[from_unit]

        # Convert MBps → target
        converted_value = value_MBps / unit_table[to_unit]

        print(f"\n✅ {value} {from_unit} = {round(converted_value, 2)} {to_unit}")
        print("ℹ️ Note: 1 Byte = 8 bits")

    except ValueError:
        print("❌ Invalid numeric input")



def temperature_converter():
    try:
        value = float(input("Enter temperature value: "))
        from_unit = input("Enter source unit (C / F / K): ").strip().upper()
        to_unit = input("Enter target unit (C / F / K): ").strip().upper()

        # Convert to Celsius
        if from_unit == "C":
            temp_c = value
        elif from_unit == "F":
            temp_c = (value - 32) * 5 / 9
        elif from_unit == "K":
            temp_c = value - 273.15
        else:
            print("❌ Invalid unit")
            return

        # Convert from Celsius
        if to_unit == "C":
            result = temp_c
        elif to_unit == "F":
            result = (temp_c * 9 / 5) + 32
        elif to_unit == "K":
            result = temp_c + 273.15
        else:
            print("❌ Invalid unit")
            return

        print(f"\n✅ {value} {from_unit} = {round(result, 2)} {to_unit}")

    except ValueError:
        print("❌ Invalid numeric input")


def distance_converter():
    try:
        value = float(input("Enter distance value: "))
        if value <= 0:
            print("❌ Distance must be positive")
            return

        from_unit = input("Enter source unit (KM / M / MILES): ").strip().upper()
        to_unit = input("Enter target unit (KM / M / MILES): ").strip().upper()

        # Base unit: KM
        unit_table = {
            "KM": 1,
            "M": 0.001,
            "MILES": 1.609
        }

        if from_unit not in unit_table or to_unit not in unit_table:
            print("❌ Invalid unit")
            return

        km_value = value * unit_table[from_unit]
        converted_value = km_value / unit_table[to_unit]

        print(f"\n✅ {value} {from_unit} = {round(converted_value, 3)} {to_unit}")

    except ValueError:
        print("❌ Invalid numeric input")


def weight_converter():
    try:
        value = float(input("Enter weight value: "))
        if value <= 0:
            print("❌ Weight must be positive")
            return

        from_unit = input("Enter source unit (KG / G / LB): ").strip().upper()
        to_unit = input("Enter target unit (KG / G / LB): ").strip().upper()

        # Base unit: KG
        unit_table = {
            "KG": 1,
            "G": 0.001,
            "LB": 0.453592
        }

        if from_unit not in unit_table or to_unit not in unit_table:
            print("❌ Invalid unit")
            return

        kg_value = value * unit_table[from_unit]
        converted_value = kg_value / unit_table[to_unit]

        print(f"\n✅ {value} {from_unit} = {round(converted_value, 3)} {to_unit}")

    except ValueError:
        print("❌ Invalid numeric input")


def electricity_bill_estimator():
    try:
        units = float(input("Enter units consumed (kWh): "))
        rate = float(input("Enter cost per unit: "))

        if units < 0 or rate < 0:
            print("❌ Values must be non-negative")
            return

        total_bill = units * rate
        print(f"\n✅ Total Electricity Bill = ₹{round(total_bill, 2)}")

    except ValueError:
        print("❌ Invalid numeric input")


def data_transfer_time_estimator():
    try:
        file_size_mb = float(input("Enter file size (MB): "))
        speed_mbps = float(input("Enter internet speed (Mbps): "))

        if file_size_mb <= 0 or speed_mbps <= 0:
            print("❌ Values must be positive")
            return

        speed_MBps = speed_mbps / 8
        total_seconds = file_size_mb / speed_MBps

        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        seconds = int(total_seconds % 60)

        print(f"\n✅ Estimated Time: {hours}h {minutes}m {seconds}s")

    except ValueError:
        print("❌ Invalid numeric input")


def salary_ctc_converter():
    try:
        ctc_lpa = float(input("Enter CTC (in LPA): "))
        tax_percent = float(input("Enter income tax percentage: "))

        if ctc_lpa <= 0 or tax_percent < 0:
            print("❌ Invalid values")
            return

        annual_ctc = ctc_lpa * 100000

        # Assumptions
        basic = 0.40 * annual_ctc
        pf = 0.12 * basic
        professional_tax = 200 * 12

        taxable_income = annual_ctc - pf
        income_tax = (tax_percent / 100) * taxable_income

        total_deductions = pf + professional_tax + income_tax
        annual_inhand = annual_ctc - total_deductions
        monthly_inhand = annual_inhand / 12

        print("\n✅ CTC BREAKDOWN")
        print(f"Annual CTC            : ₹{round(annual_ctc, 2)}")
        print(f"Basic Salary (40%)    : ₹{round(basic, 2)}")
        print(f"PF (12% of Basic)     : ₹{round(pf, 2)}")
        print(f"Professional Tax      : ₹{professional_tax}")
        print(f"Income Tax            : ₹{round(income_tax, 2)}")
        print("-" * 40)
        print(f"Annual In-Hand        : ₹{round(annual_inhand, 2)}")
        print(f"Monthly In-Hand       : ₹{round(monthly_inhand, 2)}")
        print("\n")

    except ValueError:
        print("❌ Invalid numeric input")


def fuel_cost_converter():
    try:
        distance = float(input("Enter distance (km): "))
        mileage = float(input("Enter mileage (km/l): "))
        fuel_price = float(input("Enter fuel price per litre: "))

        if distance <= 0 or mileage <= 0 or fuel_price <= 0:
            print("❌ Values must be positive")
            return

        fuel_needed = distance / mileage
        total_cost = fuel_needed * fuel_price
        cost_per_km = total_cost / distance

        print("\n✅ Fuel Analysis")
        print(f"Fuel Required : {round(fuel_needed, 2)} litres")
        print(f"Total Cost    : ₹{round(total_cost, 2)}")
        print(f"Cost per Km   : ₹{round(cost_per_km, 2)}")

    except ValueError:
        print("❌ Invalid numeric input")



if __name__ == "__main__":
    while True:
        print("\n" + "*" * 40)
        print("   Welcome to Smart Python Utility Toolkit")
        print("*" * 40)
        print("""1. Digital Storage Converter\n2. Currency Converter\n3. Internet Speed Converter\n4. Temperature Converter\n5. Distance Converter\n6. Weight Converter\n7. Electricity Bill Estimator\n8. Data Transfer Time Estimator\n9. CTC to In-Hand Salary Converter\n10. Fuel Cost Estimator\n11. Quit""")
        print("\n")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Please enter a valid number")
            continue

        match choice:
            case 1: digital_storage_converter()
            case 2: currency_converter()
            case 3: internet_speed_converter()
            case 4: temperature_converter()
            case 5: distance_converter()
            case 6: weight_converter()
            case 7: electricity_bill_estimator()
            case 8: data_transfer_time_estimator()
            case 9: salary_ctc_converter()
            case 10: fuel_cost_converter()
            case 11:
                print("👋 Thanks for using my SMART PYTHON UTILITY TOOLKIT. Goodbye!")
                break
            case _:
                print("❌ Invalid menu option")
