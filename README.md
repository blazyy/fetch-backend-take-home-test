# Fetch Coding Exercise Submission - Software Engineering Internship

## Info

* Name - Faaez Razeen Nizamudeen

## Program Info 

- Required Language and Version: Python 3.x
- Install the Python language for your system using the [official python website.](https://www.python.org/downloads/)
- Install the `pandas` library by running `pip3 install pandas` or `pip install pandas`. For more granular instructions, visit the [official pandas website.](https://pandas.pydata.org/docs/getting_started/install.html#installing-from-pypi)
- To run the program, open the Command Prompt (Windows) or Terminal (MacOS), navigate to the directory the file is in, make sure the `transactions.csv` file exists in the same directory, and then run `python3 mycode.py 5000`.


## Program Explanation

As per the exercise requirements, the program does the following:
1) Reads the `transactions.csv` file into a `pandas` dataframe.
2) Converts the `timestamp` column to type `datetime64` using the `pd.to_datetime()` function.
3) Sorts the dataframe by the `timestamp` column.
4) Groups the dataframe by the `payer`'s name, with a sum aggregation function. This result is stored into a dictionary called `payer_points`.
5) For each row in the dataframe:
    * i) If the current `payer`'s points is positive:
        * a) Decrements the value in `payer_points` for that respective `payer` by the smaller amount between `points` and the current `payer`'s points. We call this `amount_to_decrement`.
        * b) Decrements the `points` variable by `amount_to_decrement`.
    * ii) Else if (the current `payer`'s point is negative):
        * a) Increments the `points` variable by the absolute value of the current `payer`'s points.
        * b) Increases the value in `payer_points` for the current `payer` by the absolute value of * the current `payer`'s points.