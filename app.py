import streamlit as st

buildings = {
    "T": {"name": "Theatre", "time": 5, "earning": 1500},
    "P": {"name": "Pub", "time": 4, "earning": 1000},
    "C": {"name": "Commercial Park", "time": 10, "earning": 2000}
}

def calculate_profit(sequence, total_time):
    current_time = 0
    total_profit = 0

    for b in sequence:
        current_time += buildings[b]["time"]

        if current_time > total_time:
            return 0

        operational_time = total_time - current_time
        total_profit += operational_time * buildings[b]["earning"]

    return total_profit


def find_best_solutions(total_time):
    max_profit = 0
    best_solutions = []

    for t in range(0, total_time // 5 + 1):
        for p in range(0, total_time // 4 + 1):
            for c in range(0, total_time // 10 + 1):

                sequence = ["T"] * t + ["P"] * p + ["C"] * c
                profit = calculate_profit(sequence, total_time)

                if profit > max_profit:
                    max_profit = profit
                    best_solutions = [(t, p, c)]

                elif profit == max_profit and profit > 0:
                    best_solutions.append((t, p, c))

    return best_solutions, max_profit


# ---------------- UI ---------------- 

st.set_page_config(page_title="Max Profit Problem", layout="centered")

st.title(" Max Profit Problem")
st.write("Find **all optimal combinations** of buildings that maximize profit.")

time_units = st.number_input(
    "Enter Total Time Units (n):",
    min_value=1,
    step=1
)

if st.button("Calculate Max Profit"):
    solutions, profit = find_best_solutions(time_units)

    st.subheader(" Maximum Profit")
    st.success(f"${profit:,}")

    st.subheader(" All Optimal Solutions")

    for idx, (t, p, c) in enumerate(solutions, 1):
        st.markdown(
    f"**Option {idx}:**  Theatre (T): {t} |  Pub (P): {p} |  Commercial Park (C): {c}"
)
