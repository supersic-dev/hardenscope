import subprocess

def apply_remediation(rule):
    try:
        result = subprocess.run(rule["remediation"], shell=True, check=True)
        return True, "Remediation applied successfully."
    except subprocess.CalledProcessError as e:
        return False, f"Failed to apply remediation: {e}
