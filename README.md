# MISP integration with Athena demo

This project has some snippets for:
- Querying the MISP api to get a dump of attributes
- Setting up Athena database for MISP attributes
- Setting up Athena database for VPC Flow logs
- Querying threat indicators in VPC Flow logs from MISP data with Athena

![Architecture](https://raw.githubusercontent.com/colbyprior/misp-athena-demo/master/docs/Misp_Flow_logs.png)

## Reference points
- [MISP](https://github.com/MISP/MISP)
- [PyMISP](https://github.com/MISP/PyMISP)
- [VPC Flow Logs with Athena](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html)
- [Guard Duty Custom Rules](https://aws.amazon.com/blogs/security/how-to-automate-import-third-party-threat-intelligence-feeds-into-amazon-guardduty/)
- [Athena Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/athena.html)
- [How I made my diagrams](https://cloudcraft.co/)
