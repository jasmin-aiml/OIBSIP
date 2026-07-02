# Unique Workspace Implementation
# Evaluation Tracker Identity Module

def execute_health_index_calc():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("     METRIC BODY MASS EVALUATOR v1.0     ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    
    try:
        input_mass_kg = input("Please specify body mass in kilograms: ").strip()
        input_stature_m = input("Please specify total height in meters: ").strip()
        
        body_mass = float(input_mass_kg)
        body_stature = float(input_stature_m)
        
        if body_mass <= 0 or body_stature <= 0:
            print("\n[CRITICAL ERROR]: Entry figures must be non-zero positive numbers.")
            return
            
        computed_score = body_mass / (body_stature ** 2)
        
        if computed_score < 18.5:
            diagnostic_label = "Below standard weight guidelines"
        elif 18.5 <= computed_score < 24.9:
            diagnostic_label = "Optimal standard fitness range"
        elif 25.0 <= computed_score < 29.9:
            diagnostic_label = "Exceeds standard weight parameters"
        else:
            diagnostic_label = "Clinical obesity threshold detected"
            
        print("\n=========================================")
        print(f" Calculated Metric Value : {computed_score:.2f}")
        print(f" Fitness Classification  : {diagnostic_label}")
        print("=========================================")
        
    except ValueError:
        print("\n[FAILED PROCESSING]: Input format rejected. Numeric entries only.")

if __name__ == "__main__":
    execute_health_index_calc()
