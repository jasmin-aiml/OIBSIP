def execute_health_index_calc():
    print("===================================================")
    print("         METRIC BODY MASS INDEX EVALUATOR          ")
    print("===================================================\n")
    
    try:
        input_mass_kg = float(input("Please specify body mass in kilograms (e.g., 70): "))
        input_height_m = float(input("Please specify physical height in meters (e.g., 1.75): "))
        
        if input_mass_kg <= 0 or input_height_m <= 0:
            print("❌ Input validation error: Values must be positive numbers higher than zero.")
            return
            
    except ValueError:
        print("❌ Data processing exception: Invalid numerical text input detected.")
        return

    computed_bmi = input_mass_kg / (input_height_m ** 2)
    print("\n---------------------------------------------------")
    print(f"📊 METRIC COMPUTATION ANALYSIS RESULTS")
    print(f"🎯 Calculated BMI Value: {computed_bmi:.2f}")
    
    if computed_bmi < 18.5:
        print("⚠️ Clinical Assessment: Underweight Category")
    elif 18.5 <= computed_bmi < 24.9:
        print("✅ Clinical Assessment: Normal/Healthy Weight Range")
    elif 25.0 <= computed_bmi < 29.9:
        print("⚠️ Clinical Assessment: Overweight Category")
    else:
        print("🚨 Clinical Assessment: Obese Category Classification")
    print("---------------------------------------------------")

if __name__ == "__main__":
    execute_health_index_calc()

