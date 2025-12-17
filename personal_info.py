# Personal Information Manager
# Author: Shravan R L
# Description: Beginner Python project to store and display personal information

print("=" * 35)
print("      PERSONAL INFORMATION")
print("=" * 35)

name = "Shravan R L"
age = 20
city = "Bangalore"
hobby = "Exploring technology"

favorite_food = input("Enter your favorite food: ").strip()
if favorite_food == "":
    favorite_food = "Not provided"

favorite_color = input("Enter your favorite color: ").strip()
if favorite_color == "":
    favorite_color = "Not provided"

age_in_months = age * 12

print("=" * 35)
print(f"Name: {name}")
print(f"Age: {age} ({age_in_months} months old)")
print(f"City: {city}")
print(f"Hobby: {hobby}")
print()
print(f"Favorite Food: {favorite_food}")
print(f"Favorite Color: {favorite_color}")
print("=" * 35)
print("Thank you for using the program!")
