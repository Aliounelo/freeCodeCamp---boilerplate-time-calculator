# Time Calculator

# Live demo : https://replit.com/@aliounelo/freeCodeCamp-boilerplate-time-calculator#main.py

Write a function named add_time that takes in two required parameters and one optional parameter:

   + a start time in the 12-hour clock format (ending in AM or PM)
   + a duration time that indicates the number of hours and minutes
   + (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

![image](https://user-images.githubusercontent.com/53930501/176225868-5d765658-128e-4f08-81bb-46dbe6b4ca4f.png)


Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

<h1><b>Development</b></h1>

Write your code in time_calculator.py. For development, you can use main.py to test your time_calculator() function. Click the "run" button and main.py will run.
