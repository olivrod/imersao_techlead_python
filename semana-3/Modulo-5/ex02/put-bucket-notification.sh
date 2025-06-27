aws s3api put-bucket-notification-configuration \
    --bucket 42sp-rde-oliv-boletos \
    --notification-configuration file://queue-configuration.json

#aws s3api get-bucket-notification-configuration --bucket "42sp-rde-oliv-boletos" --no-cli-pager
#python3 ../ex01/upload_boletos.py ../remessas/boletos_0001.csv