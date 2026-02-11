JUICE MACHINE PROJECT

### A simple Python program that simulates a vending machine. It tracks a balance, accepts specific coins, and gives change
How it Works
1.	The machine starts with an Amount Due of 100.
2.	It only accepts these coins: 5, 20, 25, 50.
3.	If you enter an invalid coin, the machine ignores it and asks again.
4.	Once you reach or exceed 100, the machine prints your Change Owed and exits.

## files

•	juice.py: The main program logic.
•	test_juice.py: Automated tests to make sure the machine counts correctly.

### How to run
Open your terminal:
```bash
cd juice 
Run any script using: 
python juice.py

We use pytest to test the machine without having to manually type numbers every time.

#### Running Tests
To run test on project.py,and to ensure that the application functions as intended execute the following command:
```bash
pytest test_juice.py
What the tests check:

•	Math: Does 50 + 50 equal 100?
•	Change: If you insert 50 + 25 + 50, do you get 25 change?
•	Validation: Does the machine ignore a "10" cent coin?

## Example Usage
Amount Due: 100
Insert a coin: 50
Amount due: 50
Insert a coin: 50
Change Owed: 0

## Note
If you want to stop the program before finishing your payment
•	Ctrl + C: This sends a "Keyboard Interrupt" to force-stop the script immediately.

#### Run Locally
clone the project

git clone https://github.com/wanji-cloudk/juice-machine.git

### Authers:
This project is developed by(https://www.github.com/wanji-cloudk)

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details.

### Contributing:
You are always welcome to contribute to this project and kindly submit a pull requst to any improment you've made,Your input can help make the gym management system even better for users.

### Conclusion:
Gym Management System is a comprehensive tool designed to simplify gym operations by incorporating features that focused on class bookings, real-time updates, and waitlist management, it supports both gym members and administrators effectively
