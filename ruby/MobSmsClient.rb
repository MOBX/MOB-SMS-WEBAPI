=begin
Desc:短信http接口的ruby代码调用示例
author luckscript
date 2017-03-09
=end

require 'net/http'
require 'uri'
params = {}


#修改为您的appkey.在官网（http://www.mob.com)登录后获取,接口地址联系客服
appkey = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
#修改为您要发送的手机号码
phone = '18912386146'
#修改为您要发送的国家代码
zone = '86'

#Web-Api验证码发送接口
get_webapi_send_uri = URI.parse('https://webapi.sms.mob.com/xxxxx')
#Web-Api验证码验证接口
get_webapi_check_uri = URI.parse('https://webapi.sms.mob.com/xxxxx')

#请求下发短信验证码
params['appkey'] = appkey
params['phone'] = phone
params['zone'] = zone
response =  Net::HTTP.post_form(get_webapi_sendmsg_uri,params)
print response.body + "\n"

#请求校验短信验证码
code = '1234'
params['appkey'] = appkey
params['phone'] = phone
params['zone'] = zone
params['code'] = code
response = Net::HTTP.post_form(get_webapi_checkcode_uri,params)
print response.body + "\n"
