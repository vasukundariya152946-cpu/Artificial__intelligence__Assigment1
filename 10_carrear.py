
print("======================================")
print(" CAREER GUIDANCE SYSTEM")
print("======================================")

print("Answer the following questions with yes or no.\n")

C = input("Do you like coding? : ").lower().strip()
M = input("Do you like mathematics? : ").lower().strip()
B = input("Do you like biology? : ").lower().strip()
D = input("Do you like drawing? : ").lower().strip()

print("\n============ Career Suggestion =============")

if C == 'no' and M == 'no' and B == 'no' and D == 'no':
    print("Explore your interests and career options further.")

elif C == 'no' and M == 'no' and B == 'no' and D == 'yes':
    print("Graphic Designer / Animator.")

elif C == 'no' and M == 'no' and B == 'yes' and D == 'no':
    print("Pharmacist / Nurse.")

elif C == 'no' and M == 'no' and B == 'yes' and D == 'yes':
    print("Medical Illustrator / Healthcare Educator.")

elif C == 'no' and M == 'yes' and B == 'no' and D == 'no':
    print("Engineer / Data Analyst.")

elif C == 'no' and M == 'yes' and B == 'no' and D == 'yes':
    print("Architect.")

elif C == 'no' and M == 'yes' and B == 'yes' and D == 'no':
    print("Doctor.")

elif C == 'no' and M == 'yes' and B == 'yes' and D == 'yes':
    print("Medical Illustrator / Biomedical Designer.")

elif C == 'yes' and M == 'no' and B == 'no' and D == 'no':
    print("Programmer / Web Developer.")

elif C == 'yes' and M == 'no' and B == 'no' and D == 'yes':
    print("Web Designer / UI/UX Designer.")

elif C == 'yes' and M == 'no' and B == 'yes' and D == 'no':
    print("Health App Developer.")

elif C == 'yes' and M == 'no' and B == 'yes' and D == 'yes':
    print("Medical Illustrator.")

elif C == 'yes' and M == 'yes' and B == 'no' and D == 'no':
    print("Software Engineer / Computer Scientist.")

elif C == 'yes' and M == 'yes' and B == 'no' and D == 'yes':
    print("Game Developer / UI Engineer.")

elif C == 'yes' and M == 'yes' and B == 'yes' and D == 'no':
    print("Bioinformatics Scientist.")

elif C == 'yes' and M == 'yes' and B == 'yes' and D == 'yes':
    print("Biomedical Software Engineer / Medical Technology Specialist.")

else:
    print("Invalid input! Please enter only 'yes' or 'no'.")
#     ======================================
#  CAREER GUIDANCE SYSTEM
# ======================================
# Answer the following questions with yes or no.

# Do you like coding? : yes 
# Do you like mathematics? : no
# Do you like biology? : yes
# Do you like drawing? : no

# ============ Career Suggestion =============
# Health App Developer.