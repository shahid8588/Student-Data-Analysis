# ============================================
#   Student Data Analysis System
#   Author: Shahid Khan
#   Tools: NumPy, Pandas, Matplotlib
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ============================================
# STEP 1 — CREATE DATASET
# ============================================

data = {
    "Name"   : ["Shahid", "Ali", "Sara", "Ahmad", "Darab",
                 "Fatima", "Usman", "Misha", "Bilal", "Sana"],
    "Roll_No": [101, 102, 103, 104, 105,
                106, 107, 108, 109, 110],
    "Age"    : [21, 20, 22, 21, 20,
                22, 21, 20, 23, 21],
    "Marks"  : [87, 45, 92, 78, 55,
                63, 81, 48, 74, 96],
    "Subject": ["AI"] * 10,
    "City"   : ["Haripur", "Lahore", "Karachi", "Peshawar", "Islamabad",
                 "Quetta", "Multan", "Faisalabad", "Rawalpindi", "Sialkot"]
}


df = pd.DataFrame(data)

print("=" * 55)
print("        STUDENT DATA ANALYSIS SYSTEM")
print("=" * 55)
print("\n--- Complete Dataset ---")
print(df.to_string(index=False))


# ============================================
# STEP 2 — PANDAS ANALYSIS
# ============================================

print("\n" + "=" * 55)
print("           PANDAS ANALYSIS")
print("=" * 55)


print("\n--- Students With Marks Above 75 ---")
above_75 = df[df["Marks"] > 75]
print(above_75[["Name", "Marks"]].to_string(index=False))


print("\n--- Students With Marks Below 50 ---")
below_50 = df[df["Marks"] < 50]
print(below_50[["Name", "Marks"]].to_string(index=False))


print("\n--- Basic Statistics ---")
print(f"Highest Marks : {df['Marks'].max()}")
print(f"Lowest Marks  : {df['Marks'].min()}")
print(f"Average Marks : {df['Marks'].mean():.2f}")
print(f"Total Students: {len(df)}")


# ============================================
# STEP 3 — NUMPY ANALYSIS
# ============================================

print("\n" + "=" * 55)
print("           NUMPY ANALYSIS")
print("=" * 55)

marks_array = np.array(df["Marks"])

print(f"Mean           : {np.mean(marks_array):.2f}")
print(f"Median         : {np.median(marks_array):.2f}")
print(f"Std Deviation  : {np.std(marks_array):.2f}")
print(f"Highest        : {np.max(marks_array)}")
print(f"Lowest         : {np.min(marks_array)}")

# Add 5 bonus marks
bonus_marks = marks_array + 5
print(f"\nOriginal Marks : {marks_array}")
print(f"After Bonus +5 : {bonus_marks}")


df["Bonus_Marks"] = bonus_marks


# ============================================
# STEP 4 — GRADE ASSIGNMENT
# ============================================

print("\n" + "=" * 55)
print("           GRADE ASSIGNMENT")
print("=" * 55)

conditions = [
    df["Marks"] >= 80,
    df["Marks"] >= 65,
    df["Marks"] >= 50,
    df["Marks"] < 50
]
grades = ["A", "B", "C", "F"]

df["Grade"] = np.select(conditions, grades, default="F")

print(df[["Name", "Marks", "Bonus_Marks", "Grade"]].to_string(index=False))


# ============================================
# STEP 5 — VISUALIZATION
# ============================================

# Create charts folder
if not os.path.exists("charts"):
    os.makedirs("charts")

# --- Chart 1 — Bar Chart ---
plt.figure(figsize=(12, 5))
colors = []
for mark in df["Marks"]:
    if mark >= 80:
        colors.append("green")
    elif mark >= 65:
        colors.append("blue")
    elif mark >= 50:
        colors.append("orange")
    else:
        colors.append("red")

plt.bar(df["Name"], df["Marks"], color=colors)

# Add values on top of bars
for i, mark in enumerate(df["Marks"]):
    plt.text(i, mark + 0.5, str(mark),
             ha="center", fontweight="bold")

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.ylim(0, 110)
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("charts/bar_chart.png")
plt.show()

# --- Chart 2 — Pie Chart ---
grade_counts = df["Grade"].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(grade_counts.values,
        labels=grade_counts.index,
        autopct="%1.1f%%",
        shadow=True,
        colors=["green", "blue", "orange", "red"])

plt.title("Grade Distribution")
plt.savefig("charts/pie_chart.png")
plt.show()

# --- Chart 3 — Line Chart ---
plt.figure(figsize=(12, 5))
plt.plot(df["Name"], df["Marks"],
         color="blue", marker="o",
         linewidth=2, linestyle="--",
         label="Original Marks")

plt.plot(df["Name"], df["Bonus_Marks"],
         color="green", marker="s",
         linewidth=2, linestyle="-",
         label="After Bonus")

plt.title("Marks Before and After Bonus")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/line_chart.png")
plt.show()


# ============================================
# STEP 6 — SAVE TO CSV FILE
# ============================================

df.to_csv("students.csv", index=False)
print("\n" + "=" * 55)
print("✅ Complete dataset saved to students.csv!")
print("✅ Charts saved in charts/ folder!")
print("✅ Analysis Complete!")
print("=" * 55)
