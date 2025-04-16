import fastf1
import matplotlib.pyplot as plt



session = fastf1.get_session(2024,'Abu Dhabi', 'Race')
session.load()

hamilton_session = session.laps.pick_driver(44).pick_fastest()

print(hamilton_session)


hamilton_car_data = hamilton_session.get_car_data()
car_data = hamilton_car_data.add_distance()

plt.plot(car_data['Distance'], car_data['Speed'], label = 'Hamilton')
plt.xlabel("Distance (m)")
plt.ylabel("Speed (km/h)")
plt.title("Hamilton Speed vs. Distance - Abu Dhabi 2024")
plt.show()