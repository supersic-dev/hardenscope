import yaml
import subprocess

def load_rules(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)

def run_rule(rule):
    try:
        output = subprocess.getoutput(rule["check"]).strip()
        passed = output == rule["expected_output"]
        return {
            "id": rule["id"],
            "title": rule["title"],
            "passed": passed,
            "output": output,
            "expected": rule["expected_output"],
            "remediation": rule["remediation"]
        }
    except Exception as e:
        return {
            "id": rule["id"],
            "title": rule["title"],
            "passed": False,
            "error": str(e)
        }
