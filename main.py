import tkinter
import re

def is_number(text):
    return bool(re.match(r"^\d+$", text))

def click_button():
    global BMI_label
    global BMI_result_label
    global BMI_scale_label
    global BMI_scale_result_label
    global BMI_error_label1
    global BMI_error_label2

    user_input1 = my_entry1.get()
    user_input2 = my_entry2.get()

    if not is_number(user_input1):
        # Update the error label
        BMI_error_label1.config(text="Please enter a number in the weight field.", fg="red")
    elif not is_number(user_input2):
        # Update the error label
        BMI_error_label2.config(text="Please enter a number in the height field.", fg="red")
    else:
        BMI = (int(user_input1) / int(user_input2) ** 2) * 10000

        # Add the BMI scale
        bmi_scale = "Underweight"
        if BMI >= 18.5 and BMI < 25:
            bmi_scale = "Normal"
        elif BMI >= 25 and BMI < 30:
            bmi_scale = "Overweight"
        elif BMI >= 30:
            bmi_scale = "Obese"

        # Update the BMI and BMI scale labels
        BMI_result_label.config(text=str(BMI)[:5])
        BMI_scale_result_label.config(text=bmi_scale)

        # Clear the error labels
        BMI_error_label1.config(text="")
        BMI_error_label2.config(text="")

window = tkinter.Tk()
window.title("BMI Calculator")
window.minsize(width=450,height=300)
window.config(padx=10,pady=10)


# The first label
my_label = tkinter.Label(text="Enter Your Weight(kg)",font=("Arial",15,"bold"))
my_label.pack()


# The entry field for weight
my_entry1 = tkinter.Entry(width=10)
my_entry1.pack()


# The second label
my_label2 = tkinter.Label(text="Enter Your Height(cm)",font=("Arial",15,"bold"))
my_label2.pack()


# The entry field for height
my_entry2 = tkinter.Entry(width=10)
my_entry2.pack()

#For Space Label
my_label3 = tkinter.Label(text="",font=("Arial",5,"bold"))
my_label3.pack()


# The button
my_button = tkinter.Button(text="Calculate",fg="green",font=("Arial",15,"bold"), command=click_button)
my_button.pack()


# Create BMI labels
BMI_label = tkinter.Label(text="BMI:", font=("Arial", 15, "bold"))
BMI_label.pack()

BMI_result_label = tkinter.Label(text=str(0)[:5], font=("Arial", 15, "bold"))
BMI_result_label.pack()

BMI_scale_label = tkinter.Label(text="BMI Scale:", font=("Arial", 15, "bold"))
BMI_scale_label.pack()

BMI_scale_result_label = tkinter.Label(text="...", font=("Arial", 15, "bold"))
BMI_scale_result_label.pack()


# Create error labels
BMI_error_label1 = tkinter.Label(text="", font=("Arial", 15, "bold"))
BMI_error_label1.pack()

BMI_error_label2 = tkinter.Label(text="", font=("Arial", 15, "bold"))
BMI_error_label2.pack()




window.mainloop()
