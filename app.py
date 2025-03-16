import time
import streamlit as st
import threading

class MoneyMakerMachine:
    def __init__(self):
        self.money = 0
        self.making_rate = 1  # Money earned per second
        self.upgrade_cost = 100  # Cost to upgrade machine
        self.upgrade_rate = 2  # Money earned per second after upgrade
    
    def earn_money(self):
        """Earn money over time."""
        while True:
            time.sleep(1)  # Simulate earning money every second
            self.money += self.making_rate
    
    def upgrade_machine(self):
        """Upgrade the machine to make more money."""
        if self.money >= self.upgrade_cost:
            self.money -= self.upgrade_cost
            self.making_rate = self.upgrade_rate
            self.upgrade_cost *= 2  # Upgrade cost increases after each upgrade
            return True
        return False

def run_machine(machine):
    """Start the earning money process in a separate thread."""
    threading.Thread(target=machine.earn_money, daemon=True).start()

def main():
    # Initialize the MoneyMakerMachine
    machine = MoneyMakerMachine()

    st.title("💸 Money Maker Machine 🤑")
    
    # Run the machine in a background thread
    run_machine(machine)

    # Show current money balance
    st.subheader("Your Balance: $")
    balance = st.empty()
    balance.text(f"${machine.money}")

    # User actions
    action = st.selectbox(
        "Choose an action:",
        ["Earn Money", "Check Balance", "Upgrade Machine", "Exit"]
    )

    if action == "Earn Money":
        st.write("The machine is earning money every second... 💰")
    elif action == "Check Balance":
        balance.text(f"${machine.money}")
    elif action == "Upgrade Machine":
        if machine.upgrade_machine():
            st.success(f"Machine upgraded! Now earning ${machine.making_rate} per second.")
        else:
            st.warning("Not enough money to upgrade! 💸")
    elif action == "Exit":
        st.write("Goodbye! 💸")

if __name__ == "__main__":
    main()

