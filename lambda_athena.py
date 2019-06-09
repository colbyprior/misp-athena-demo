import boto3

session = boto3.Session()
client = session.client('athena', region_name='ap-southeast-2')

response = client.start_query_execution(
    QueryString='select * from vpc_flow_logs limit 100;',
    QueryExecutionContext={
        'Database': 'vpc_logs'
    },
    ResultConfiguration={
        'OutputLocation': 's3://<bucket>'
    }
)
