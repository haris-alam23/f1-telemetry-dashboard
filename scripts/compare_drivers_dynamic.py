import fastf1
import matplotlib.pyplot as plt

def compare_drivers_dynamic(driver1, driver2, year, gp, session_type):
    
    session = fastf1.get_session(year, gp, session_type)
    session.load()
    
    driver1lap = session.laps.pick_drivers(driver1).pick_fastest()
    driver2lap = session.laps.pick_drivers(driver2).pick_fastest()
    
    if driver1lap.empty or driver2lap.empty:
        print("No valid laps found.")
        return
    
    driver1tel = driver1lap.get_car_data().add_distance()
    driver2tel = driver2lap.get_car_data().add_distance()
    
    if driver1tel.empty or driver2tel.empty:
        print("Missing Telemetry Data")
        return
    
    fig, axs = plt.subplots(4,1, figsize =(12,10), sharex= True)

    # Speed    
    axs[0].plot(driver1tel['Distance'], driver1tel['Speed'], label = driver1, color = 'red')
    axs[0].plot(driver2tel['Distance'], driver2tel['Speed'], label = driver2, color = 'blue')
    axs[0].set_ylabel('Speed (km/h)')
    axs[0].legend()

    #Throttle
    axs[1].plot(driver1tel['Distance'], driver1tel['Throttle'], label = driver1, color = 'red')
    axs[1].plot(driver2tel['Distance'], driver2tel['Throttle'], label = driver2, color = 'blue')
    axs[1].set_ylabel('Throttle (%)')
    axs[1].legend()
    
    axs[2].plot(driver1tel['Distance'], driver1tel['Brake'], label = driver1, color = 'red')
    axs[2].plot(driver2tel['Distance'], driver2tel['Brake'], label = driver2, color = 'blue')
    axs[2].set_ylabel('Brake (bool)')
    axs[2].legend()
    
    axs[3].plot(driver1tel['Distance'], driver1tel['nGear'], label = driver1, color = 'red')
    axs[3].plot(driver2tel['Distance'], driver2tel['nGear'], label = driver2, color = 'blue')
    axs[3].set_ylabel('Gear')
    axs[3].legend()
    
    fig.suptitle(f'Telemetry Comparison = {driver1} vs {driver2} - {gp} - {year} - {session_type}')
    plt.tight_layout()
    plt.subplots_adjust(top = 0.92)
    plt.show()

compare_drivers_dynamic('VER','HAM',2021,'Abu Dhabi','Race')
