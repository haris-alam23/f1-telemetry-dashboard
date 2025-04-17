import fastf1
import matplotlib.pyplot as plt

session = fastf1.get_session(2024, "Monza", "Q")
session.load()

lec_lap = session.laps.pick_driver("LEC").pick_fastest()
ver_lap = session.laps.pick_driver("HAM").pick_fastest()

lec_tele = lec_lap.get_car_data().add_distance()
ver_tele = ver_lap.get_car_data().add_distance()

plt.figure(figsize=(10,6))
plt.plot(lec_tele['Distance'],lec_tele['Speed'], label = 'Leclerc', color = 'red')
plt.plot(ver_tele['Distance'], ver_tele['Speed'], label = 'Verstappen', color = 'blue')


plt.title('Qualifying Speed Comparison - 2024 Monza')
plt.xlabel('Distance (m)')
plt.ylabel('Speed (km/h)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()