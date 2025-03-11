print("\t\t\t\t\tWELCOME TO THE ADVANCE BMI CALCULATOR \n\n\n\n")
# Offer Measurement Conversions
Offer_Conversions = input("Would you like to convert your imperial units to metric? (yes /no):\n ")
if Offer_Conversions.lower() in ["yes", "y"]:
    Imperial_Weight = input("\nWhat is your weight in pounds?: ")
    Imperial_Height = input("\nWhat is your height in feet (decimals)?: ")
    Imperial_Weight = float(Imperial_Weight)
    Imperial_Height = float(Imperial_Height)
    Metric_Converted_Weight = Imperial_Weight * 2.205
    Metric_Converted_Height = Imperial_Height * 30.48
    Metric_Converted_Weight = str(Metric_Converted_Weight)
    Metric_Converted_Height = str(Metric_Converted_Height)
    print("\nYour metric weight is " + Metric_Converted_Weight + " kg, please note this for the next stage.")
    print("\n")
    print("\nYour metric height is " + Metric_Converted_Height + " cm, please note this for the next stage.")
    print("--")
elif Offer_Conversions.lower() in ["no", "n"]:
    # Proceed without conversion...
    print("--")
    # Data Collection
    Weight = input("\nPut in your weight in KG: ")
    Height = input("\nPut in your height in CM: ")
    # BMI Formula Calculation
    Weight = float(Weight)
    Height = float(Height)
    Height_Squared = Height * Height
    BMI_Formula_Assisted = Weight / Height_Squared
    BMI_Formula_Completed = BMI_Formula_Assisted * 10000
    # Health Chart Display
    BMI_Formula_Completed = str(BMI_Formula_Completed)
    print("\nYou have a BMI score of " + BMI_Formula_Completed + ".\n\n")
    BMI_Formula_Completed = float(BMI_Formula_Completed)
    if BMI_Formula_Completed < 18.5:
        print(" YOU ARE UNDERWEIGHT ")
        print("""
        1. OVERVIEW
        UNDERWEIGHT:
        Underweight Complication is a term that indicates an adult’s thinness and weight loss below
        the normal and healthy weight range.
        2. RANGE
        BMI RANGE FOR UNDERWEIGHT- A person is considered underweight when the BMIis less than 18.5.
        A. BMI YOU REQUIRE FOR GOOD HEALTH - consider gaining weight to bring your BMI to between 20
        and 25.")
        3.
        SYMPTOMS
        A.Dizziness or fatigue from anemia
        B.Fragile bones
        C.Hair loss
        D.Irregular menstrual periods or problems getting pregnant
        E.Poor growth and development, especially in children who are underweight
        F.Weak immune system
        4. HEALTH RISKS RELATED ISSUSES DUE TO UNDERWEIGHT:
        These risks include:

        
        A.Malnutrition, vitamin deficiencies, or anemia
        B.Osteoporosis from too little vitamin D and calcium
        C.Decreased immune function
        D.Increased risk for complications from surgery
        E.Fertility issues caused by irregular menstrual cycles
        F.Growth and development issues, especially in children and teenagers
        5. PREVENTIVE MEASURES
        A.Add healthy calories
        B.Go nutrient dense
        C.Snack away
        D.Eat mini meals
        E.Bulk up
        """)
    elif BMI_Formula_Completed <= 24.9:
        print(" YOU ARE PERFECTLY HEALTHY ")
        print("""

        1. OVERVIEW
        HEALTHY WEIGHT:
        A healthy body weight is one that can be maintained without constant dieting
        or without restricted food intake.
        A healthy body weight is a weight that can be accepted by YOU.
        Yes, YOU are in charge of your body and therefore, YOU need to feel good in your body.
        2.
        RANGE
        BMI RANGE FOR HEALTHY PERSON- A person is considered HEALTHY when their BMI is between 18.5 and
        24.9
        25
        A. KEEP YOUR BMI AT CONSTANT RATE(YOU ARE DOING GOOD)
        3.
        Benefits of Maintaining a Healthy Body Weight
        A. Discomfort Relief.
        B. Healthier Heart.
        C. Lower Risk of Diabetes.
        D. Cancer Avoidance.
        E. Prevent Osteoarthritis.
        4. PREVENTIVE MEASURES
        1.Stick to your diet
        2.Exercise daily
        3.Eat high protein diet
        4.Do meditation
        5. SPECIAL NOTE
        YOU ARE DOING GOOD. BUT YOU HAVE TO MAINTAIN IT . DON'T THINK THAT NOW YOU
        ARE HEALTHY SO YOU CAN EAT ANYTHING OR WILL NOT EXERCISE.
        BEING HEALTHY IS EASY BUT MAINTAING A HEALTHY WEIGHT FOR LIFE TIME IS DIFFICULT
        """)
    elif BMI_Formula_Completed <= 29.9:
        print(" YOU ARE OVERWEIGHT ")
        print("""
        1. OVERVIEW:
        OVERWEIGHT -
        A condition where the person weighs more than what is considered normal for that height,age
        and sex.


        
        2. RANGE
        BMI RANGE FOR OVERWEIGHT- A person is considered overweight when their BMI is between 25 and
        29.9.
        A. BMI YOU REQUIRE FOR GOOD HEALTH - between 18.5 and 24.9 or else you may be at risks.")
        3. SYMPTOMS
        A.Excess body fat accumulation (particularly around the waist)
        B.Shortness of breath
        C.Sweating (more than usual)
        D.Snoring
        E.Trouble sleeping
        F.Skin problems (from moisture accumulating in the folds of skin)
        G.Inability to perform simple physical tasks
        H.Fatigue (from mild to extreme)
        I.Pain (commonly in the back and joints)
        3. HEALTH RISKS RELATED ISSUSES DUE TO OVERWEIGHT:
        4.
        A. All-causes of death (mortality)
        B.High blood pressure (Hypertension)
        C.igh LDL cholesterol, low HDL cholesteroL
        D.Type 2 diabetes
        E.Coronary heart disease
        F.Stroke
        G.Gallbladder disease
        H.Osteoarthritis
        I.Sleep apnea and breathing problems
        K.Many types of cancerexternal icon
        L.Low quality of life
        M.Mental illness such as clinical depression
        N.Body pain
        5.
        PREVENTIVE MEASURE
        27
        A.Exercise regularly
        B.Eat a well-balanced diet
        C.Maintain a healthy body weight
        D.Limit unhealthy foods
        E.Improve sleep routine and reduce the stress
    """)
    elif BMI_Formula_Completed >= 30.0:
        print(" YOU ARE OBESE ")
        print("""
        1. OVERVIEW:
        OBESITY- condition characterized by abnormal or excessive fat accumulation.
        A.How common is condition?
        Very common (More than 3 million cases per year in US)
        B.Is condition treatable?
        .Treatable by a medical professional
        C.Does diagnosis require lab test or imaging?
        .Doesn't require lab test or imaging
        D.Time taken for recovery
        Can last several years or be lifelong
        E.Condition Highlight
        Family history may increase likelihood for some types
        2. RANGE
        BMI range for obese- A person is considered obese when BMI is over 30.
        A. BMI YOU REQUIRE FOR GOOD HEALTH - between 18.5 and 24.9 or else you may be at risks.")
        28
        3.
        SYMPTOMS
        The symptoms of obesity include:
        A.Above average body weight
        B.Trouble sleeping
        C.Sleep apnea- a condition in which breathing is irregular and periodically stops during Sleep
        D.Varicose veins
        E.Skin problems caused by moisture that accumulates in the folds of your Skin
        F.Gallstones
        G.Osteoarthritis in Weight-bearing joints, especially the knees
        4. HEALTH RISKS RELATED ISSUSES DUE TO OBESITY:
        A.Heart disease and stroke
        B.High blood pressure
        C.Diabetes
        D.Some cancers
        E.Gallbladder disease and gallstones
        F.Osteoarthritis
        G.Gout
        H.Breathing problems, such as sleep apnea
        5. PREVENTIVE MEASURES:
        A.Exercise regularly
        B.Eat a well-balanced diet
        C.Maintain a healthy body weight
        D.Limit unhealthy foods
        E.Improve sleep routine and reduce the stress
        """)