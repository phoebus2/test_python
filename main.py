import os
from datetime import datetime, timedelta, timezone

base_datetime =  datetime.now(timezone.utc)
print(base_datetime)

previous_datetime = base_datetime.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=-1)
print(previous_datetime)

date_path = '/date=' + previous_datetime.strftime("%Y%m%d")
print(date_path)

year = 'year=' + str(previous_datetime)[:4]
# print(year)
month = 'month=' + str(previous_datetime)[5:7]
day = 'day=' + str(previous_datetime)[8:10]
print(year+'/'+month+'/'+day)

source_base_path = 'thinq-care-result/summary'
copy_bucket_name = source_base_path.split('/')[0]
file_count_check_path = os.path.join(copy_bucket_name+'/'+'file_count_check')
print(file_count_check_path)

tt = 'thinq-care-result-us-dev/file_count_check/test/server=T10/region=AIC/country=MX/category=201/date=20220823/integration-parser-v1_9_8-plv1_00110ac1-805c-4b3c-96ff-e8fe846c006c_gz-0.gz'
ss = '/'.join(tt.split('/')[2:])
print(ss)


aa = 'file_count_check/test/server=T10/region=AIC/country=MX/category=202/date=20220821/integration-parser-v1_9_8-plv1_0043a3c7-875d-4cb1-a44e-797bc4d3f1ad_gz-0.gz'
qq = '/'.join(aa.split('/')[1:])
print(qq)


bb = 'integration-parser-v1_9_8-plv1_7c82640a-20d4-4610-b8d5-552e1368dd2d_gz-0.gz'
print(bb.split('.')[:1])

copy_obj_key = 'file_count_check' + '/' + bb.split('.')[:1]
print(copy_obj_key)