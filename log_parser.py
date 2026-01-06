from typing import List


class LogAnalyzer:
    def analyze(self, logs: List[str]):
        # 模擬測試工程師分析 Serial Log 或 dmesg
        error_count = 0
        found_errors = []

        # 關鍵字過濾邏輯
        critical_keywords = ["KERNEL PANIC", "SEGMENTATION FAULT", "TIMEOUT"]

        for line in logs:
            upper_line = line.upper()
            for keyword in critical_keywords:
                if keyword in upper_line:
                    error_count += 1
                    found_errors.append(line)
                    break

        return {
            "scanned_lines": len(logs),
            "error_count": error_count,
            "errors": found_errors,
            "test_result": "PASS" if error_count == 0 else "FAIL",
        }
