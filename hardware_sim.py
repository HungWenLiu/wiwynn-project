import random
from datetime import datetime


class HardwareSimulator:
    def get_metrics(self):
        # 模擬伺服器 Sensor 數值
        # 邏輯：隨機生成數據，若超過閾值則標記為 Critical
        cpu_temp = random.randint(40, 98)
        fan_rpm = random.randint(2000, 15000)
        voltage = round(random.uniform(11.8, 12.2), 2)

        status = "Healthy"
        if cpu_temp > 95:
            status = "Critical: CPU Overheat"
        elif fan_rpm < 3000:
            status = "Warning: Fan Failure"

        return {
            "timestamp": datetime.now().isoformat(),
            "sensor_data": {
                "cpu_temp_c": cpu_temp,
                "fan_speed_rpm": fan_rpm,
                "voltage_v": voltage,
            },
            "system_status": status,
        }
