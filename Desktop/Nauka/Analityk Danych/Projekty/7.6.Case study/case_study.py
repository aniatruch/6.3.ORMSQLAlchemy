import numpy as np
import numpy_financial as npf
import matplotlib.pyplot as plt

M0 = 120_000            # cena mieszkania teraz
r_annual = 0.05         # roczny wzrost ceny mieszkania
years = 5
months = years * 12

nominal_annual_rate = 0.12
i = nominal_annual_rate / 12  # miesięczna stopa procentowa

M5 = M0 * (1 + r_annual)**years
print(f"Orientacyjna cena mieszkania za 5 lat: {M5:.2f} zł")

P = M5 * i / ((1 + i)**months - 1)
print(f"Miesięczna wpłata do banku: {P:.2f} zł")

M_monthly = np.linspace(M0, M5, months)

months_arr = np.arange(1, months + 1)
FV_values = P * ((1 + i)**months_arr - 1) / i

# Wykres
plt.figure(figsize=(10,6))
plt.plot(months_arr, M_monthly, label="Cena mieszkania")
plt.plot(months_arr, FV_values, label="Wartość lokaty")
plt.xlabel("Miesiące")
plt.ylabel("Zł")
plt.title("Zmiana ceny mieszkania i wartości lokaty w czasie")
plt.legend()
plt.grid(True)
plt.show()