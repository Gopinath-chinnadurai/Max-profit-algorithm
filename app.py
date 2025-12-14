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


def find_best_solution(total_time):
    max_profit = 0
    best_t = best_p = best_c = 0

    for t in range(0, total_time // 5 + 1):
        for p in range(0, total_time // 4 + 1):
            for c in range(0, total_time // 10 + 1):

                sequence = ["T"] * t + ["P"] * p + ["C"] * c
                profit = calculate_profit(sequence, total_time)

                if profit > max_profit:
                    max_profit = profit
                    best_t, best_p, best_c = t, p, c

    return best_t, best_p, best_c, max_profit



st.set_page_config(page_title="Max Profit Problem", layout="centered")

st.title(" Max Profit Problem")
st.write("Find the best combination of buildings to maximize profit.")

time_units = st.number_input(
    "Enter Total Time Units (n):",
    min_value=1,
    step=1
)

if st.button("Calculate Max Profit"):
    t, p, c, profit = find_best_solution(time_units)

    st.subheader(" Best Solution")

    st.write(f" **Theatres (T):** {t}   |    **Pubs (P):** {p}   |    **Commercial Parks (C):** {c}")

    st.subheader(" Total Earnings")
    st.success(f"${profit}")
