import boto3
from datetime import datetime

def scan_and_generate_report():
    ec2 = boto3.client('ec2', region_name='us-east-2')
    response = ec2.describe_security_groups()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_name = f"sg_misconfig_report_{timestamp}.md"

    with open(report_name, "w") as report:
        report.write("# Security Group Misconfiguration Report\n")
        report.write(f"**Generated:** {datetime.now()}\n\n")

        for sg in response['SecurityGroups']:
            group_name = sg['GroupName']
            group_id = sg['GroupId']
            report.write(f"## {group_name} ({group_id})\n")

            for permission in sg['IpPermissions']:
                from_port = permission.get('FromPort', 'ALL')
                to_port = permission.get('ToPort', 'ALL')
                ip_ranges = permission.get('IpRanges', [])

                for ip_range in ip_ranges:
                    cidr = ip_range.get('CidrIp')
                    if cidr == "0.0.0.0/0":
                        report.write(f"- **Port {from_port}-{to_port} open to the world** (`{cidr}`)\n")
            report.write("\n")

    print(f"\n[+] Report saved as {report_name}")

if __name__ == "__main__":
    scan_and_generate_report()
