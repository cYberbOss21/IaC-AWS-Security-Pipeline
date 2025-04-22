
# 🛡️ Cloud IaC + AWS Security Pipeline with Jira Automation

A project that simulates a DevSecOps pipeline by scanning Terraform for misconfigurations, mapping them to MITRE ATT&CK and CIS benchmarks, and automatically creating Jira tickets. It also scans live AWS EC2 security groups for open ports and generates Markdown reports.

---

## 📸 Architecture
![image](https://github.com/user-attachments/assets/420365c0-5976-4ddb-9944-8e6a0878a1a6)

---

## ⚠️ Disclaimer
This project is for educational and professional development purposes only. Do not use it in production or environments that contain sensitive infrastructure. Ensure compliance with organizational and legal guidelines before deploying any automated remediation tools.

---

## 🔍 What Is This Pipeline?
This project integrates:
- **Checkov** to scan Terraform IaC for misconfigurations
- **Jira API** to auto-create tickets for failed checks
- **MITRE ATT&CK + CIS Benchmarks** for mapping each finding
- **boto3** to scan live AWS Security Groups and identify risky rules

---

## 🎯 Why This Project Matters
This end-to-end cloud security pipeline helps:

- Catch security misconfigurations before deployment (shift-left security)
- Correlate findings to industry standards (MITRE + CIS)
- Automate ticketing for faster remediation
- Visualize real misconfigs in AWS using EC2 and Security Groups

---

## 📊 Cloud Security Stats
- 🔍 [**67% of cloud breaches** are due to misconfigured resources](https://www.gartner.com/smarterwithgartner/is-the-cloud-secure) — Gartner
- 📌 [**99% of cloud security failures** will be the customer’s fault](https://www.gartner.com/en/newsroom/press-releases/2019-06-25-gartner-says-through-2025-99--of-cloud-security-fail) — Gartner
- 🚀 [**MITRE ATT&CK adoption among blue teams** increased by 80%](https://attack.mitre.org/resources/adoption/) — MITRE

---

## 🛠 Project Features
✅ Scans Terraform configs using Checkov  
✅ Maps misconfigs to MITRE ATT&CK + CIS Benchmarks  
✅ Auto-generates Jira tickets using Python + Jira API  
✅ Scans live AWS EC2 Security Groups using boto3  
✅ Generates Markdown security reports  
✅ Deployable from EC2 instance or local environment

---

## 👩‍💻 For Cybersecurity Analysts
This project helps you build experience in:
- Cloud misconfiguration detection
- Python scripting for security automation
- Ticketing system integrations (Jira, Slack)
- Threat mapping using MITRE ATT&CK
- Infrastructure-as-Code scanning and remediation
- Real-world AWS security workflows

Use it to demonstrate:
- Threat detection  
- Alerting pipeline creation  
- Security control validation and monitoring  

---

## 🤝 Contributing
Pull requests, mapping additions, tool integrations (e.g., Slack, SIEM, Discord), or remediation enhancements are welcome!

1. Fork the repo  
2. Add your changes  
3. Submit a pull request  




