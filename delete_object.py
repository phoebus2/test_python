def remove_file_count_check(s3_client, bucket, event_list, previous_datetime):
    access_key, secret_key, bucket_name = get_config()
    date_path = '/date=' + previous_datetime.strftime("%Y%m%d")
    paginator = s3_client.get_paginator('list_objects_v2')
    delete_key = dict(Objects=[])
    resp = []
    for event in event_list:
        prefix = 'file_count_check/' + event + date_path
        pages = paginator.paginate(Bucket=bucket, Prefix=prefix)
        for page in pages:
            if 'Contents' in page:
                for i in page['Contents']:
                    delete_key['Objects'].append(dict(Key=i['Key']))
                    S3Util.remove_s3_object(access_key, secret_key, bucket_name, i['Key'])
                    #print('delete_key_cnt1:', len(delete_key['Objects']))
                    #if len(delete_key['Objects']) >= 1000:
                        #resp = s3_client.delete_objects(Bucket=bucket, Delete=delete_key)
                        #delete_key = dict(Objects=[])

                #if len(delete_key['Objects']):
                #    print('delete_key_cnt2:', len(delete_key['Objects']))
                #    resp = s3_client.delete_objects(Bucket=bucket, Delete=delete_key)
                    
    return resp