import boto3
import xlwt
ec2 = boto3.client(
    service_name='ec2',
)
response = ec2.describe_instances()
Instance_list = []
for i in response['Reservations']:
    ret = i['Instances'][0]['Tags']
    for j in ret:
        InstanceId = i['Instances'][0]['InstanceId']
        Tags = i['Instances'][0]['Tags']
        Instance_item = [InstanceId,Tags]
        Instance_list.append(Instance_item)
# print(Instance_list)


wb = xlwt.Workbook(encoding = 'ascii')    #创建实例，并且规定编码
sheet = wb.add_sheet('AWS EC2')
# 标题样式
style_title = xlwt.XFStyle()
font_title = xlwt.Font()
font_title.name = u'宋体'
font_title.color = 'black'
font_title.height = 440
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
style_title.alignment = alignment
style_title.font = font_title

# 内容样式
style_content = xlwt.XFStyle()
font_content = xlwt.Font()
font_content.name = u'宋体'
font_content.color = 'black'
font_content.height = 220
alignment = xlwt.Alignment()
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 水平方向
alignment.vert = xlwt.Alignment.VERT_CENTER  # 竖直方向
style_content.alignment = alignment
style_content.font = font_content

sheet.write_merge(0, 0, 0, 3, '标签统计', style_title)
sheet.write(1, 0, '实例ID', style_content)
sheet.write_merge(1, 1, 1, 3, '标签', style_content)
for row, i in enumerate(Instance_list, 1):
    id = i[0]
    tags = i[1]
    row = row*4
    sheet.write(row, 0, id, style_content)
    count = 0
    for j in tags:
        sheet.write(row + count, 1, j['Key'], style_content)
        sheet.write(row + count, 2, j['Value'], style_content)
        count += 1
wb.save('shee.xls')